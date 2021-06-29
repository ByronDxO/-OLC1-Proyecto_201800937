from Interprete.TS.Exception import Exception
from Interprete.Abstract.Instruccion import Instruccion
from Interprete.TS.Simbolo import Simbolo
from Interprete.Abstract.NodoAST import NodoAST


class Declaracion(Instruccion):
    def __init__(self, tipo, identificador, fila, columna, expresion=None):
        self.identificador = identificador
        self.tipo = tipo
        self.expresion = expresion
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):

        if self.expresion != None:
            value = self.expresion.interpretar(tree, table) # Valor a asignar a la variable
            if isinstance(value, Exception): return value
            self.tipo = self.expresion.tipo
        else:
            value = None

        simbolo = Simbolo(str(self.identificador).lower(), self.tipo, self.fila, self.columna, value)
        
        result = table.setTabla(simbolo)
  
        if isinstance(result, Exception): return result
        
        return None

    
    def getNodo(self):
        nodo = NodoAST("DECLARACION")
        nodo.agregarHijo(str(self.tipo))
        nodo.agregarHijo(str(self.identificador))
        if self.expresion != None:
            nodo.agregarHijoNodo(self.expresion.getNodo())
        return nodo
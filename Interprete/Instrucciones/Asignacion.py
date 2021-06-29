from Interprete.Expresiones.Identificador import Identificador
from Interprete.TS.Exception import Exception
from Interprete.Abstract.Instruccion import Instruccion
from Interprete.TS.Simbolo import Simbolo
from Interprete.Abstract.NodoAST import NodoAST


class Asignacion(Instruccion):

    def __init__(self, identificador, expresion, fila, columna):
        self.identificador = identificador
        self.expresion = expresion
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        value = self.expresion.interpretar(tree, table) # Valor a asignar a la variable
        if isinstance(value, Exception): return value
        
        simbolo = Simbolo(str(self.identificador).lower(), self.expresion.tipo, self.fila, self.columna, value)
        result = table.actualizarTabla(simbolo)
        
        if isinstance(result, Exception): return result
        return None

    def getNodo(self):
        nodo = NodoAST("ASIGNACION")

        nodo.agregarHijo(str(self.expresion.tipo))
        nodo.agregarHijo(str(self.identificador))
        nodo.agregarHijoNodo(self.expresion.getNodo())
        return nodo
from Interprete.TS.Tipo import Operador_Aritmetico, Tipo
from Interprete.Expresiones.Identificador import Identificador
from Interprete.TS.Exception import Exception
from Interprete.Abstract.Instruccion import Instruccion
from Interprete.TS.Simbolo import Simbolo
from Interprete.Abstract.NodoAST import NodoAST


class IncrementoDecremento(Instruccion):

    def __init__(self, identificador, tipo, fila, columna):
        self.identificador = identificador
        self.tipo = tipo
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        
        if self.tipo == Operador_Aritmetico.INCREMENTO:
            simbolo = table.getTabla(self.identificador.lower())
            if simbolo is None:
                return None
            if simbolo.tipo == Tipo.ENTERO or simbolo.tipo == Tipo.DECIMAL:
                simbolo.valor = simbolo.valor + 1
                #self.tipo = simbolo.tipo
            else:
                 return Exception("Semantico", "Error de Tipo de dato.", self.fila, self.columna)
       

        elif self.tipo == Operador_Aritmetico.DECREMENTO:
            simbolo = table.getTabla(self.identificador.lower())
            if simbolo is None:
                return None
            if simbolo.tipo == Tipo.ENTERO or simbolo.tipo == Tipo.DECIMAL:
                simbolo.valor = simbolo.valor - 1
                #self.tipo = simbolo.tipo
            else:
                return Exception("Semantico", "Error de Tipo de dato.", self.fila, self.columna)
        else:
            return Exception("Semantico", "Variable " + self.identificador + " Diferente tipo de dato.", self.fila, self.columna)
       
        #simbolo_nuevo = Simbolo(self.identificador.lower(), simbolo.tipo, self.fila, self.columna, simbolo.valor)
        result = table.actualizarTabla(simbolo)
        if isinstance(result, Exception): return result

        return result

    def getNodo(self):
        nodo = NodoAST("ASIGNACION")
        nodo.agregarHijo(str(self.tipo))
        nodo.agregarHijo(str(self.identificador))
        return nodo
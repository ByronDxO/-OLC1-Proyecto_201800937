from Interprete.Abstract.Instruccion import Instruccion
from Interprete.TS.Exception import Exception
from Interprete.TS.Tipo import Tipo
from Interprete.TS.TablaSimbolo import TablaSimbolo
from Interprete.Abstract.NodoAST import NodoAST

class Return(Instruccion):
    def __init__(self, expresion, fila, columna):
        self.expresion = expresion
        self.fila = fila
        self.columna = columna
        self.tipo = None
        self.result = None

    def interpretar(self, tree, table):
        result = self.expresion.interpretar(tree, table)
        if isinstance(result, Exception): return result

        self.tipo = self.expresion.tipo # Aqui va a guardar el tipo de la expresion a interpretar.
        self.result = result            # Aqui ya optiene el resultado de la expresion a interpretar.

        return self


    def getNodo(self):
        nodo = NodoAST("RETURN")

        nodo.agregarHijoNodo(self.expresion.getNodo())

        return nodo
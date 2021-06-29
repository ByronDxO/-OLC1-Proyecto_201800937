from Interprete.Abstract.Instruccion import Instruccion
from Interprete.Abstract.NodoAST import NodoAST

class Primitivos(Instruccion):
    
    def __init__(self, tipo, valor, fila, columna):
        self.tipo = tipo
        self.valor = valor
        self.fila = fila
        self.columna = columna
    
    def interpretar(self, tree, table):
        return self.valor

    def getNodo(self):
        nodo = NodoAST("PRIMITIVO")
        nodo.agregarHijo(str(self.valor))
        return nodo
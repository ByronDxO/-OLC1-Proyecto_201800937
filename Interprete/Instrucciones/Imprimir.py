'''
    isinstance -> Recibe como argumentos un objeto y una clase, y devuelve True si el objeto es una instancia de dicha clase o de una subclase de ella.
'''
from Interprete.Abstract.Instruccion import Instruccion
from Interprete.TS.Tipo import Tipo
from Interprete.TS.Exception import Exception
from Interprete.Abstract.NodoAST import NodoAST

class Imprimir(Instruccion):
    
    def __init__(self, expresion, fila, columna):
        self.expresion = expresion
        self.fila = fila
        self.columna = columna
    
    def interpretar(self, tree, tabla):
        value = self.expresion.interpretar(tree, tabla)

        if isinstance(value, Exception):
            return value

        if self.expresion.tipo == Tipo.ARREGLO:
            return Exception("Semantico", "No se puede imprimir un arreglo", self.fila, self.columna)

        tree.update_consola(value)

    def getNodo(self):
        nodo = NodoAST("IMPRIMIR")
        nodo.agregarHijoNodo(self.expresion.getNodo())
        return nodo
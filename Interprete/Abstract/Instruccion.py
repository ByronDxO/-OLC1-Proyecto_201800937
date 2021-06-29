'''
    -----------------------------------
    Implementación de clase  Abstracta.
    -----------------------------------
'''
from abc import ABC, abstractmethod

class Instruccion(ABC):

    def __init__(self, fila, columna):      # fila y columna, ingresa el punto exacto de la entrada
        self.fila = fila
        self.columna = columna
        super().__init__()

    @abstractmethod
    def interpretar(self, tree, table):
        pass

    @abstractmethod
    def getNodo(self):
        pass

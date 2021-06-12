from Interprete.Abstract.Instruccion import Instruccion
from Interprete.TS.Exception import Exception
from Interprete.TS.Tipo import Tipo, Operador_Relacional

class Relacional(Instruccion):
    def __init__(self, operador, OperacionIzq, OperacionDer, fila, columna):
        self.operador = operador
        self.OperacionIzq = OperacionIzq
        self.OperacionDer = OperacionDer
        self.fila = fila
        self.columna = columna
        self.tipo = Tipo.BOOLEANO
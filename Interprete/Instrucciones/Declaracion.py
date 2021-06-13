from Interprete.TS.Exception import Exception
from Interprete.Abstract.Instruccion import Instruccion
from Interprete.TS.Simbolo import Simbolo


class Declaracion(Instruccion):
    def __init__(self, tipo, identificador, fila, columna, expresion=None):
        self.identificador = identificador
        self.tipo = tipo
        self.expresion = expresion
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        value = self.expresion.interpretar(tree, table) # Valor a asignar a la variable
        if isinstance(value, Exception): return value
        
        simbolo = Simbolo(str(self.identificador), self.tipo, self.fila, self.columna, value)
        result = table.setTabla(simbolo)

        if isinstance(result, Exception): return result
        return None


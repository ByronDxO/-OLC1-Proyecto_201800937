from Interprete.TS.Exception import Exception
from Interprete.Abstract.Instruccion import Instruccion


class Identificador(Instruccion):
    def __init__(self, identificador, fila, columna):
        self.identificador = identificador
        self.fila = fila
        self.columna = columna
        self.tipo = None

    def interpretar(self, tree, table):
        simbolo = table.getTabla(self.identificador.lower())
        if simbolo == None:
            return Exception("Semantico", "Variable " + self.identificador + " no encontrada.", self.fila, self.columna)

        self.tipo = simbolo.get_tipo()
        
        
        return simbolo.get_valor()
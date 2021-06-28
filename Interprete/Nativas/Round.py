from Interprete.TS.Exception import Exception
from Interprete.TS.Tipo import Tipo
from Interprete.Instrucciones.Funcion import Funcion
import math

class Round(Funcion):
    def __init__(self, nombre, parametros, instrucciones, fila, columna):
        self.nombre = nombre.lower()
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna
        self.tipo = Tipo.NULO
    
    def interpretar(self, tree, table):
        simbolo = table.getTabla("round##Param1")
        if simbolo == None : return Exception("Semantico", "No se encontró el parámetro de Truncate", self.fila, self.columna)

        if simbolo.get_tipo() != Tipo.DECIMAL and simbolo.get_tipo() != Tipo.ENTERO:
            return Exception("Semantico", "Tipo de parametro de Round no es un valor.", self.fila, self.columna)
        
        self.tipo = Tipo.ENTERO
        if simbolo.get_tipo() == Tipo.DECIMAL:
            if str(simbolo.get_valor()).split('.')[1][0] >= '5':
                return int(math.ceil(simbolo.get_valor()))
        return round(simbolo.get_valor())
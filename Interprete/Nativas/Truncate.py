from Interprete.TS.Exception import Exception
from Interprete.TS.Tipo import Tipo
from Interprete.Instrucciones.Funcion import Funcion

class Truncate(Funcion):
    def __init__(self, nombre, parametros, instrucciones, fila, columna):
        self.nombre = nombre.lower()
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna
        self.tipo = Tipo.NULO
    
    def interpretar(self, tree, table):
        simbolo = table.getTabla("truncate##Param1")
        if simbolo == None : return Exception("Semantico", "No se encontró el parámetro de Truncate", self.fila, self.columna)

        if simbolo.get_tipo() != Tipo.ENTERO:
            return Exception("Semantico", "Tipo de parametro de Truncate no es un valor.", self.fila, self.columna)
        
        self.tipo = simbolo.get_tipo()
        return int(simbolo.get_valor())
from Interprete.TS.Exception import Exception
from Interprete.TS.Tipo import Tipo
from Interprete.Instrucciones.Funcion import Funcion

class Length(Funcion):
    def __init__(self, nombre, parametros, instrucciones, fila, columna):
        self.nombre = nombre.lower()
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna
        self.tipo = Tipo.NULO
    
    def interpretar(self, tree, table):
        simbolo = table.getTabla("length##Param1")
        if simbolo == None : return Exception("Semantico", "No se encontró el parámetro de Length", self.fila, self.columna)

        if simbolo.get_tipo() != Tipo.CADENA:
            return Exception("Semantico", "Tipo de parametro de Length no es cadena.", self.fila, self.columna)

        self.tipo = simbolo.get_tipo()
        return len(simbolo.get_valor())
from Interprete.TS.Exception import Exception
from Interprete.TS.Tipo import Tipo
from Interprete.Instrucciones.Funcion import Funcion

class TypeOf(Funcion):
    def __init__(self, nombre, parametros, instrucciones, fila, columna):
        self.nombre = nombre.lower()
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna
        self.tipo = Tipo.NULO
    
    def interpretar(self, tree, table):
        simbolo = table.getTabla("typeOf##Param1")
        if simbolo == None : return Exception("Semantico", "No se encontró el parámetro de TypeOf", self.fila, self.columna)
        
        if simbolo.get_tipo() == Tipo.NULO:
            return Exception("Semantico", "Tipo de parametro de TypeOf es Nulo.", self.fila, self.columna)
        
        self.tipo = simbolo.get_tipo()

        if self.tipo == Tipo.ENTERO:
            return "INT"
        elif self.tipo == Tipo.DECIMAL:
            return "DOUBLE"
        elif self.tipo == Tipo.BOOLEANO:
            return "BOOLEAN"
        elif self.tipo == Tipo.CHAR:
            return "CHAR"      
        elif self.tipo == Tipo.BOOLEANO:
            return "BOOLEAN"
        elif self.tipo == Tipo.CADENA:
            return "STRING"


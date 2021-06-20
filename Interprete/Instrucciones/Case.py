from Interprete.Instrucciones.IncrementoDecremento import IncrementoDecremento
from Interprete.Instrucciones.Declaracion import Declaracion
from Interprete.Instrucciones.Asignacion import Asignacion
from Interprete.Abstract.Instruccion import Instruccion
from Interprete.TS.Exception import Exception
from Interprete.TS.Tipo import Tipo
from Interprete.TS.TablaSimbolo import TablaSimbolo
from Interprete.Instrucciones.Break import Break

class Case(Instruccion):
    def __init__(self, condicion, instrucciones,  fila, columna):
        self.condicion = condicion
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        result = self.condicion.interpretar(tree, table)
        if isinstance(result, Exception): return result

        return result

    def get_instrucciones_case(self):
        return self.instrucciones
    
    def set_instrucciones_case(self, instrucciones):
        self.instrucciones = instrucciones
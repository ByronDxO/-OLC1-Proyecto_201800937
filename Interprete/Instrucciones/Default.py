from Interprete.Instrucciones.IncrementoDecremento import IncrementoDecremento
from Interprete.Instrucciones.Declaracion import Declaracion
from Interprete.Instrucciones.Asignacion import Asignacion
from Interprete.Abstract.Instruccion import Instruccion
from Interprete.TS.Exception import Exception
from Interprete.TS.Tipo import Tipo
from Interprete.TS.TablaSimbolo import TablaSimbolo
from Interprete.Instrucciones.Break import Break
from Interprete.Abstract.NodoAST import NodoAST

class Default(Instruccion):
    def __init__(self, instrucciones,  fila, columna):
        self.condicion = None
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        return None

    def getNodo(self):
        nodo = NodoAST("DEFAULT")

        if self.instrucciones != None:
            instruccionesDefault = NodoAST("INSTRUCCIONES DEFAULT")
            for instr in self.instrucciones:
                instruccionesDefault.agregarHijoNodo(instr.getNodo())
            nodo.agregarHijoNodo(instruccionesDefault)
        return nodo
    
    def get_instrucciones_default(self):
        return self.instrucciones
    
    def set_instrucciones_default(self, instrucciones):
        self.instrucciones = instrucciones
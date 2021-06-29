from Interprete.Abstract.Instruccion import Instruccion
from Interprete.TS.Exception import Exception
from Interprete.TS.TablaSimbolo import TablaSimbolo
from Interprete.Instrucciones.Break import Break
from Interprete.Instrucciones.Return import Return
from Interprete.Instrucciones.Continue import Continue
from Interprete.Abstract.NodoAST import NodoAST


class Main(Instruccion):
    def __init__(self, instrucciones, fila, columna):
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna
    
    def interpretar(self, tree, table):
        nuevaTabla = TablaSimbolo(table) 
        for instruccion in self.instrucciones:      # REALIZAR LAS ACCIONES
            value = instruccion.interpretar(tree,nuevaTabla)
            if isinstance(value, Exception) :
                tree.get_excepcion().append(value)
                tree.update_consola(value.__str__())
            if isinstance(value, Break): 
                err = Exception("Semantico", "Sentencia Break fuera de ciclo", instruccion.fila, instruccion.columna)
                tree.get_excepcion().append(err)
                tree.update_consola(err.__str__())
            if isinstance(value, Return): 
                err = Exception("Semantico", "Sentencia Return fuera de ciclo", instruccion.fila, instruccion.columna)
                tree.get_excepcion().append(err)
                tree.update_consola(err.__str__())
            if isinstance(value, Continue): 
                err = Exception("Semantico", "Sentencia Continue fuera de ciclo", instruccion.fila, instruccion.columna)
                tree.get_excepcion().append(err)
                tree.update_consola(err.__str__())

    def getNodo(self):
        nodo = NodoAST("MAIN")

        instrucciones = NodoAST("INSTRUCCIONES")
        for instr in self.instrucciones:
            instrucciones.agregarHijoNodo(instr.getNodo())
        nodo.agregarHijoNodo(instrucciones)
        return nodo
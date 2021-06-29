from Interprete.Abstract.Instruccion import Instruccion
from Interprete.Instrucciones.IncrementoDecremento import IncrementoDecremento
from Interprete.TS.Exception import Exception
from Interprete.TS.Tipo import Tipo
from Interprete.TS.TablaSimbolo import TablaSimbolo
from Interprete.Instrucciones.Break import Break
from Interprete.Instrucciones.Return import Return
from Interprete.Instrucciones.Continue import Continue
from Interprete.Abstract.NodoAST import NodoAST

class While(Instruccion):
    def __init__(self, condicion, instrucciones, fila, columna):
        self.condicion = condicion
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        while True:
            condicion = self.condicion.interpretar(tree, table)
            if isinstance(condicion, Exception): return condicion
            
            if self.condicion.tipo == Tipo.BOOLEANO: # Aqui verifica si la condicion es una expresion logica, sino lanza una Exception.
                if bool(condicion) == True:                 
                    nuevaTabla = TablaSimbolo(table)        # Inicia el Nuevo Ambito.

                    for instruccion in self.instrucciones:  # Inicia ejecutando las instrucciones adentro del While.
                        result = instruccion.interpretar(tree, nuevaTabla) 
                        if isinstance(result, Exception):
                            tree.get_excepcion().append(result)
                            tree.update_consola(result.__str__())
                        if isinstance(result, Break): return None
                        if isinstance(result, Return): return result
                        if isinstance(result, Continue): break
                else:
                    break
            else:
                return Exception("Semantico", "Tipo de dato no booleano en While.", self.fila, self.columna)

    def getNodo(self):
        nodo = NodoAST("WHILE")
        nodo.agregarHijoNodo(self.condicion.getNodo())
        instrucciones = NodoAST("INSTRUCCIONES")
        for instr in self.instrucciones:
            instrucciones.agregarHijoNodo(instr.getNodo())
        nodo.agregarHijoNodo(instrucciones)
        
        return nodo
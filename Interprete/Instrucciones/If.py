from Interprete.Abstract.Instruccion import Instruccion
from Interprete.TS.Exception import Exception
from Interprete.TS.Tipo import Tipo
from Interprete.TS.TablaSimbolo import TablaSimbolo
from Interprete.Instrucciones.Break import Break
from Interprete.Instrucciones.Return import Return
from Interprete.Instrucciones.Continue import Continue
from Interprete.Abstract.NodoAST import NodoAST


class If(Instruccion):
    def __init__(self, condicion, instruccionesIf, instruccionesElse, ElseIf, fila, columna):
        self.condicion = condicion
        self.instruccionesIf = instruccionesIf
        self.instruccionesElse = instruccionesElse
        self.elseIf = ElseIf
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):

        condicion = self.condicion.interpretar(tree, table)
        if isinstance(condicion, Exception): return condicion

        if self.condicion.tipo == Tipo.BOOLEANO: # Aqui verifica si la condicion es una expresion logica, sino lanza una Exception.

            if bool(condicion) == True:   # Verifica que cummpla esta condicion, si no pasa al else if o al else.
                nuevaTabla = TablaSimbolo(table)       # Se inicia con el primer Ambito.
                for instruccion in self.instruccionesIf:
                    result = instruccion.interpretar(tree, nuevaTabla) # Inicia ejecutando las instrucciones adentro del If.
                    if isinstance(result, Exception):
                        tree.get_excepcion().append(result)
                        tree.update_consola(result.__str__())
                    if isinstance(result, Break): return result
                    if isinstance(result, Return): return result
                    if isinstance(result, Continue): return result

            else: # Aqui busca si la condicion es un else if o un else.

                if self.instruccionesElse != None: # Aqui se ejecuta las instrucciones del else.
                    nuevaTabla = TablaSimbolo(table)       # Se creal el nuevo Ambito.
                    for instruccion in self.instruccionesElse:  # Inicia ejecutando las instrucciones adentro del else.
                        result = instruccion.interpretar(tree, nuevaTabla) 
                        if isinstance(result, Exception) :
                            tree.get_excepcion().append(result)
                            tree.update_consola(result.__str__()) 
                        if isinstance(result, Break): return result
                        if isinstance(result, Return): return result
                        if isinstance(result, Continue): return result

                elif self.elseIf != None:   # Aqui se ejecuta las instrucciones del else if.
                    result = self.elseIf.interpretar(tree, table) 
                    if isinstance(result, Exception): return result
                    if isinstance(result, Break): return result
                    if isinstance(result, Return): return result
                    if isinstance(result, Continue): return result

        else:
            return Exception("Semantico", "Tipo de dato no booleano en IF.", self.fila, self.columna)

    def getNodo(self):
        nodo = NodoAST("IF")
        nodo.agregarHijoNodo(self.condicion.getNodo())
        instruccionesIf = NodoAST("INSTRUCCIONES IF")
        for instr in self.instruccionesIf:
            instruccionesIf.agregarHijoNodo(instr.getNodo())
        nodo.agregarHijoNodo(instruccionesIf)

        if self.instruccionesElse != None:
            instruccionesElse = NodoAST("INSTRUCCIONES ELSE")
            for instr in self.instruccionesElse:
                instruccionesElse.agregarHijoNodo(instr.getNodo())
            nodo.agregarHijoNodo(instruccionesElse) 
        elif self.elseIf != None:
            nodo.agregarHijoNodo(self.elseIf.getNodo())

        return nodo
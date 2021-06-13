from Interprete.Abstract.Instruccion import Instruccion
from Interprete.TS.Exception import Exception
from Interprete.TS.Tipo import Tipo
from Interprete.TS.TablaSimbolo import TablaSimbolo
from Interprete.Instrucciones.Break import Break


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

        if self.condicion.tipo == Tipo.BOOLEANO:
            if bool(condicion) == True:   # VERIFICA SI ES VERDADERA LA CONDICION
                nuevaTabla = TablaSimbolo(table)       #NUEVO ENTORNO
                for instruccion in self.instruccionesIf:
                    result = instruccion.interpretar(tree, nuevaTabla) #EJECUTA INSTRUCCION ADENTRO DEL IF
                    if isinstance(result, Exception):
                        tree.get_excepcion().append(result)
                        tree.update_consola(result.__str__())
                    if isinstance(result, Break): return result
            else: # AQUI SI LA CONDICION NO CUMPLE.
                if self.instruccionesElse != None:
                    nuevaTabla = TablaSimbolo(table)       #NUEVO ENTORNO
                    for instruccion in self.instruccionesElse:
                        result = instruccion.interpretar(tree, nuevaTabla) #EJECUTA INSTRUCCION ADENTRO DEL IF
                        if isinstance(result, Exception) :
                            tree.get_excepcion().append(result)
                            tree.update_consola(result.__str__()) 
                        if isinstance(result, Break): return result
                elif self.elseIf != None:
                    result = self.elseIf.interpretar(tree, table)
                    if isinstance(result, Exception): return result
                    if isinstance(result, Break): return result

        else:
            return Exception("Semantico", "Tipo de dato no booleano en IF.", self.fila, self.columna)
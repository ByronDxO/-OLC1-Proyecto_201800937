from Interprete.Abstract.Instruccion import Instruccion
from Interprete.Instrucciones.IncrementoDecremento import IncrementoDecremento
from Interprete.TS.Exception import Exception
from Interprete.TS.Tipo import Tipo
from Interprete.TS.TablaSimbolo import TablaSimbolo
from Interprete.Instrucciones.Break import Break

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
            
            if self.condicion.tipo == Tipo.BOOLEANO:
                if bool(condicion) == True:   # VERIFICA SI ES VERDADERA LA CONDICION
                    nuevaTabla = TablaSimbolo(table)       #NUEVO ENTORNO

                    for instruccion in self.instrucciones:
                        result = instruccion.interpretar(tree, nuevaTabla) #EJECUTA INSTRUCCION ADENTRO DEL IF
                        if isinstance(result, Exception):
                            tree.get_excepcion().append(result)
                            tree.update_consola(result.__str__())
                        if isinstance(result, Break): return None
                else:
                    break
            else:
                return Exception("Semantico", "Tipo de dato no booleano en IF.", self.fila, self.columna)
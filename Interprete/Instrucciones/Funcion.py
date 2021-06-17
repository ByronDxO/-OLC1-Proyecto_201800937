from Interprete.Abstract.Instruccion import Instruccion
from Interprete.TS.Exception import Exception
from Interprete.TS.TablaSimbolo import TablaSimbolo
from Interprete.Instrucciones.Break import Break


class Funcion(Instruccion):
    def __init__(self, nombre, instrucciones, fila, columna):
        self.nombre = nombre.lower()
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna
        self.tipo = None
    
    def interpretar(self, tree, table):
        nuevaTabla = TablaSimbolo(table) 
        for instruccion in self.instrucciones:      # REALIZAR LAS ACCIONES
            value = instruccion.interpretar(tree, nuevaTabla)
            if isinstance(value, Exception):
                tree.get_excepcion().append(value)
                tree.update_consola(value.__str__())
            if isinstance(value, Break): 
                err = Exception("Semantico", "Sentencia Break fuera de ciclo", instruccion.fila, instruccion.columna)
                tree.get_excepcion().append(err)
                tree.update_consola(err.__str__())
        return None
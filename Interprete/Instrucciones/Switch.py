from Interprete.Expresiones.Identificador import Identificador
from Interprete.Instrucciones.Case import Case
from Interprete.Instrucciones.IncrementoDecremento import IncrementoDecremento
from Interprete.Instrucciones.Declaracion import Declaracion
from Interprete.Instrucciones.Asignacion import Asignacion
from Interprete.Abstract.Instruccion import Instruccion
from Interprete.TS.Exception import Exception
from Interprete.TS.Tipo import Tipo
from Interprete.TS.TablaSimbolo import TablaSimbolo
from Interprete.Instrucciones.Break import Break

class Switch(Instruccion):
    def __init__(self, condicion, caso_instrucciones, default_instrucciones, fila, columna):
        self.condicion = condicion
        self.caso_instrucciones = caso_instrucciones
        self.default_instrucciones = default_instrucciones
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):

        condicion = self.condicion.interpretar(tree, table) 
        if isinstance(condicion, Exception): return condicion
        
        if self.caso_instrucciones != None and self.default_instrucciones != None:      # Condicion 1 => [<CASES_LIST>] [<DEFAULT>]
            
            nuevaTabla = TablaSimbolo(table)
            for instrucciones in self.caso_instrucciones:

                result = instrucciones.interpretar(tree, nuevaTabla)
                if isinstance(result, Exception): 
                    tree.get_excepcion().append(result)
                    tree.update_consola(result.__str__())
                
                if (condicion == result):
                    for instruccion in instrucciones.get_instrucciones_case():
                        value = instruccion.interpretar(tree, nuevaTabla)
                        if isinstance(value, Exception):     
                            tree.get_excepcion().append(value)
                            tree.update_consola(value.__str__())
                        if isinstance(value, Break): return None

            
            for instrucciones in self.default_instrucciones.get_instrucciones_default():

                result = instrucciones.interpretar(tree, nuevaTabla)
                if isinstance(result, Exception): 
                    tree.get_excepcion().append(result)
                    tree.update_consola(result.__str__())
                if isinstance(value, Break): return None

            
                
        elif self.caso_instrucciones != None and self.default_instrucciones == None:    # Condicion 2 => [<CASES_LIST>] 

            nuevaTabla = TablaSimbolo(table)
            for instrucciones in self.caso_instrucciones:

                result = instrucciones.interpretar(tree, nuevaTabla)
                if isinstance(result, Exception): 
                    tree.get_excepcion().append(result)
                    tree.update_consola(result.__str__())
                
                if (condicion == result):
                    for instruccion in instrucciones.get_instrucciones_case():
                        value = instruccion.interpretar(tree, nuevaTabla)
                        if isinstance(value, Exception):     
                            tree.get_excepcion().append(value)
                            tree.update_consola(value.__str__())
                        if isinstance(value, Break): return None
            
            
        elif self.caso_instrucciones == None and self.default_instrucciones != None:    # Condicion 3 => [<DEFAULT>]
            nuevaTabla = TablaSimbolo(table)

            for instrucciones in self.default_instrucciones.get_instrucciones_default():

                result = instrucciones.interpretar(tree, nuevaTabla)
                if isinstance(result, Exception): 
                    tree.get_excepcion().append(result)
                    tree.update_consola(result.__str__())
                if isinstance(result, Break): return None

        
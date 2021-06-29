from Interprete.Abstract.Instruccion import Instruccion
from Interprete.TS.Tipo import Tipo
from Interprete.TS.Exception import Exception
from Interprete.TS.TablaSimbolo import TablaSimbolo
from Interprete.Instrucciones.Break import Break
from Interprete.Instrucciones.Return import Return
from Interprete.Instrucciones.Continue import Continue
from Interprete.Abstract.NodoAST import NodoAST

class Funcion(Instruccion):
    def __init__(self, nombre, parametros, instrucciones, fila, columna):
        self.nombre = nombre.lower()
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna
        self.tipo = Tipo.NULO
    
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
            if isinstance(value, Continue): 
                err = Exception("Semantico", "Sentencia Continue fuera de ciclo", instruccion.fila, instruccion.columna)
                tree.get_excepcion().append(err)
                tree.update_consola(err.__str__())

            if isinstance(value, Return):
                self.tipo = value.tipo
                return value.result
        return None

    def getNodo(self):
        nodo = NodoAST("FUNCION")

        nodo.agregarHijo(str(self.nombre))

        parametros = NodoAST("PARAMETROS")
        for param in self.parametros:
            parametro = NodoAST("PARAMETRO")
            parametro.agregarHijo(param["tipoDato"])
            parametro.agregarHijo(param["identificador"])
            parametros.agregarHijoNodo(parametro)
        nodo.agregarHijoNodo(parametros)

        instrucciones = NodoAST("INSTRUCCIONES")
        for instruccion in self.instrucciones:
            instrucciones.agregarHijoNodo(instruccion.getNodo())
        nodo.agregarHijoNodo(instrucciones)
        
        return nodo
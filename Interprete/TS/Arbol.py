'''
    AST   -> Abstract Syntax Tree, almacena nodos.
    Nodos -> Los nodos del AST siven para realizar todas las instrucciones, funciones, operaciones, entre otros, por medio del interprete.
    Instruccion -> Sera una clase abstracta
'''
from tkinter import *
class Arbol():
    
    def __init__(self, instruccion):
        self.instruccion = instruccion
        self.funciones = []
        self.excepcion = []
        self.consola = ""
        self.tabla_ts_global = None
        self.consolaSalida = None
        self.dot = ""
        self.contador = 0

    def get_instruccion(self):
        return self.instruccion

    def set_instruccion(self, instruccion):
        self.instruccion = instruccion

    def get_funciones(self):
        return self.funciones

    def getFuncion(self, nombre):
        for funcion in self.funciones:
            if funcion.nombre == nombre:
                return funcion
        return None

    def get_excepcion(self):
        return self.excepcion

    def set_excepcion(self, excepcion):
        self.excepcion = excepcion

    def get_consola(self):
        return self.consola
    
    def set_consola(self, consola):
        self.consola = consola

    def update_consola(self, cadena):
        self.consola += str(cadena) + '\n'

    def get_tabla_ts_global(self):
        return self.tabla_ts_global

    def set_tabla_ts_global(self, ts_global):
        self.tabla_ts_global = ts_global

    def addFuncion(self, funcion):
        self.funciones.append(funcion)
        
    # se implento para que en el read se actualice la consola.
    def getConsolaSalida(self):
        return self.consolaSalida
        
    def setConsolaSalida(self, consola):
        self.consolaSalida = consola

    def showConsolaSalida(self, consola):
        self.consolaSalida.delete("1.0","end")
        self.consolaSalida.insert(INSERT, consola)

    # GENERA EL AST
    def getDot(self, raiz): ## DEVUELVE EL STRING DE LA GRAFICA EN GRAPHVIZ
        self.dot = ""
        self.dot += "digraph {\n"
        self.dot += "n0[label=\"" + raiz.getValor().replace("\"", "\\\"") + "\"];\n"
        self.contador = 1
        self.recorrerAST("n0", raiz)
        self.dot += "}"
        return self.dot

    def recorrerAST(self, idPadre, nodoPadre):
        for hijo in nodoPadre.getHijos():
            nombreHijo = "n" + str(self.contador)
            self.dot += nombreHijo + "[label=\"" + hijo.getValor().replace("\"", "\\\"") + "\"];\n"
            self.dot += idPadre + "->" + nombreHijo + ";\n"
            self.contador += 1
            self.recorrerAST(nombreHijo, hijo)


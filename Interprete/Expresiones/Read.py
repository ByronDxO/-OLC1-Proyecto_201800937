from Interprete.Abstract.Instruccion import Instruccion
from Interprete.TS.Tipo import Tipo


from tkinter import *
from tkinter import Tk, simpledialog
import tkinter as tk
import sys

class Read(Instruccion):
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna
        self.tipo = Tipo.CADENA

    def interpretar(self, tree, table):
        print(tree.get_consola()) #IMPRIME LA CONSOLA
        # print("Ingreso a un READ. Ingrese el valor\r")
        
        tree.showConsolaSalida(tree.get_consola())
        lectura = simpledialog.askstring("Read()", "ingrese dato", parent=tree.getConsolaSalida())
        
        return lectura
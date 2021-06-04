'''
    DOCUMENTACION -> https://likegeeks.com/es/ejemplos-de-la-gui-de-python/
    DOCUMENTACION -> https://guia-tkinter.readthedocs.io/es/develop/chapters/6-widgets/6.1-Intro.html
    DOCUMENTACION -> https://python-intermedio.readthedocs.io/es/latest/args_and_kwargs.html
'''

from tkinter import ttk, Tk, Label, Menu, Button, Entry, StringVar, Scrollbar, Frame, Text, scrolledtext
import tkinter as tk
from tkinter import *

class Ventana():

    def __init__(self):
        
        self.root_window = Tk()
        
        self.scrollbar = Scrollbar(self.root_window)
        self.scrollbar.pack( side = RIGHT, fill = Y )
        
        self.root_window.geometry("1350x670+0+0")
        self.root_window.title("Ventana Principal")
        
        # ------------------------------------ BARRA MENU ------------------------------------ 
        self.barra_menu = Menu(self.root_window)
        
        # ------------------------------------ CARGAR ARCHIVO ------------------------------------ 
        self.open_file = Menu(self.barra_menu)
        self.open_file.add_command(label="Cargar Archivo")
        self.open_file.add_command(label="Abrir Archivo")
        self.open_file.add_command(label="Guardar")
        self.open_file.add_command(label="Guardar Como")


        self.barra_menu.add_cascade(label="Archivo", menu=self.open_file)

        # ------------------------------------ EDICION ------------------------------------ 
        self.edicion = Menu(self.barra_menu)
        self.edicion.add_command(label="opcion 1")


        self.barra_menu.add_cascade(label="Edicion", menu=self.edicion)
        # ------------------------------------ HERRAMIENTAS ------------------------------------ 
        self.herramienta = Menu(self.barra_menu)
        self.herramienta.add_command(label="opcion 1")


        self.barra_menu.add_cascade(label="Herramientas", menu=self.herramienta)
        # ------------------------------------ ANALIZAR ------------------------------------ 
        self.analizar = Menu(self.barra_menu)
        self.analizar.add_command(label="opcion 1")


        self.barra_menu.add_cascade(label="Analizar", menu=self.analizar)
        # ------------------------------------ REPORTES ------------------------------------ 
        self.reporte = Menu(self.barra_menu)
        self.reporte.add_command(label="opcion 1")


        self.barra_menu.add_cascade(label="Reporte", menu=self.reporte)

        # ------------------------------------ AYUDA ------------------------------------ 
        self.ayuda = Menu(self.barra_menu)
        self.ayuda.add_command(label="opcion 1")


        self.barra_menu.add_cascade(label="Reporte", menu=self.ayuda)

        # ----------------------------------- FUNCIONALIDAD ---------------------------------------

        self.editor = Label(self.root_window, text="Editor")
        self.editor.pack()
        self.editor.place(x=1, y=1)

        
        self.scroll_consola = scrolledtext.ScrolledText(self.root_window, height=20, width=70)
        self.scroll_consola.pack()
        self.scroll_consola.place(x=700, y=25)
        
        
        # ------------------------------------ FIN DE TK -------------------------------------------


        self.scroll = ScrollText(self.root_window)
        #self.scroll.insert(ttk.END, "HEY" + 20*'\n')
        self.scroll.pack()
        self.scroll.place(x=50, y=25)
        self.scroll.text.focus()
        self.root_window.after(200, self.scroll.redraw())
        self.root_window.config(menu=self.barra_menu)
        self.root_window.mainloop()



class ScrollText(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        # bg -> color de fondo --- foreground -> color al texto --- selectbrackgroud -> color a lo que seleccione --- inserbackgroud -> color al puntero
        self.text = tk.Text(self, bg='#FFFFFF', foreground="#000000", selectbackground="#C8C8C8", insertbackground='#000000',  height=20, width=70)

        self.scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.text.yview)
        self.text.configure(yscrollcommand=self.scrollbar.set)

        self.numero_lineas = TextLineNumbers(self, width=35, bg='#D5D5D5')
        self.numero_lineas.attach(self.text)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.numero_lineas.pack(side=tk.LEFT, fill=tk.Y, padx=(5, 0))
        self.text.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.text.bind("<Key>", self.onPressDelay)
        self.text.bind("<Button-1>", self.numero_lineas.redraw)
        self.scrollbar.bind("<Button-1>", self.onScrollPress)
        self.text.bind("<MouseWheel>", self.onPressDelay)

    def onScrollPress(self, *args):
        self.scrollbar.bind("<B1-Motion>", self.numero_lineas.redraw)

    def onScrollRelease(self, *args):
        self.scrollbar.unbind("<B1-Motion>", self.numero_lineas.redraw)

    def onPressDelay(self, *args):
        self.after(2, self.numero_lineas.redraw)

    def get(self, *args, **kwargs):
        return self.text.get(*args, **kwargs)

    def insert(self, *args, **kwargs):
        return self.text.insert(*args, **kwargs)

    def delete(self, *args, **kwargs):
        return self.text.delete(*args, **kwargs)

    def index(self, *args, **kwargs):
        return self.text.index(*args, **kwargs)

    def redraw(self):
        self.numero_lineas.redraw()

class TextLineNumbers(tk.Canvas):
    def __init__(self, *args, **kwargs):
        tk.Canvas.__init__(self, *args, **kwargs, highlightthickness=0)
        self.textwidget = None

    def attach(self, text_widget):
        self.textwidget = text_widget

    def redraw(self, *args):
        '''redraw line numbers'''
        self.delete("all")

        i = self.textwidget.index("@0,0")
        while True :
            dline= self.textwidget.dlineinfo(i)
            if dline is None: break
            y = dline[1]
            linenum = str(i).split(".")[0]
            self.create_text(2, y, anchor="nw", text=linenum, fill="#606366")
            i = self.textwidget.index("%s+1line" % i)

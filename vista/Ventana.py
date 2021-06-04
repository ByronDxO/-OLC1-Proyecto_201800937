from tkinter import ttk, Tk, Label, Menu, Button, Entry, StringVar, Scrollbar, Frame

class Ventana():

    def __init__(self):
        
        self.root_window = Tk()
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

        # ------------------------------------ FIN DE TK -------------------------------------------
        self.root_window.config(menu=self.barra_menu)
        self.root_window.mainloop()



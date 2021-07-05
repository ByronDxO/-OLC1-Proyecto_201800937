'''
    DOCUMENTACION -> https://likegeeks.com/es/ejemplos-de-la-gui-de-python/
    DOCUMENTACION -> https://guia-tkinter.readthedocs.io/es/develop/chapters/6-widgets/6.1-Intro.html
    DOCUMENTACION -> https://python-intermedio.readthedocs.io/es/latest/args_and_kwargs.html
'''

from tkinter import ttk, Tk, Label, Menu, Button, Entry, StringVar, Scrollbar, Frame, Text, scrolledtext
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import tkinter.font as tkFont
import webbrowser as wb


class Ventana():

    def __init__(self):
        self.text_global = ""
        self.filename = ""
        
        self.root_window = Tk()
        self.root_window.configure(bg='#000000')
        
        self.root_window.geometry("1350x670+0+0")
        self.root_window.title("Ventana Principal")
        
        # ------------------------------------ BARRA MENU ------------------------------------ 
        self.barra_menu = Menu(self.root_window)
        
        # ------------------------------------ CARGAR ARCHIVO ------------------------------------ 
        self.open_file = Menu(self.barra_menu, bg='#000000', foreground="#ffffff")
        self.open_file.add_command(label="Crear Archivo", command=lambda: self.crear_archivo())
        self.open_file.add_command(label="Abrir Archivo", command=lambda: self.abrir_archivo())
        self.open_file.add_command(label="Guardar", command=lambda: self.guardar())
        self.open_file.add_command(label="Guardar Como", command=lambda: self.guardar_como())


        self.barra_menu.add_cascade(label="Archivo", menu=self.open_file)
        # ------------------------------------ HERRAMIENTAS ------------------------------------ 
        self.herramienta = Menu(self.barra_menu, bg='#000000', foreground="#ffffff")
        self.herramienta.add_command(label="Interpretar", command=self.interpretar)
        self.herramienta.add_command(label="Debugger")


        self.barra_menu.add_cascade(label="Herramientas", menu=self.herramienta)
        # ------------------------------------ REPORTES ------------------------------------ 
        self.reporte = Menu(self.barra_menu, bg='#000000', foreground="#ffffff")
        self.reporte.add_command(label="Reporte de Errores")
        self.reporte.add_command(label="Generar Árbol AST (Árbol de Análisis Sintáctico)", command=lambda:self.reporte_ast())
        self.reporte.add_command(label="Reporte de Tabla de Símbolos")


        self.barra_menu.add_cascade(label="Reporte", menu=self.reporte)

        # ------------------------------------ AYUDA ------------------------------------ 
        self.ayuda = Menu(self.barra_menu, bg='#000000', foreground="#ffffff")
        self.ayuda.add_command(label="opcion 1")


        self.barra_menu.add_cascade(label="Reporte", menu=self.ayuda)

        # ----------------------------------- CONSOLA Y PARTE DE CODIGO ---------------------------------------

        self.editor = Label(self.root_window, text="Editor", bg='#000000', foreground="#ffffff")
        self.editor.pack()
        self.editor.place(x=20, y=1)

        self.label_position = Label(self.root_window, bg='#000000', foreground="#ffffff")
        self.label_position.pack()
        self.label_position.place(x=55, y=1)

        self.scroll = ScrollText(self.root_window, bg='#000000') # aqui va el codigo fuente
        self.scroll.pack()
        self.scroll.place(x=10, y=25)
        #self.scroll.text.focus()
        #self.root_window.after(200, self.scroll.redraw())

        
        self.fontStyle = tkFont.Font(family="Courier New",size=8)
        self.scroll_consola = scrolledtext.ScrolledText(self.root_window, height=23, width=80, font=self.fontStyle, bg='#000000', foreground="#ffffff") # consola
        #self.scroll_consola.configure(state='disabled')
        self.scroll_consola.pack()
        self.scroll_consola.place(x=750, y=25)


        # -----------------------  PARTE DE REPORTES Y TABLA DE SIMBOLOS ---------------------------


        self.root_tab_control = ttk.Notebook(self.root_window, height=210, width=1250) # Creando la raiz de las petañas
        

        self.root_tab1 = tk.Frame(self.root_tab_control, bg='#000000') # Creando la pestaña
        self.root_tab1.pack()
        # self.root_tab1.config(bg='#000000') 
        self.root_tab_control.add(self.root_tab1, text="Tabla de Simbolos")

        self.root_tab2 = tk.Frame(self.root_tab_control, bg='#000000') # Creeando otra pestaña
        self.root_tab2.pack()
        self.root_tab_control.add(self.root_tab2, text="Reporte de Errores")
        

        self.lb1 = Label(self.root_tab1, text="Tabla de Simbolos", bg='#000000', foreground="#ffffff")
        self.lb1.pack()
        self.lb2 = Label(self.root_tab2, text="Tabla de Reportes", bg='#000000', foreground="#ffffff")
        self.lb2.pack()

        self.root_tab_control.pack(expand=1, fill="both")
        self.root_tab_control.place(x=50, y=400)

        #TABLA SIMBOLOS
        self.table = ttk.Treeview(self.root_tab1)
        self.table['columns'] = ('NO', 'ID', 'TIPO', 'DIMENSION', 'VALOR', 'AMBITO', 'REFERENCIAS')
        self.table.column('#0', width=0, stretch=NO)
        self.table.column('NO', anchor=CENTER, width=3)
        self.table.column('ID', anchor=CENTER)
        self.table.column('TIPO', anchor=CENTER)
        self.table.column('DIMENSION', anchor=CENTER)
        self.table.column('VALOR', anchor=CENTER)
        self.table.column('AMBITO', anchor=CENTER)
        self.table.column('REFERENCIAS', anchor=CENTER)

        self.table.heading('#0', text='', anchor=CENTER)
        self.table.heading('NO', text='#', anchor=CENTER)
        self.table.heading('ID', text='Id', anchor=CENTER)
        self.table.heading('TIPO', text='Tipo', anchor=CENTER)
        self.table.heading('DIMENSION', text='Dimension', anchor=CENTER)
        self.table.heading('VALOR', text='Valor', anchor=CENTER)
        self.table.heading('AMBITO', text='Ambito', anchor=CENTER)
        self.table.heading('REFERENCIAS', text='Referencias', anchor=CENTER)
        """
        i = 0
        while i < 10:
            self.table.insert(parent='', index=i, iid=i, text='', values=(f'{i+1}', f'id{i}',f'tipo{i}',f'dime{i}',f'val{i}',f'amb{i}',f'refe{i}'))
            i += 1
        """
        # self.table.tag_configure("gray", background="gray")
        self.table.pack()

        # TABLA DE ERRORES
        self.table_error = ttk.Treeview(self.root_tab2)
        self.table_error['columns'] = ('NO', 'TIPO', 'DESCRIPCION', 'LINEA', 'COLUMNA')
        self.table_error.column('#0', width=0, stretch=NO)
        self.table_error.column('NO', anchor=CENTER, width=3)
        self.table_error.column('TIPO', anchor=CENTER)
        self.table_error.column('DESCRIPCION', anchor=CENTER)
        self.table_error.column('LINEA', anchor=CENTER)
        self.table_error.column('COLUMNA', anchor=CENTER)

        self.table_error.heading('#0', text='', anchor=CENTER)
        self.table_error.heading('NO', text='#', anchor=CENTER)
        self.table_error.heading('TIPO', text='Tipo', anchor=CENTER)
        self.table_error.heading('DESCRIPCION', text='Dimension', anchor=CENTER)
        self.table_error.heading('LINEA', text='Fila', anchor=CENTER)
        self.table_error.heading('COLUMNA', text='Columna', anchor=CENTER)
        
        self.table_error.pack() 
        # ----------------------------------- POSICION DEL MOUSE Y COLORES----------------------------------
               
        self.scroll.text.bind("<Button-1>", self.get_posicion_mouse)
        self.scroll.text.bind("<Button-2>", self.get_posicion_mouse)
        self.scroll.text.bind("<Button-3>", self.get_posicion_mouse)


        self.scroll.text.tag_config('tk_reseverda',     foreground='#0317D8')      # Palabras reservadas   - Azul
        self.scroll.text.tag_config('tk_cadena',        foreground='#ff860d')      # Cadenas o caracteres  - Anaranjado
        self.scroll.text.tag_config('tk_numero',        foreground='#a33aff')      # Numeros               - Morado
        self.scroll.text.tag_config('tk_comentario',    foreground='#646464')      # Comentario            - Gris
        self.scroll.text.tag_config('tk_id',            foreground='#45f50d')      # id                    - Verde Claro
        self.scroll.text.tag_config('tk_otro',          foreground='#ffffff')      # Otros                 - Negro        

        



        # ------------------------------------ FIN DE TK -------------------------------------------
       
        self.root_window.config(menu=self.barra_menu)
        self.root_window.mainloop()

    # ----------------------------------- POSICION -----------------------------------

    def get_posicion_mouse(self, *args, **kwargs):
        position = self.scroll.text.index(INSERT)
        self.label_position.destroy()
        self.label_position = Label(self.root_window, text=f"{position}", bg='#000000', foreground="#ffffff")
        self.label_position.pack()
        self.label_position.place(x=55, y=1)
    

        

    # -------------------------------------------------------- ARCHIVO ------------------------------------------------------

    def crear_archivo(self):
        print('\n---------------')
        result=self.scroll.text.get(1.0, tk.END+"-1c")
        print(result)
        print('---------------')

        self.filename = filedialog.asksaveasfilename(initialdir = "/",title = "Guardar como",filetypes = (("txt files","*.jpr"),("todos los archivos","*.*")))
        
        if self.filname!='':
            archi1=open(self.filename, "w")
            archi1.write(result)
            archi1.close()



    def abrir_archivo(self):
        try:
            ruta =  ""
            self.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("JPR files","*.jpr"),("all files","*.*")))
            ruta = self.filename
            if ruta != "":
                try:
                    archivo = open(ruta, "r", encoding='utf-8')
                    texto = archivo.read()

                    self.scroll.text.delete("1.0","end")
                    for array in self.set_paint(texto):
                        self.scroll.text.insert(INSERT, array[1], array[0])
                    archivo.close()
                except (FileNotFoundError):
                    print("Error")
            else:
                return None

        except IndexError as e:
            print(e)  

    def guardar(self):
        
        if self.filename != "":
            result=self.scroll.text.get(1.0, tk.END+"-1c")
            archivo = open(self.filename, "w")
            archivo.write(result)
            archivo.close()
        else:
            messagebox.showinfo(message="No hay Documento abierto", title="Gaurdar")

    def guardar_como(self):

        self.filename = filedialog.asksaveasfilename(initialdir = "/", title = "Seleccione el Archivo", defaultextension=".jpr", filetypes = (("jpr files","*.jpr"),("all files","*.*")))
        result = self.scroll.text.get(1.0, tk.END+"-1c")

        if self.filename!='':
            archi1=open(self.filename, "w")
            archi1.write(result)
            archi1.close()

    # -------------------------------------------------------- PINTAR ------------------------------------------------------
    def set_paint(self, texto):
        global_lista = []
        temp = ''
        
        i = 0
        while i < len(texto):

            if (re.search(r'[0-9]', texto[i])): # Aqui si el valor es solo un numero.
                temp += texto[i] # Esto hace que se concatene el temp con el texto.
                i = i + 1

                while (i != len(texto)):
                    if (re.search(r'[0-9]', texto[i])):
                        temp += texto[i]
                        i = i + 1

                    elif (texto[i] == '.'):
                        temp += texto[i]
                        i = i + 1

                    if (not texto[i].isnumeric()) and (texto[i] != '.'):
                        auxiliar_lista = ["tk_numero", temp]
                        global_lista.append(auxiliar_lista)
                        temp = ''
                        i = i - 1
                        break

                if (len(temp) != 0):
                    auxiliar_lista = ['tk_numero', temp]
                    global_lista.append(auxiliar_lista)
                    temp = ''
            
            elif (re.search(r'[a-zA-Z0-9_]', texto[i])): # Si el valor es una variable..
                temp += texto[i]
                i = i + 1

                while (i != len(texto)):
                    if (i + 1 != len(texto)):
                        if not (re.search(r'[a-zA-Z0-9_]', texto[i + 1])):
                            temp += texto[i]
                            auxiliar_lista = ['tk_id', temp]
                            global_lista.append(auxiliar_lista)
                            temp = ''
                            break

                    temp += texto[i]
                    i = i + 1

                if (len(temp) != 0):
                    auxiliar_lista = ['tk_id', temp]
                    global_lista.append(auxiliar_lista)
                    temp = ''

            elif (texto[i] == '\"'):    # Aqui si el valor es unicamente una cadena - String.
                temp += texto[i]  
                i = i + 1               # Se incremente para que pase despues del ""

                while (i != len(texto)):
                    if (re.search(r'''\"(\\"|\\'|\\\\|\\n|\\t|\\r|[^\\\'\"])*?\"''', temp) and (i <= (len(texto)) - 1)): # Obtiene lo que esta adentro de - " String "
                        auxiliar_lista = ['tk_cadena', temp]
                        global_lista.append(auxiliar_lista)
                        temp = ''
                        i = i - 1
                        break

                    temp += texto[i]
                    i = i + 1

                if (len(temp) != 0):
                    auxiliar_lista = ['tk_cadena', temp]
                    global_lista.append(auxiliar_lista)
                    temp = ''

            elif (texto[i] == '\''): # Aqui si el valor es unicamente una caracter- Char.
                temp += texto[i]  
                i = i + 1

                while (i != len(texto)):
                    if (re.search(r'''\'(\\'|\\\\|\\n|\\t|\\r|\\"|.)?\'''', temp) and (i <= (len(texto)) - 1)): # Obtiene lo que esta adentro de - ' char '

                        auxiliar_lista = ["tk_cadena", temp]
                        global_lista.append(auxiliar_lista)
                        temp = ""
                        i = i - 1
                        break

                    temp += texto[i]
                    i = i + 1
                if (len(temp) != 0):
                    auxiliar_lista = ['tk_cadena', temp]
                    global_lista.append(auxiliar_lista)
                    temp = ''

            
            elif (texto[i] == '#'): # Aqui si el valor es un comentario
                temp += texto[i]  # concateno de nuevo al val para la cadena
                i = i + 1
                if (texto[i] == '*'):  # Entonces buscara un multilinea
                    while (i != len(texto)):
                        if (texto[i] == '*' and (i <= len(texto) - 1)):
                            temp += texto[i]
                            i = i + 1
                            temp += texto[i]

                            # if (re.search(r'#*\*(.|\n)*?\*#', temp)): # Obtiene todo lo que esta adentro del comentario - # Comentario #
                            if (re.search(r'\#\*(.|\n)*?\*\#', temp)): # Obtiene todo lo que esta adentro del comentario - # Comentario #
                                auxiliar_lista = ['tk_comentario', temp]
                                global_lista.append(auxiliar_lista)
                                temp = ""
                                break

                        temp += texto[i]
                        i = i + 1
                else:
                    while (i != len(texto)):
                        if (texto[i] == '\n' and (i <= len(texto) - 1)):
                            temp += texto[i]
                            if (re.search(r'#.*\n', temp)):
                                auxiliar_lista = ['tk_comentario', temp]
                                global_lista.append(auxiliar_lista)
                                temp = ""
                                break

                        temp += texto[i]
                        i = i + 1

                if (len(temp) != 0):
                    auxiliar_lista = ['tk_comentario', temp]
                    global_lista.append(auxiliar_lista)
                    temp = ""

            else:
                # Validar la concatenacion
                if (len(temp) != 0):
                    auxiliar_lista = ['tk_otro', temp]
                    global_lista.append(auxiliar_lista)
                # En este momento se ha encontrado con algun otro signo
                auxiliar_lista = ['tk_otro', texto[i]]
                global_lista.append(auxiliar_lista)
                temp = ''
            i = i + 1

        # Se revisa en la lista de reservadas
        for tokens_reservadas in global_lista:
            if  (tokens_reservadas[1].lower() == "print")      or \
                (tokens_reservadas[1].lower() == "var")        or \
                (tokens_reservadas[1].lower() == "true")       or \
                (tokens_reservadas[1].lower() == "false")      or \
                (tokens_reservadas[1].lower() == "if")         or \
                (tokens_reservadas[1].lower() == "else")       or \
                (tokens_reservadas[1].lower() == "while")      or \
                (tokens_reservadas[1].lower() == "break")      or \
                (tokens_reservadas[1].lower() == "main")       or \
                (tokens_reservadas[1].lower() == "func")       or \
                (tokens_reservadas[1].lower() == "for")        or \
                (tokens_reservadas[1].lower() == "switch")     or \
                (tokens_reservadas[1].lower() == "case")       or \
                (tokens_reservadas[1].lower() == "default")    or \
                (tokens_reservadas[1].lower() == "int")        or \
                (tokens_reservadas[1].lower() == "double")     or \
                (tokens_reservadas[1].lower() == "string")     or \
                (tokens_reservadas[1].lower() == "char")       or \
                (tokens_reservadas[1].lower() == "boolean")    or \
                (tokens_reservadas[1].lower() == "continue")   or \
                (tokens_reservadas[1].lower() == "return")     or \
                (tokens_reservadas[1].lower() == "tolower")    or \
                (tokens_reservadas[1].lower() == "toupper")    or \
                (tokens_reservadas[1].lower() == "typeof")     or \
                (tokens_reservadas[1].lower() == "length")     or \
                (tokens_reservadas[1].lower() == "round")      or \
                (tokens_reservadas[1].lower() == "truncate")   or \
                (tokens_reservadas[1].lower() == "read"):

                tokens_reservadas[0] = "tk_reseverda"

        return global_lista

    # -------------------------------------------------------- HERRAMIENTAS ------------------------------------------------------
    def interpretar(self):
        #INTERFAZ
        import Gramatica as prueba
        
        result=self.scroll.text.get(1.0, tk.END+"-1c")
        self.scroll.text.delete("1.0","end")
        for array in self.set_paint(result):
            self.scroll.text.insert(INSERT, array[1], array[0])
        
        AST = prueba.interprete(result, self.scroll_consola)

        self.scroll_consola.delete("1.0","end")
        self.scroll_consola.insert(tk.INSERT, AST.get_consola())
        
        for d in self.table_error.get_children(): # Esto sirve para resetear la tabla de errores.
            self.table_error.delete(d)

        i = 0
        for pedo in AST.get_excepcion():
            self.table_error.insert(parent='', index=i, iid=i, text='', values=(f'{i+1}',f'{pedo.tipo}',f'{pedo.descripcion}',f'{pedo.fila}',f'{pedo.columna}'))
            print(pedo)
            i += 1

      
    def debugger(self):
        pass

    # -------------------------------------------------------- REPORTE ------------------------------------------------------

    def reporte_error(self):
        pass
    def reporte_ast(self):
        try:
            #root = Tk()
            ruta =  ""
            filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("TXT files","*.pdf"),("all files","*.*")))
            ruta = filename
            if ruta != "":
                wb.open_new(ruta)
                return ruta
            else:

                return None

        except IndexError as e:
            print(e)

    def reporte_tabla_simbolo(self):
        pass


class ScrollText(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        
        self.fontStyle = tkFont.Font(family="Courier New",size=8)
        # bg -> color de fondo --- foreground -> color al texto --- selectbrackgroud -> color a lo que seleccione --- inserbackgroud -> color al puntero
        self.text = tk.Text(self, bg='#000000', foreground="#ffffff", selectbackground="#c2c2c2", insertbackground='#ffffff',  height=23, width=95, font=self.fontStyle)

        self.scrollbar = tk.Scrollbar(self, bg='#000000', orient=tk.VERTICAL, command=self.text.yview)
        self.text.configure(yscrollcommand=self.scrollbar.set)

        self.numero_lineas = TextoLinea(self, width=35, bg='#000000')
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

class TextoLinea(tk.Canvas):
    def __init__(self, *args, **kwargs):
        tk.Canvas.__init__(self, *args, **kwargs, highlightthickness=0)
        self.textwidget = None

    def attach(self, text_widget):
        self.textwidget = text_widget

    def redraw(self, *args):
        self.delete("all")
        i = self.textwidget.index("@1,0")
        while True :
            dline= self.textwidget.dlineinfo(i)
            if dline is None: break
            y = dline[1]
            linenum = str(i).split(".")[0]
            self.create_text(2, y, anchor="nw", text=linenum, fill="#606366")
            i = self.textwidget.index("%s+1line" % i)


    

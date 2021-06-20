from Interprete.TS.Exception import Exception

errores = []
reservadas = {
    'print'   : 'RPRINT',
    'var'     : 'RVAR',
    'true'    : 'RTRUE',
    'false'   : 'RFALSE',
    'if'      : 'RIF',
    'else'    : 'RELSE',
    'while'   : 'RWHILE',
    'break'   : 'RBREAK',
    'null'    : 'RNULL',
    'main'    : 'RMAIN',
    'func'    : 'RFUNC',
    'for'     : 'RFOR',
    'switch'  : 'RSWITCH',
    'case'    : 'RCASE',
    'default' : 'RDEFAULT'
}


tokens  = [
    'PUNTOCOMA',
    'PARA',
    'PARC',
    'LLAVEA',
    'LLAVEC',
    'IGUAL',
    'MAS',
    'MENOS',
    'POR',
    'DIV',
    'POT',
    'MODULO',
    'MENORQUE',
    'MENORIGUAL',
    'MAYORIGUAL',
    'MAYORQUE',
    'IGUALIGUAL',
    'DIFERENCIA',
    'AND',
    'OR',
    'NOT',
    'DECIMAL',
    'ENTERO',
    'CADENA',
    'CHAR',
    'ID',
    'COMENTARIO_SIMPLE',
    'COMENTARIO_VARIAS_LINEAS',
    'INCREMENTO',
    'DECREMENTO',
    'DOSPUNTOS',
] + list(reservadas.values())

# Tokens
t_PUNTOCOMA     = r';'
t_PARA          = r'\('
t_PARC          = r'\)'
t_LLAVEA        = r'\{'
t_LLAVEC        = r'\}'
t_IGUAL         = r'='
t_MAS           = r'\+'
t_MENOS         = r'-'
t_POR           = r'\*'
t_DIV           = r'\/'
t_POT           = r'\*\*'
t_MODULO        = r'\%'
t_MENORQUE      = r'<'
t_MENORIGUAL    = r'<='
t_MAYORQUE      = r'>'
t_MAYORIGUAL    = r'>='
t_IGUALIGUAL    = r'=='
t_AND           = r'&&'
t_OR            = r'\|\|'
t_NOT           = r'!'
t_DIFERENCIA    = r'=!'
t_INCREMENTO    = r'\+\+'
t_DECREMENTO    = r'\-\-'
t_DOSPUNTOS     = r'\:'

def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_ID(t):
     r'[a-zA-Z][a-zA-Z_0-9]*'
     t.type = reservadas.get(t.value.lower(),'ID')
     return t

def t_CADENA(t):
    #r'(\".*?\")'
    # t.value = t.value[1:-1] # remuevo las comillas
    # return t
    r'\"(\\"|.)*?\"'
    t.value = t.value[1:-1]  # remover comillas
    t.value = t.value.replace('\\n', '\n')
    t.value = t.value.replace('\\r', '\r')
    t.value = t.value.replace('\\\\', '\\')
    t.value = t.value.replace('\\"', '\"')
    t.value = t.value.replace('\\t', '\t')
    t.value = t.value.replace("\\'", '\'')
    return t

def t_CHAR(t):
    r"""\' (\\'| \\\\ | \\n | \\t | \\r | \\" | .)? \'"""
    t.value = t.value[1:-1]  # remover comillas
    t.value = t.value.replace('\\n', '\n')
    t.value = t.value.replace('\\r', '\r')
    t.value = t.value.replace('\\\\', '\\')
    t.value = t.value.replace('\\"', '\"')
    t.value = t.value.replace('\\t', '\t')
    t.value = t.value.replace("\\'", '\'')
    return t

def t_COMENTARIO_VARIAS_LINEAS(t):
    r'\#\*(.|\n)*?\*\#'
    t.lexer.lineno += t.value.count("\n") 

# Comentario simple // ...
def t_COMENTARIO_SIMPLE(t):
    r'\#.*\n'
    t.lexer.lineno += 1
       

# Caracteres ignorados
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    errores.append(Exception("Lexico","Error léxico." + t.value[0] , t.lexer.lineno, find_column(input, t)))
    t.lexer.skip(1)

# Compute column.
#     input is the input text string
#     token is a token instance
def find_column(inp, token):
    line_start = inp.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

# Construyendo el analizador léxico
import Interprete.ply.lex as lex
lexer = lex.lex()
# Asociacion
precedence = (
    ('left','OR'),
    ('left','AND'),
    ('right','UNOT'),
    ('left','IGUALIGUAL','DIFERENCIA','MENORQUE','MENORIGUAL','MAYORQUE','MAYORIGUAL'),
    ('left','MAS','MENOS'),
    ('left','DIV','POR','MODULO'),
    ('nonassoc', 'POT'),
    ('right','UMENOS'),
    )

# Definición de la gramática

#Abstract
from Interprete.Instrucciones.IncrementoDecremento import IncrementoDecremento
from Interprete.Instrucciones.Declaracion import Declaracion
from Interprete.Instrucciones.Asignacion import Asignacion
from Interprete.Instrucciones.Imprimir import Imprimir
from Interprete.Instrucciones.LLamada import Llamada
from Interprete.Instrucciones.Funcion import Funcion
from Interprete.Instrucciones.Default import Default
from Interprete.Instrucciones.Switch import Switch
from Interprete.Instrucciones.While import While
from Interprete.Instrucciones.Break import Break
from Interprete.Instrucciones.Case import Case
from Interprete.Instrucciones.Main import Main
from Interprete.Instrucciones.For import For
from Interprete.Instrucciones.If import If

from Interprete.Abstract.Instruccion import Instruccion
from Interprete.TS.Tipo import *

from Interprete.Expresiones.Identificador import Identificador
from Interprete.Expresiones.Primitivos import Primitivos
from Interprete.Expresiones.Aritmetica import Aritmetica
from Interprete.Expresiones.Relacional import Relacional
from Interprete.Expresiones.Logica import Logica

def p_init(t) :
    'init            : instrucciones'
    t[0] = t[1]

def p_instrucciones_instrucciones_instruccion(t) :
    'instrucciones    : instrucciones instruccion'
    if t[2] != "":
        t[1].append(t[2])
    t[0] = t[1]
    
# --------------------------------------------- INSTRUCCIONES ---------------------------------------------

def p_instrucciones_instruccion(t) :
    'instrucciones    : instruccion'
    if t[1] == "":
        t[0] = []
    else:    
        t[0] = [t[1]]

# --------------------------------------------- INSTRUCCION ---------------------------------------------

def p_instruccion(t):
    '''instruccion  : imprimir_ fin_instruccion
                    | declaracion_ins fin_instruccion
                    | incre_decre_ins fin_instruccion
                    | if_ins
                    | while_ins
                    | switch_ins
                    | for_ins
                    | main_ins
                    | break_ins fin_instruccion
                    | funcion_ins
                    | llamada_ins
                    | COMENTARIO_VARIAS_LINEAS
                    | COMENTARIO_SIMPLE
                    
                    
    '''
    t[0] = t[1]

def p_decla(t):
    ''' declaracion_ins : declaracion_ 
                        | declaracion_comp
                        | asignacion_ins '''
        
    t[0] = t[1]

# ---------------------------------------- DECLARACION FOR -------------------------------------------
def p_declaracion_for(t):
    ''' declaracion_for : declaracion_comp
                        | asignacion_ins '''
        
    t[0] = t[1]

def p_actualizacion_for(t):
    ''' asignacion_for : asignacion_ins 
                        | incre_decre_ins '''
        
    t[0] = t[1]



# ---------------------------------------- ERROR EN PUNTO COMA -------------------------------------------
def p_instruccion_error(t):
    'instruccion        : error PUNTOCOMA'
    errores.append(Exception("Sintáctico","Error Sintáctico." + str(t[1].value) , t.lineno(1), find_column(input, t.slice[1])))
    t[0] = ""

def p_fin_instruc(t) :
    '''fin_instruccion  : PUNTOCOMA
                        | '''
    t[0] = None
# ------------------------------------------ DECLARACION ---------------------------------------------
def p_declaracion_simple(t):
    '''declaracion_  :  TIPO ID'''
    
    t[0] = Declaracion(t[1], t[2], t.lineno(2), find_column(input, t.slice[2]))

def p_declaracion_completa(t):
    'declaracion_comp  : TIPO ID IGUAL expresion'

    t[0] = Declaracion(t[1], t[2], t.lineno(2), find_column(input, t.slice[2]), t[4])

# ------------------------------------------ ASIGNACION ---------------------------------------------
def p_asignacion_i(t):
    'asignacion_ins    : ID IGUAL expresion'
    t[0] = Asignacion(t[1], t[3], t.lineno(1), find_column(input, t.slice[1]))
# --------------------------------------------- IMPRIMIR ---------------------------------------------

def p_imprimir(t) :
    'imprimir_   : RPRINT PARA expresion PARC'
    t[0] = Imprimir(t[3], t.lineno(1), find_column(input, t.slice[1]))


# --------------------------------------------- SENTENCIA IF ---------------------------------------------

def p_condi_if(t): # Condicion if si solo viene un if
    'if_ins     : RIF PARA expresion PARC LLAVEA instrucciones LLAVEC'
    t[0] = If(t[3], t[6], None, None, t.lineno(1), find_column(input, t.slice[1]))

def p_condi_if_dos(t) : # condicion if si solo viene un if y un else
    'if_ins     : RIF PARA expresion PARC LLAVEA instrucciones LLAVEC RELSE LLAVEA instrucciones LLAVEC'
    t[0] = If(t[3], t[6], t[10], None, t.lineno(1), find_column(input, t.slice[1]))

def p_condi_if_tres(t) : # condicion para que pueda venir un else if, o un else if y un else.
    'if_ins     : RIF PARA expresion PARC LLAVEA instrucciones LLAVEC RELSE if_ins'
    t[0] = If(t[3], t[6], None, t[9], t.lineno(1), find_column(input, t.slice[1]))

# --------------------------------------------- SENTENCIA SWITCH ---------------------------------------------
def p_condicion_switch_case_list_default(t): # Aqui verifiac que la condicion venga  [<CASES_LIST>] [<DEFAULT>]
    'switch_ins   : RSWITCH PARA expresion PARC LLAVEA case_switch_ins default_switch LLAVEC'
    t[0] = Switch(t[3], t[6], t[7] ,t.lineno(1), find_column(input, t.slice[1]))

def p_condicion_switch_case_list(t): # Aqui verifiac que la condicion venga  [<CASES_LIST>]
    'switch_ins   : RSWITCH PARA expresion PARC LLAVEA case_switch_ins LLAVEC'
    t[0] = Switch(t[3], t[6], None, t.lineno(1), find_column(input, t.slice[1]))

def p_condicion_switch_default(t): # Aqui verifiac que la condicion venga   [<DEFAULT>]
    'switch_ins   : RSWITCH PARA expresion PARC LLAVEA default_switch LLAVEC'
    t[0] = Switch(t[3], None, t[6], t.lineno(1), find_column(input, t.slice[1]))

def p_casos_switch_ins_caso_switch(t): # Aqui hace a que sea recursivo y puedan venir infinitos [<CASES_LIST>]
    'case_switch_ins : case_switch_ins case_switch'
    if t[2] != "":
        t[1].append(t[2])
    t[0] = t[1]

def p_caso_switch_(t):
    'case_switch_ins : case_switch'
    if t[1] == "":
        t[0] = []
    else:    
        t[0] = [t[1]]

def p_condicion_switch_case(t):
    'case_switch  : RCASE expresion DOSPUNTOS instrucciones'
    t[0] = Case(t[2], t[4], t.lineno(1), find_column(input, t.slice[1]))

def p_condicion_default_switch(t):
    'default_switch : RDEFAULT DOSPUNTOS instrucciones'
    # t[0] = t[3]
    t[0] = Default(t[3], t.lineno(1), find_column(input, t.slice[1]))


# --------------------------------------------- WHILE --------------------------------------------- 
def p_sentencia_while(t) :
    'while_ins     : RWHILE PARA expresion PARC LLAVEA instrucciones LLAVEC'
    t[0] = While(t[3], t[6], t.lineno(1), find_column(input, t.slice[1]))

# --------------------------------------------- FOR --------------------------------------------- 
def p_sentencia_for(t) :
    'for_ins     : RFOR PARA declaracion_for PUNTOCOMA expresion PUNTOCOMA asignacion_for PARC LLAVEA instrucciones LLAVEC'
    t[0] = For(t[3], t[5], t[7], t[10],  t.lineno(1), find_column(input, t.slice[1]))

# --------------------------------------------- MAIN --------------------------------------------- 
def p_main(t) :
    'main_ins     : RMAIN PARA PARC LLAVEA instrucciones LLAVEC'
    t[0] = Main(t[5], t.lineno(1), find_column(input, t.slice[1]))

# --------------------------------------------- FUNCION --------------------------------------------- 

def p_funcion(t) :
    'funcion_ins     : RFUNC ID PARA PARC LLAVEA instrucciones LLAVEC'
    t[0] = Funcion(t[2], t[6], t.lineno(1), find_column(input, t.slice[1]))

# --------------------------------------------- LLAMADA --------------------------------------------- 

def p_llamada_de_funcion(t) :
    'llamada_ins     : ID PARA PARC'
    t[0] = Llamada(t[1], t.lineno(1), find_column(input, t.slice[1]))

# --------------------------------------------- BREAK ---------------------------------------------
def p_sentencia_break(t) :
    'break_ins     : RBREAK'
    t[0] = Break(t.lineno(1), find_column(input, t.slice[1]))
# --------------------------------------------- TIPO ---------------------------------------------
def p_tipo_dato(t):
    '''TIPO :  RVAR'''

    if t[1] == 'var':
        t[0] = Tipo.NULO
# --------------------------------------------- INCREMENTO O DECREMENTO ---------------------------------------------
def p_incremento_decremento(t):
    ''' incre_decre_ins : ID INCREMENTO
                        | ID DECREMENTO'''

    if t[2] == '++':
        t[0] = IncrementoDecremento(t[1], Operador_Aritmetico.INCREMENTO, t.lineno(1), find_column(input, t.slice[1]))
    elif t[2] == '--':
        t[0] = IncrementoDecremento(t[1], Operador_Aritmetico.DECREMENTO, t.lineno(1), find_column(input, t.slice[1]))
   
    

# --------------------------------------------- EXPRESION ---------------------------------------------

def p_expresion_binaria(t):
    '''
    expresion : expresion MAS expresion
            | expresion MENOS expresion
            | expresion POR expresion
            | expresion DIV expresion
            | expresion POT expresion
            | expresion MODULO expresion
            | expresion MENORQUE expresion
            | expresion MENORIGUAL expresion
            | expresion MAYORQUE expresion
            | expresion MAYORIGUAL expresion
            | expresion IGUALIGUAL expresion
            | expresion DIFERENCIA expresion
            | expresion AND expresion
            | expresion OR expresion
    '''
    if t[2] == '+':
        t[0] = Aritmetica(Operador_Aritmetico.SUMA, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '-':
        t[0] = Aritmetica(Operador_Aritmetico.RESTA, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '*':
        t[0] = Aritmetica(Operador_Aritmetico.POR, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '/':
        t[0] = Aritmetica(Operador_Aritmetico.DIV, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))   
    elif t[2] == '**':
        t[0] = Aritmetica(Operador_Aritmetico.POTE, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '%':
        t[0] = Aritmetica(Operador_Aritmetico.MODU, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))  

    elif t[2] == '==':
        t[0] = Relacional(Operador_Relacional.IGUALACION, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '<':
        t[0] = Relacional(Operador_Relacional.MENORQUE, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '<=':
        t[0] = Relacional(Operador_Relacional.MENORIGUAL, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '>':
        t[0] = Relacional(Operador_Relacional.MAYORQUE, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '>=':
        t[0] = Relacional(Operador_Relacional.MAYORIGUAL, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '=!':
        t[0] = Relacional(Operador_Relacional.DIFERENCIA, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))

    elif t[2] == '&&':
        t[0] = Logica(Operador_Logico.AND, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '||':
        t[0] = Logica(Operador_Logico.OR, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
   

def p_expresion_unaria(t):
    '''
    expresion : MENOS expresion %prec UMENOS 
            | NOT expresion %prec UNOT 
    '''
    if t[1] == '-':
        t[0] = Aritmetica(Operador_Aritmetico.UMENOS, t[2],None, t.lineno(1), find_column(input, t.slice[1]))
    elif t[1] == '!':
         t[0] = Logica(Operador_Logico.NOT, t[2],None, t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_agrupacion(t):
    '''
    expresion :   PARA expresion PARC 
    '''
    t[0] = t[2]

def p_expresion_identificador(t):
    '''expresion : ID'''
    
    t[0] = Identificador(t[1], t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_entero(t):
    '''expresion : ENTERO'''
    t[0] = Primitivos(Tipo.ENTERO,t[1], t.lineno(1), find_column(input, t.slice[1]))

def p_primitivo_decimal(t):
    '''expresion : DECIMAL'''
    t[0] = Primitivos(Tipo.DECIMAL, t[1], t.lineno(1), find_column(input, t.slice[1]))

def p_primitivo_cadena(t):
    '''expresion : CADENA'''
    t[0] = Primitivos(Tipo.CADENA,str(t[1]).replace('\\n', '\n'), t.lineno(1), find_column(input, t.slice[1]))

def p_primitivo_char(t):
    '''expresion : CHAR'''
    t[0] = Primitivos(Tipo.CHAR,str(t[1]).replace('\\n', '\n'), t.lineno(1), find_column(input, t.slice[1]))

def p_primitivo_true(t):
    '''expresion : RTRUE'''
    t[0] = Primitivos(Tipo.BOOLEANO, True, t.lineno(1), find_column(input, t.slice[1]))

def p_primitivo_false(t):
    '''expresion : RFALSE'''
    t[0] = Primitivos(Tipo.BOOLEANO, False, t.lineno(1), find_column(input, t.slice[1]))

def p_primitivo_null(t):
    '''expresion : RNULL '''
    t[0] = Primitivos(Tipo.NULO, None, t.lineno(1), find_column(input, t.slice[1]))


import Interprete.ply.yacc as yacc
parser = yacc.yacc()

input = ''

def getErrores():
    return errores

def parse(inp) :
    global errores
    global lexer
    global parser
    errores = []
    lexer = lex.lex()
    parser = yacc.yacc()
    global input
    input = inp
    return parser.parse(inp)

#INTERFAZ

f = open("./entrada.txt", "r")
entrada = f.read()
from Interprete.TS.Arbol import Arbol
from Interprete.TS.TablaSimbolo import TablaSimbolo

instrucciones = parse(entrada) # ARBOL AST
ast = Arbol(instrucciones)
TSGlobal = TablaSimbolo()
ast.set_tabla_ts_global(TSGlobal)
for error in errores:                   # Aqui va a "Capturar o Guardar" todo error Lexico y Sintactico.
    ast.get_excepcion().append(error)
    ast.update_consola(error.__str__())

for instruccion in ast.get_instruccion():      # 1ERA PASADA (DECLARACIONES Y ASIGNACIONES)
    if isinstance(instruccion, Funcion):
        ast.addFuncion(instruccion)     # GUARDAR LA FUNCION EN "MEMORIA" (EN EL ARBOL)
    if isinstance(instruccion, Declaracion) or isinstance(instruccion, Asignacion):
        value = instruccion.interpretar(ast,TSGlobal)
        if isinstance(value, Exception) :
            ast.get_excepcion().append(value)
            ast.update_consola(value.__str__())
        if isinstance(value, Break): 
            err = Exception("Semantico", "Sentencia BREAK fuera de ciclo", instruccion.fila, instruccion.columna)
            ast.get_excepcion().append(err)
            ast.update_consola(err.__str__())


for instruccion in ast.get_instruccion():      # Verfiica con esta instruccion que el main no sea repetido
    i = 0
    if isinstance(instruccion, Main):
        i += 1
        if i == 2: # VERIFICAR LA DUPLICIDAD
            err = Exception("Semantico", "Existen 2 funciones Main", instruccion.fila, instruccion.columna)
            ast.get_excepcion().append(err)
            ast.update_consola(err.__str__())
            break
        value = instruccion.interpretar(ast,TSGlobal)
        if isinstance(value, Exception) :
            ast.get_excepcion().append(value)
            ast.update_consola(value.__str__())
        if isinstance(value, Break): 
            err = Exception("Semantico", "Sentencia BREAK fuera de ciclo", instruccion.fila, instruccion.columna)
            ast.get_excepcion().append(err)
            ast.update_consola(err.__str__())

for instruccion in ast.get_instruccion():    # Ultima vez que lo reccore, va a buscar funciones fuera del main
    if not (isinstance(instruccion, Main) or isinstance(instruccion, Declaracion) or isinstance(instruccion, Asignacion) or isinstance(instruccion, Funcion)):
        err = Exception("Semantico", "Sentencias fuera de Main", instruccion.fila, instruccion.columna)
        ast.get_excepcion().append(err)
        ast.update_consola(err.__str__())

print(ast.get_consola())


def interprete(entrada):
    from Interprete.TS.Arbol import Arbol
    from Interprete.TS.TablaSimbolo import TablaSimbolo

    instrucciones = parse(entrada) # ARBOL AST
    ast = Arbol(instrucciones)
    TSGlobal = TablaSimbolo()
    ast.set_tabla_ts_global(TSGlobal)
    for error in errores:                   # Aqui va a "Capturar o Guardar" todo error Lexico y Sintactico.
        ast.get_excepcion().append(error)
        ast.update_consola(error.__str__())

    for instruccion in ast.get_instruccion():      # 1ERA PASADA (DECLARACIONES Y ASIGNACIONES)
        if isinstance(instruccion, Funcion):
            ast.addFuncion(instruccion)     # GUARDAR LA FUNCION EN "MEMORIA" (EN EL ARBOL)
        if isinstance(instruccion, Declaracion) or isinstance(instruccion, Asignacion):
            value = instruccion.interpretar(ast,TSGlobal)
            if isinstance(value, Exception) :
                ast.get_excepcion().append(value)
                ast.update_consola(value.__str__())
            if isinstance(value, Break): 
                err = Exception("Semantico", "Sentencia BREAK fuera de ciclo", instruccion.fila, instruccion.columna)
                ast.get_excepcion().append(err)
                ast.update_consola(err.__str__())


    for instruccion in ast.get_instruccion():      # Verfiica con esta instruccion que el main no sea repetido
        i = 0
        if isinstance(instruccion, Main):
            i += 1
            if i == 2: # VERIFICAR LA DUPLICIDAD
                err = Exception("Semantico", "Existen 2 funciones Main", instruccion.fila, instruccion.columna)
                ast.get_excepcion().append(err)
                ast.update_consola(err.__str__())
                break
            value = instruccion.interpretar(ast,TSGlobal)
            if isinstance(value, Exception) :
                ast.get_excepcion().append(value)
                ast.update_consola(value.__str__())
            if isinstance(value, Break): 
                err = Exception("Semantico", "Sentencia BREAK fuera de ciclo", instruccion.fila, instruccion.columna)
                ast.get_excepcion().append(err)
                ast.update_consola(err.__str__())

    for instruccion in ast.get_instruccion():    # Ultima vez que lo reccore, va a buscar funciones fuera del main
        if not (isinstance(instruccion, Main) or isinstance(instruccion, Declaracion) or isinstance(instruccion, Asignacion) or isinstance(instruccion, Funcion)):
            err = Exception("Semantico", "Sentencias fuera de Main", instruccion.fila, instruccion.columna)
            ast.get_excepcion().append(err)
            ast.update_consola(err.__str__())

    return ast
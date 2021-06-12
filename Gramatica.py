from Interprete.TS.Exception import Exception

errores = []
reservadas = {
    'print' : 'RPRINT',
    'true'  : 'RTRUE',
    'false' : 'RFALSE',
}

tokens  = [
    'PUNTOCOMA',
    'PARA',
    'PARC',
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
    'ID'
] + list(reservadas.values())

# Tokens
t_PUNTOCOMA     = r';'
t_PARA          = r'\('
t_PARC          = r'\)'
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
t_DIFERENCIA    = r'!='

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
    r'(\".*?\")'
    t.value = t.value[1:-1] # remuevo las comillas
    return t

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
    ('right','UMENOS'),
    )

# Definición de la gramática

#Abstract
from Interprete.Abstract.Instruccion import Instruccion
from Interprete.Instrucciones.Imprimir import Imprimir
from Interprete.TS.Tipo import *

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
    
#///////////////////////////////////////INSTRUCCIONES//////////////////////////////////////////////////

def p_instrucciones_instruccion(t) :
    'instrucciones    : instruccion'
    if t[1] == "":
        t[0] = []
    else:    
        t[0] = [t[1]]

#///////////////////////////////////////INSTRUCCION//////////////////////////////////////////////////

def p_instruccion(t) :
    '''instruccion      : imprimir_instr'''
    t[0] = t[1]

def p_instruccion_error(t):
    'instruccion        : error PUNTOCOMA'
    errores.append(Exception("Sintáctico","Error Sintáctico." + str(t[1].value) , t.lineno(1), find_column(input, t.slice[1])))
    t[0] = ""
#///////////////////////////////////////IMPRIMIR//////////////////////////////////////////////////

def p_imprimir(t) :
    'imprimir_instr     : RPRINT PARA expresion PARC PUNTOCOMA'
    t[0] = Imprimir(t[3], t.lineno(1), find_column(input, t.slice[1]))

#///////////////////////////////////////EXPRESION//////////////////////////////////////////////////

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

    elif t[2] == '<':
        t[0] = Relacional(Operador_Relacional.MENORQUE, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '<=':
        t[0] = Relacional(Operador_Relacional.MENORIGUAL, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '>':
        t[0] = Relacional(Operador_Relacional.MAYORQUE, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '>=':
        t[0] = Relacional(Operador_Relacional.MAYORIGUAL, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '==':
        t[0] = Relacional(Operador_Relacional.IGUALACION, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '!=':
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
    # elif t[1] == '!':
    #     t[0] = Relacional(Operador_Aelacional.NOT, t[2],None, t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_entero(t):
    '''expresion : ENTERO'''
    t[0] = Primitivos(Tipo.ENTERO,t[1], t.lineno(1), find_column(input, t.slice[1]))

def p_primitivo_decimal(t):
    '''expresion : DECIMAL'''
    t[0] = Primitivos(Tipo.DECIMAL, t[1], t.lineno(1), find_column(input, t.slice[1]))

def p_primitivo_cadena(t):
    '''expresion : CADENA'''
    t[0] = Primitivos(Tipo.CADENA,str(t[1]).replace('\\n', '\n'), t.lineno(1), find_column(input, t.slice[1]))


def p_primitivo_boolean(t):
    '''
    expresion : RTRUE
            | RFALSE
    '''
    t[0] = Primitivos(Tipo.BOOLEANO,t[1], t.lineno(1), find_column(input, t.slice[1]))

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

instrucciones = parse(entrada) #ARBOL AST
ast = Arbol(instrucciones)
TSGlobal = TablaSimbolo()
ast.set_tabla_ts_global(TSGlobal)
for error in errores:                   #CAPTURA DE ERRORES LEXICOS Y SINTACTICOS
    ast.get_excepcion().append(error)
    ast.update_consola(error.__str__())

for instruccion in ast.get_instruccion():      # REALIZAR LAS ACCIONES
    value = instruccion.interpretar(ast,TSGlobal)
    if isinstance(value, Exception) :
        ast.get_excepcion().append(value)
        ast.update_consola(value.__str__())

print(ast.get_consola())
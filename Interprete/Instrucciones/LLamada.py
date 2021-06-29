from Interprete.Abstract.Instruccion import Instruccion
from Interprete.TS.Exception import Exception
from Interprete.TS.TablaSimbolo import TablaSimbolo
from Interprete.Instrucciones.Break import Break
from Interprete.TS.Simbolo import Simbolo
from Interprete.Instrucciones.Funcion import Funcion
from Interprete.Abstract.NodoAST import NodoAST


class Llamada(Instruccion):
    def __init__(self, nombre, parametros, fila, columna):
        self.nombre = nombre
        self.parametros = parametros
        self.fila = fila
        self.columna = columna
    
    def interpretar(self, tree, table):
        result = tree.getFuncion(self.nombre.lower())       # OBTENER LA FUNCION
        if result == None: # NO SE ENCONTRO LA FUNCION
            return Exception("Semantico", "No existe una funcionn con ese nombre: " + self.nombre, self.fila, self.columna)
        nuevaTabla = TablaSimbolo(tree.get_tabla_ts_global())
        # OBTENER PARAMETROS
        if len(result.parametros) == len(self.parametros): #LA CANTIDAD DE PARAMETROS ES LA ADECUADA
            contador=0
            for expresion in self.parametros: # SE OBTIENE EL VALOR DEL PARAMETRO EN LA LLAMADA
                resultExpresion = expresion.interpretar(tree, table)
                if isinstance(resultExpresion, Exception): return resultExpresion
                
                
                if result.parametros[contador]["tipoDato"] == expresion.tipo:  # VERIFICACION DE TIPO
                    # CREACION DE SIMBOLO E INGRESARLO A LA TABLA DE SIMBOLOS
                    simbolo = Simbolo(str(result.parametros[contador]['identificador']), result.parametros[contador]['tipoDato'], self.fila, self.columna, resultExpresion)
                    resultTabla = nuevaTabla.setTabla(simbolo)
                    if isinstance(resultTabla, Exception): return resultTabla
                    
                elif result.parametros[contador]["identificador"] == "truncate##Param1":  # VERIFICACION DE TIPO
                    # CREACION DE SIMBOLO E INGRESARLO A LA TABLA DE SIMBOLOS
                    
                    simbolo = Simbolo(str(result.parametros[contador]['identificador']), result.parametros[contador]['tipoDato'], self.fila, self.columna, resultExpresion)
                    resultTabla = nuevaTabla.setTabla(simbolo)
                    if isinstance(resultTabla, Exception): return resultTabla

                elif result.parametros[contador]["identificador"] == "round##Param1":  # VERIFICACION DE TIPO
                    # CREACION DE SIMBOLO E INGRESARLO A LA TABLA DE SIMBOLOS

                    simbolo = Simbolo(str(result.parametros[contador]['identificador']), expresion.tipo, self.fila, self.columna, resultExpresion)
                    resultTabla = nuevaTabla.setTabla(simbolo)
                    if isinstance(resultTabla, Exception): return resultTabla

                elif result.parametros[contador]["identificador"] == "typeOf##Param1":  # VERIFICACION DE TIPO
                    # CREACION DE SIMBOLO E INGRESARLO A LA TABLA DE SIMBOLOS
                    result.parametros[contador]['tipoDato'] = expresion.tipo
                    simbolo = Simbolo(str(result.parametros[contador]['identificador']), expresion.tipo, self.fila, self.columna, resultExpresion)
                    resultTabla = nuevaTabla.setTabla(simbolo)
                    if isinstance(resultTabla, Exception): return resultTabla

                else:
                    return Exception("Semantico", "Tipo de dato diferente en Parametros de la llamada.", self.fila, self.columna)
                contador += 1

            
        else: 
            return Exception("Semantico", "Cantidad de Parametros incorrecta.", self.fila, self.columna)
    
        value = result.interpretar(tree, nuevaTabla)         # INTERPRETAR EL NODO FUNCION
        if isinstance(value, Exception): return value
        self.tipo = result.tipo
        
        return value


    def getNodo(self):
        nodo = NodoAST("LLAMADA A FUNCION")
        nodo.agregarHijo(str(self.nombre))

        parametros = NodoAST("PARAMETROS")
        for param in self.parametros:
            parametros.agregarHijoNodo(param.getNodo())
        nodo.agregarHijoNodo(parametros)
        
        return nodo
from Interprete.Abstract.Instruccion import Instruccion
from Interprete.TS.Exception import Exception
from Interprete.TS.Tipo import *

class Casteo(Instruccion):
    def __init__(self, tipo, expresion, fila, columna):
        self.expresion = expresion
        self.fila = fila
        self.columna = columna
        self.tipo = tipo

    
    def interpretar(self, tree, table):
        val = self.expresion.interpretar(tree, table)
        
        if self.tipo == Tipo.DECIMAL: # Este es el tipo que se quiere convertir.
            if self.expresion.tipo == Tipo.ENTERO: # Este es el tipo de la expresion(int).                      -> Decimal a int
                try:
                    return float(self.obtenerVal(self.expresion.tipo, val))
                except:
                    return Exception("Semantico", "No se puede castear para Double a Int.", self.fila, self.columna)
            elif self.expresion.tipo == Tipo.CADENA: # Este es el tipo de la expresion(String).                 -> Decimal a String
                try:
                    return float(self.obtenerVal(self.expresion.tipo, val))
                except:
                    return Exception("Semantico", "No se puede castear para Double a String.", self.fila, self.columna)
            return Exception("Semantico", "Tipo Erroneo de casteo para Double.", self.fila, self.columna)

        elif self.tipo == Tipo.ENTERO:
            if self.expresion.tipo == Tipo.DECIMAL:# Este es el tipo de la expresion(Double).                    -> Int a Double
                try:
                    return int(self.obtenerVal(self.expresion.tipo, val))
                except:
                    return Exception("Semantico", "No se puede castear para Int a Double.", self.fila, self.columna)
            elif self.expresion.tipo == Tipo.CADENA:# Este es el tipo de la expresion(String).                   -> Int a String
                try:
                    return int(self.obtenerVal(self.expresion.tipo, val))
                except:
                    return Exception("Semantico", "No se puede castear para Int a String.", self.fila, self.columna)
            elif self.expresion.tipo == Tipo.CHAR:# Este es el tipo de la expresion(Char).                        -> Int a Char
                try:
                    return int(self.obtenerVal(self.expresion.tipo, val))
                except:
                    return Exception("Semantico", "No se puede castear para Int a Char.", self.fila, self.columna)
            return Exception("Semantico", "Tipo Erroneo de casteo para Int.", self.fila, self.columna)

        elif self.tipo == Tipo.CHAR:
            if self.expresion.tipo == Tipo.DECIMAL:# Este es el tipo de la expresion(Double).                    -> Char a Double
                try:
                    return str(self.obtenerVal(self.expresion.tipo, val))
                except:
                    return Exception("Semantico", "No se puede castear para Int a Double.", self.fila, self.columna)
            elif self.expresion.tipo == Tipo.ENTERO:# Este es el tipo de la expresion(String).                   -> Char a Int
                try:
                    return str(self.obtenerVal(self.expresion.tipo, val))
                except:
                    return Exception("Semantico", "No se puede castear para Int a String.", self.fila, self.columna)
            return Exception("Semantico", "Tipo Erroneo de casteo para Char.", self.fila, self.columna)
                
        elif self.tipo == Tipo.CADENA:
            if self.expresion.tipo == Tipo.DECIMAL:# Este es el tipo de la expresion(Double).                    -> String a Double
                try:
                    return str(self.obtenerVal(self.expresion.tipo, val))
                except:
                    return Exception("Semantico", "No se puede castear para String a Double.", self.fila, self.columna)
            elif self.expresion.tipo == Tipo.ENTERO:# Este es el tipo de la expresion(String).                   -> String a Int
                try:
                    return str(self.obtenerVal(self.expresion.tipo, val))
                except:
                    return Exception("Semantico", "No se puede castear para String a Int.", self.fila, self.columna)
            elif self.expresion.tipo == Tipo.BOOLEANO:# Este es el tipo de la expresion(String).                   -> Char a Int
                try:
                    return str(self.obtenerVal(self.expresion.tipo, val))
                except:
                    return Exception("Semantico", "No se puede castear para String a Int.", self.fila, self.columna)
            return Exception("Semantico", "Tipo Erroneo de casteo para Char.", self.fila, self.columna)

    def obtenerVal(self, tipo, val):
        if tipo == TIPO.ENTERO:
            return int(val)
        elif tipo == TIPO.DECIMAL:
            return float(val)
        elif tipo == TIPO.BOOLEANO:
            return bool(val)
        return str(val)

    def toASCII(cadena):
        result = 0
        for char in cadena:
            result += ord(char)
        return result

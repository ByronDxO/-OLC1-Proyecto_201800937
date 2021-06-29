from Interprete.Abstract.Instruccion import Instruccion
from Interprete.TS.Exception import Exception
from Interprete.TS.Tipo import Tipo, Operador_Relacional
from Interprete.Abstract.NodoAST import NodoAST

class Relacional(Instruccion):

    def __init__(self, operador, OperacionIzq, OperacionDer, fila, columna):
        self.operador = operador
        self.OperacionIzq = OperacionIzq
        self.OperacionDer = OperacionDer
        self.fila = fila
        self.columna = columna
        self.tipo = Tipo.BOOLEANO

    def interpretar(self, tree, table):
        izq = self.OperacionIzq.interpretar(tree, table)
        if isinstance(izq, Exception): return izq
        der = self.OperacionDer.interpretar(tree, table)
        if isinstance(der, Exception): return der
        
        if self.operador == Operador_Relacional.IGUALACION:
            # INT
            if self.OperacionIzq.tipo == Tipo.ENTERO and self.OperacionDer.tipo == Tipo.ENTERO:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) == self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == Tipo.ENTERO and self.OperacionDer.tipo == Tipo.DECIMAL:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) == self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == Tipo.ENTERO and self.OperacionDer.tipo == Tipo.CADENA:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) == self.obtenerVal(self.OperacionDer.tipo, der)
            # DOUBLE
            elif self.OperacionIzq.tipo == Tipo.DECIMAL and self.OperacionDer.tipo == Tipo.ENTERO:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) == self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == Tipo.DECIMAL and self.OperacionDer.tipo == Tipo.DECIMAL:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) == self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == Tipo.DECIMAL and self.OperacionDer.tipo == Tipo.CADENA:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) == self.obtenerVal(self.OperacionDer.tipo, der)
            # BOOLEAN
            elif self.OperacionIzq.tipo == Tipo.BOOLEANO and self.OperacionDer.tipo == Tipo.BOOLEANO:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) == self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == Tipo.BOOLEANO and self.OperacionDer.tipo == Tipo.CADENA:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) == self.obtenerVal(self.OperacionDer.tipo, der)
            # CHAR
            elif self.OperacionIzq.tipo == Tipo.CHAR and self.OperacionDer.tipo == Tipo.CHAR:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) == self.obtenerVal(self.OperacionDer.tipo, der)
            # STRING
            elif self.OperacionIzq.tipo == Tipo.CADENA and self.OperacionDer.tipo == Tipo.ENTERO:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) == self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == Tipo.CADENA and self.OperacionDer.tipo == Tipo.DECIMAL:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) == self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == Tipo.CADENA and self.OperacionDer.tipo == Tipo.BOOLEANO:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) == self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == Tipo.CADENA and self.OperacionDer.tipo == Tipo.CADENA:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) == self.obtenerVal(self.OperacionDer.tipo, der)
            return Exception("Semantico", "Tipo Erroneo de operacion para ==.", self.fila, self.columna)

        elif self.operador == Operador_Relacional.DIFERENCIA:
            # INT
            if self.OperacionIzq.tipo == Tipo.ENTERO and self.OperacionDer.tipo == Tipo.ENTERO:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) != self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == Tipo.ENTERO and self.OperacionDer.tipo == Tipo.DECIMAL:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) != self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == Tipo.ENTERO and self.OperacionDer.tipo == Tipo.CADENA:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) != self.obtenerVal(self.OperacionDer.tipo, der)
            # DOUBLE
            elif self.OperacionIzq.tipo == Tipo.DECIMAL and self.OperacionDer.tipo == Tipo.ENTERO:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) != self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == Tipo.DECIMAL and self.OperacionDer.tipo == Tipo.DECIMAL:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) != self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == Tipo.DECIMAL and self.OperacionDer.tipo == Tipo.CADENA:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) != self.obtenerVal(self.OperacionDer.tipo, der)
            # BOOLEAN
            elif self.OperacionIzq.tipo == Tipo.BOOLEANO and self.OperacionDer.tipo == Tipo.BOOLEANO:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) != self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == Tipo.BOOLEANO and self.OperacionDer.tipo == Tipo.CADENA:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) != self.obtenerVal(self.OperacionDer.tipo, der)
            # CHAR
            elif self.OperacionIzq.tipo == Tipo.CHAR and self.OperacionDer.tipo == Tipo.CHAR:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) != self.obtenerVal(self.OperacionDer.tipo, der)
            # STRING
            elif self.OperacionIzq.tipo == Tipo.CADENA and self.OperacionDer.tipo == Tipo.ENTERO:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) != str(self.obtenerVal(self.OperacionDer.tipo, der))
            elif self.OperacionIzq.tipo == Tipo.CADENA and self.OperacionDer.tipo == Tipo.DECIMAL:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) != self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == Tipo.CADENA and self.OperacionDer.tipo == Tipo.BOOLEANO:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) != self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == Tipo.CADENA and self.OperacionDer.tipo == Tipo.CADENA:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) != self.obtenerVal(self.OperacionDer.tipo, der)
            return Exception("Semantico", "Tipo Erroneo de operacion para =!.", self.fila, self.columna)

        elif self.operador == Operador_Relacional.MENORQUE:
            # INT
            if self.OperacionIzq.tipo == Tipo.ENTERO and self.OperacionDer.tipo == Tipo.ENTERO:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) < self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == Tipo.ENTERO and self.OperacionDer.tipo == Tipo.DECIMAL:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) < self.obtenerVal(self.OperacionDer.tipo, der)
            # DOUBLE
            elif self.OperacionIzq.tipo == Tipo.DECIMAL and self.OperacionDer.tipo == Tipo.ENTERO:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) < self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == Tipo.DECIMAL and self.OperacionDer.tipo == Tipo.DECIMAL:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) < self.obtenerVal(self.OperacionDer.tipo, der)
            # BOOLEAN
            elif self.OperacionIzq.tipo == Tipo.BOOLEANO and self.OperacionDer.tipo == Tipo.BOOLEANO:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) < self.obtenerVal(self.OperacionDer.tipo, der)
            return Exception("Semantico", "Tipo Erroneo de operacion para <.", self.fila, self.columna)

        elif self.operador == Operador_Relacional.MAYORQUE:
            # INT
            if self.OperacionIzq.tipo == Tipo.ENTERO and self.OperacionDer.tipo == Tipo.ENTERO:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) > self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == Tipo.ENTERO and self.OperacionDer.tipo == Tipo.DECIMAL:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) > self.obtenerVal(self.OperacionDer.tipo, der)
            # DOUBLE
            elif self.OperacionIzq.tipo == Tipo.DECIMAL and self.OperacionDer.tipo == Tipo.ENTERO:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) > self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == Tipo.DECIMAL and self.OperacionDer.tipo == Tipo.DECIMAL:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) > self.obtenerVal(self.OperacionDer.tipo, der)
            # BOOLEAN
            elif self.OperacionIzq.tipo == Tipo.BOOLEANO and self.OperacionDer.tipo == Tipo.BOOLEANO:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) > self.obtenerVal(self.OperacionDer.tipo, der)
            return Exception("Semantico", "Tipo Erroneo de operacion para >.", self.fila, self.columna)
        
        elif self.operador == Operador_Relacional.MENORIGUAL:
            # INT
            if self.OperacionIzq.tipo == Tipo.ENTERO and self.OperacionDer.tipo == Tipo.ENTERO:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) <= self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == Tipo.ENTERO and self.OperacionDer.tipo == Tipo.DECIMAL:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) <= self.obtenerVal(self.OperacionDer.tipo, der)
            # DOUBLE
            elif self.OperacionIzq.tipo == Tipo.DECIMAL and self.OperacionDer.tipo == Tipo.ENTERO:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) <= self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == Tipo.DECIMAL and self.OperacionDer.tipo == Tipo.DECIMAL:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) <= self.obtenerVal(self.OperacionDer.tipo, der)
            # BOOLEAN
            elif self.OperacionIzq.tipo == Tipo.BOOLEANO and self.OperacionDer.tipo == Tipo.BOOLEANO:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) <= self.obtenerVal(self.OperacionDer.tipo, der)
            return Exception("Semantico", "Tipo Erroneo de operacion para <=.", self.fila, self.columna)
        
        elif self.operador == Operador_Relacional.MAYORIGUAL:
            # INT
            if self.OperacionIzq.tipo == Tipo.ENTERO and self.OperacionDer.tipo == Tipo.ENTERO:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) >= self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == Tipo.ENTERO and self.OperacionDer.tipo == Tipo.DECIMAL:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) >= self.obtenerVal(self.OperacionDer.tipo, der)
            # DOUBLE
            elif self.OperacionIzq.tipo == Tipo.DECIMAL and self.OperacionDer.tipo == Tipo.ENTERO:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) >= self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == Tipo.DECIMAL and self.OperacionDer.tipo == Tipo.DECIMAL:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) >= self.obtenerVal(self.OperacionDer.tipo, der)
            # BOOLEAN
            elif self.OperacionIzq.tipo == Tipo.BOOLEANO and self.OperacionDer.tipo == Tipo.BOOLEANO:
                return self.obtenerVal(self.OperacionIzq.tipo, izq) >= self.obtenerVal(self.OperacionDer.tipo, der)
            return Exception("Semantico", "Tipo Erroneo de operacion para >.", self.fila, self.columna)

        return Exception("Semantico", "Tipo de Operacion no Especificado.", self.fila, self.columna)

    def getNodo(self):
        nodo = NodoAST("RELACIONAL")
        nodo.agregarHijoNodo(self.OperacionIzq.getNodo())
        nodo.agregarHijo(str(self.operador))
        nodo.agregarHijoNodo(self.OperacionDer.getNodo())
        
        return nodo


    def obtenerVal(self, tipo, val):
        if tipo == Tipo.ENTERO:
            return int(val)
        elif tipo == Tipo.DECIMAL:
            return float(val)
        elif tipo == Tipo.BOOLEANO:
            return bool(val)
        return str(val)
        
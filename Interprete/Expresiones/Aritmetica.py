from Interprete.Abstract.NodoAST import NodoAST
from Interprete.Abstract.Instruccion import Instruccion
from Interprete.TS.Exception import Exception
from Interprete.TS.Tipo import Tipo, Operador_Aritmetico

class Aritmetica(Instruccion):
    def __init__(self, operador, OperacionIzq, OperacionDer, fila, columna):
        self.operador = operador
        self.OperacionIzq = OperacionIzq
        self.OperacionDer = OperacionDer
        self.fila = fila
        self.columna = columna
        self.tipo = None

    
    def interpretar(self, tree, table):
        izq = self.OperacionIzq.interpretar(tree, table)
        if isinstance(izq, Exception): return izq
        if self.OperacionDer != None:
            der = self.OperacionDer.interpretar(tree, table)
            if isinstance(der, Exception): return der


        if self.operador == Operador_Aritmetico.SUMA: # CUANDO TIENE UN SIGNO POSITIVO (+)
            # INT
            if self.OperacionIzq.tipo == Tipo.ENTERO and self.OperacionDer.tipo == Tipo.ENTERO:                         # int + int     = int
                self.tipo = Tipo.ENTERO
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + self.obtenerVal(self.OperacionDer.tipo, der) 
            elif self.OperacionIzq.tipo == Tipo.ENTERO and self.OperacionDer.tipo == Tipo.DECIMAL:                      # int + double  = double
                self.tipo = Tipo.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == Tipo.ENTERO and self.OperacionDer.tipo == Tipo.CADENA:                       # int + string  = string            
                self.tipo = Tipo.CADENA
                return str(self.obtenerVal(self.OperacionIzq.tipo, izq)) + self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == Tipo.ENTERO and self.OperacionDer.tipo == Tipo.BOOLEANO:                     # int + boolean  = string            
                self.tipo = Tipo.ENTERO
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + self.obtenerVal(self.OperacionDer.tipo, der)
            # DOUBLE
            elif self.OperacionIzq.tipo == Tipo.DECIMAL and self.OperacionDer.tipo == Tipo.ENTERO:                       # doube + int   = double
                self.tipo = Tipo.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + self.obtenerVal(self.OperacionDer.tipo, der) 
            elif self.OperacionIzq.tipo == Tipo.DECIMAL and self.OperacionDer.tipo == Tipo.DECIMAL:                      # double + double  = double
                self.tipo = Tipo.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == Tipo.DECIMAL and self.OperacionDer.tipo == Tipo.CADENA:                       # double + string  = string            
                self.tipo = Tipo.CADENA
                return str(self.obtenerVal(self.OperacionIzq.tipo, izq)) + self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == Tipo.DECIMAL and self.OperacionDer.tipo == Tipo.BOOLEANO:                     # double + boolean  = double            
                self.tipo = Tipo.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + self.obtenerVal(self.OperacionDer.tipo, der)
            # BOOLEAN
            elif self.OperacionIzq.tipo == Tipo.BOOLEANO and self.OperacionDer.tipo == Tipo.ENTERO:                      # boolean + int   = int
                self.tipo = Tipo.ENTERO
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + self.obtenerVal(self.OperacionDer.tipo, der) 
            elif self.OperacionIzq.tipo == Tipo.BOOLEANO and self.OperacionDer.tipo == Tipo.DECIMAL:                      # boolean + double  = double
                self.tipo = Tipo.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == Tipo.BOOLEANO and self.OperacionDer.tipo == Tipo.CADENA:                       # boolean + string  = string            
                self.tipo = Tipo.CADENA
                return str(self.obtenerVal(self.OperacionIzq.tipo, izq)) + self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == Tipo.BOOLEANO and self.OperacionDer.tipo == Tipo.BOOLEANO:                     # boolean + boolean  = int            
                self.tipo = Tipo.ENTERO
                return bool(self.obtenerVal(self.OperacionIzq.tipo, izq)) + bool(self.obtenerVal(self.OperacionDer.tipo, der))
            # CHAR
            elif self.OperacionIzq.tipo == Tipo.CHAR and self.OperacionDer.tipo == Tipo.CHAR:                       # char + char  = string            
                self.tipo = Tipo.CADENA
                return str(self.obtenerVal(self.OperacionIzq.tipo, izq)) + str(self.obtenerVal(self.OperacionDer.tipo, der))
            elif self.OperacionIzq.tipo == Tipo.CHAR and self.OperacionDer.tipo == Tipo.CHAR:                       # char + string  = string            
                self.tipo = Tipo.CADENA
                return bool(self.obtenerVal(self.OperacionIzq.tipo, izq)) + bool(self.obtenerVal(self.OperacionDer.tipo, der))
            # CADENA
            elif self.OperacionIzq.tipo == Tipo.CADENA and self.OperacionDer.tipo == Tipo.ENTERO:                       # string  + int   = string
                self.tipo = Tipo.CADENA
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + str(self.obtenerVal(self.OperacionDer.tipo, der)) 
            elif self.OperacionIzq.tipo == Tipo.CADENA and self.OperacionDer.tipo == Tipo.DECIMAL:                      # string + double  = double
                self.tipo = Tipo.CADENA
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + str(self.obtenerVal(self.OperacionDer.tipo, der))
            elif self.OperacionIzq.tipo == Tipo.CADENA and self.OperacionDer.tipo == Tipo.CADENA:                       # string + string  = string            
                self.tipo = Tipo.CADENA
                return str(self.obtenerVal(self.OperacionIzq.tipo, izq)) + str(self.obtenerVal(self.OperacionDer.tipo, der))
            elif self.OperacionIzq.tipo == Tipo.CADENA and self.OperacionDer.tipo == Tipo.BOOLEANO:                     # string + boolean  = string           
                self.tipo = Tipo.CADENA
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + str(self.obtenerVal(self.OperacionDer.tipo, der))
            elif self.OperacionIzq.tipo == Tipo.CADENA and self.OperacionDer.tipo == Tipo.CHAR:                         # string + char  = string           
                self.tipo = Tipo.CADENA
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + str(self.obtenerVal(self.OperacionDer.tipo, der))
            return Exception("Semantico", "Tipo Erroneo de operacion para +.", self.fila, self.columna)
            
        elif self.operador == Operador_Aritmetico.RESTA:

            if self.OperacionIzq.tipo == Tipo.ENTERO and self.OperacionDer.tipo == Tipo.ENTERO:                         # int - int     = int
                self.tipo = Tipo.ENTERO
                return self.obtenerVal(self.OperacionIzq.tipo, izq) - self.obtenerVal(self.OperacionDer.tipo, der) 
            elif self.OperacionIzq.tipo == Tipo.ENTERO and self.OperacionDer.tipo == Tipo.DECIMAL:                      # int - double  = double
                self.tipo = Tipo.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) - self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == Tipo.ENTERO and self.OperacionDer.tipo == Tipo.BOOLEANO:                     # int - boolean  = int            
                self.tipo = Tipo.ENTERO
                return self.obtenerVal(self.OperacionIzq.tipo, izq) - self.obtenerVal(self.OperacionDer.tipo, der)
            # DOUBLE
            elif self.OperacionIzq.tipo == Tipo.DECIMAL and self.OperacionDer.tipo == Tipo.ENTERO:                       # doube - int   = double
                self.tipo = Tipo.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) - self.obtenerVal(self.OperacionDer.tipo, der) 
            elif self.OperacionIzq.tipo == Tipo.DECIMAL and self.OperacionDer.tipo == Tipo.DECIMAL:                      # double - double  = double
                self.tipo = Tipo.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) - self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == Tipo.DECIMAL and self.OperacionDer.tipo == Tipo.BOOLEANO:                     # double - boolean  = double            
                self.tipo = Tipo.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) - self.obtenerVal(self.OperacionDer.tipo, der)
            # BOOLEAN
            elif self.OperacionIzq.tipo == Tipo.BOOLEANO and self.OperacionDer.tipo == Tipo.ENTERO:                      # boolean - int   = int
                self.tipo = Tipo.ENTERO
                return self.obtenerVal(self.OperacionIzq.tipo, izq) - self.obtenerVal(self.OperacionDer.tipo, der) 
            elif self.OperacionIzq.tipo == Tipo.BOOLEANO and self.OperacionDer.tipo == Tipo.DECIMAL:                      # boolean - double  = double
                self.tipo = Tipo.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) - self.obtenerVal(self.OperacionDer.tipo, der)
            
            return Exception("Semantico", "Tipo Erroneo de operacion para -.", self.fila, self.columna)

        elif self.operador == Operador_Aritmetico.POR:

            if self.OperacionIzq.tipo == Tipo.ENTERO and self.OperacionDer.tipo == Tipo.ENTERO:                         # int * int     = int
                self.tipo = Tipo.ENTERO
                return self.obtenerVal(self.OperacionIzq.tipo, izq) * self.obtenerVal(self.OperacionDer.tipo, der) 
            elif self.OperacionIzq.tipo == Tipo.ENTERO and self.OperacionDer.tipo == Tipo.DECIMAL:                      # int * double  = double
                self.tipo = Tipo.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) * self.obtenerVal(self.OperacionDer.tipo, der)
            # DOUBLE
            elif self.OperacionIzq.tipo == Tipo.DECIMAL and self.OperacionDer.tipo == Tipo.ENTERO:                       # doube * int   = double
                self.tipo = Tipo.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) * self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == Tipo.DECIMAL and self.OperacionDer.tipo == Tipo.DECIMAL:                      # double * double  = double
                self.tipo = Tipo.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) * self.obtenerVal(self.OperacionDer.tipo, der)
           
            return Exception("Semantico", "Tipo Erroneo de operacion para *.", self.fila, self.columna)

        elif self.operador == Operador_Aritmetico.DIV:

            if self.OperacionIzq.tipo == Tipo.ENTERO and self.OperacionDer.tipo == Tipo.ENTERO:                         # int / int     = double
                self.tipo = Tipo.DECIMAL
                if self.obtenerVal(self.OperacionDer.tipo, der) == 0:  
                    return Exception("Semantico", "Divisiones entre 0 no se puede", self.fila, self.columna)
                return self.obtenerVal(self.OperacionIzq.tipo, izq) / self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == Tipo.ENTERO and self.OperacionDer.tipo == Tipo.DECIMAL:                      # int / double  = double
                self.tipo = Tipo.DECIMAL
                if self.obtenerVal(self.OperacionDer.tipo, der) == 0:  
                    return Exception("Semantico", "Divisiones entre 0 no se puede", self.fila, self.columna)
                return self.obtenerVal(self.OperacionIzq.tipo, izq) / self.obtenerVal(self.OperacionDer.tipo, der)
            # DOUBLE
            elif self.OperacionIzq.tipo == Tipo.DECIMAL and self.OperacionDer.tipo == Tipo.ENTERO:                       # doube / int   = double
                self.tipo = Tipo.DECIMAL
                if self.obtenerVal(self.OperacionDer.tipo, der) == 0:  
                    return Exception("Semantico", "Divisiones entre 0 no se puede", self.fila, self.columna)
                return self.obtenerVal(self.OperacionIzq.tipo, izq) / self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == Tipo.DECIMAL and self.OperacionDer.tipo == Tipo.DECIMAL:                      # double / double  = double
                self.tipo = Tipo.DECIMAL
                if self.obtenerVal(self.OperacionDer.tipo, der) == 0:  
                    return Exception("Semantico", "Divisiones entre 0 no se puede", self.fila, self.columna)
                return self.obtenerVal(self.OperacionIzq.tipo, izq) / self.obtenerVal(self.OperacionDer.tipo, der)
           
            return Exception("Semantico", "Tipo Erroneo de operacion para /.", self.fila, self.columna)
        

        elif self.operador == Operador_Aritmetico.POTE:

            if self.OperacionIzq.tipo == Tipo.ENTERO and self.OperacionDer.tipo == Tipo.ENTERO:                         # int ** int     = int
                self.tipo = Tipo.ENTERO
                return self.obtenerVal(self.OperacionIzq.tipo, izq) ** self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == Tipo.ENTERO and self.OperacionDer.tipo == Tipo.DECIMAL:                      # int ** double  = double
                self.tipo = Tipo.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) ** self.obtenerVal(self.OperacionDer.tipo, der)
            # DOUBLE
            elif self.OperacionIzq.tipo == Tipo.DECIMAL and self.OperacionDer.tipo == Tipo.ENTERO:                       # doube ** int   = double
                self.tipo = Tipo.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) ** self.obtenerVal(self.OperacionDer.tipo, der) 
            elif self.OperacionIzq.tipo == Tipo.DECIMAL and self.OperacionDer.tipo == Tipo.DECIMAL:                      # double ** double  = double
                self.tipo = Tipo.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) ** self.obtenerVal(self.OperacionDer.tipo, der)
        
            
            return Exception("Semantico", "Tipo Erroneo de operacion para **.", self.fila, self.columna)

        elif self.operador == Operador_Aritmetico.MODU:

            if self.OperacionIzq.tipo == Tipo.ENTERO and self.OperacionDer.tipo == Tipo.ENTERO:                         # int % int     = double
                self.tipo = Tipo.DECIMAL
                if self.obtenerVal(self.OperacionDer.tipo, der) == 0:  
                    return Exception("Semantico", "Modular entre 0 no se puede", self.fila, self.columna)
                return self.obtenerVal(self.OperacionIzq.tipo, izq) % self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == Tipo.ENTERO and self.OperacionDer.tipo == Tipo.DECIMAL:                      # int % double  = double
                self.tipo = Tipo.DECIMAL
                if self.obtenerVal(self.OperacionDer.tipo, der) == 0:  
                    return Exception("Semantico", "Modular entre 0 no se puede", self.fila, self.columna)
                return self.obtenerVal(self.OperacionIzq.tipo, izq) % self.obtenerVal(self.OperacionDer.tipo, der)
            # DOUBLE
            elif self.OperacionIzq.tipo == Tipo.DECIMAL and self.OperacionDer.tipo == Tipo.ENTERO:                       # doube % int   = double
                self.tipo = Tipo.DECIMAL
                if self.obtenerVal(self.OperacionDer.tipo, der) == 0:  
                    return Exception("Semantico", "Modular entre 0 no se puede", self.fila, self.columna)
                return self.obtenerVal(self.OperacionIzq.tipo, izq) % self.obtenerVal(self.OperacionDer.tipo, der) 
            elif self.OperacionIzq.tipo == Tipo.DECIMAL and self.OperacionDer.tipo == Tipo.DECIMAL:                      # double % double  = double
                self.tipo = Tipo.DECIMAL
                if self.obtenerVal(self.OperacionDer.tipo, der) == 0:  
                    return Exception("Semantico", "Modular entre 0 no se puede", self.fila, self.columna)
                return self.obtenerVal(self.OperacionIzq.tipo, izq) % self.obtenerVal(self.OperacionDer.tipo, der)
         
              
            return Exception("Semantico", "Tipo Erroneo de operacion para %.", self.fila, self.columna)

        elif self.operador == Operador_Aritmetico.UMENOS: #NEGACION UNARIA
            
            if self.OperacionIzq.tipo == Tipo.ENTERO:
                self.tipo = Tipo.ENTERO
                return - self.obtenerVal(self.OperacionIzq.tipo, izq)
            elif self.OperacionIzq.tipo == Tipo.DECIMAL:
                self.tipo = Tipo.DECIMAL
                return - self.obtenerVal(self.OperacionIzq.tipo, izq)
            return Exception("Semantico", "Tipo Erroneo de operacion para - unario.", self.fila, self.columna)
        
        return Exception("Semantico", "Tipo de Operacion no Especificado.", self.fila, self.columna)

    def getNodo(self):
        nodo = NodoAST("ARITMETICA")
        if self.OperacionDer != None:
            nodo.agregarHijoNodo(self.OperacionIzq.getNodo())
            nodo.agregarHijo(str(self.operador))
            nodo.agregarHijoNodo(self.OperacionDer.getNodo())
        else:
            nodo.agregarHijo(str(self.operador))
            nodo.agregarHijoNodo(self.OperacionIzq.getNodo())
        
        return nodo

    def obtenerVal(self, tipo, val):
        if tipo == Tipo.ENTERO:
            return int(val)
        elif tipo == Tipo.DECIMAL:
            return float(val)
        elif tipo == Tipo.BOOLEANO:
            return bool(val)
        return str(val)
        
from enum import Enum

class Tipo(Enum):

    ENTERO      = 1  # int
    DECIMAL     = 2  # double 
    BOOLEANO    = 3  # Boolean
    CHAR        = 4  # char
    CADENA      = 5  # String
    NULO        = 6  # null
    ARREGLO     = 7  # []
    VAR         = 8  # var


class Operador_Aritmetico(Enum):

    SUMA        = 1  # suma (+)
    RESTA       = 2  # resta (-)
    POR         = 3  # multiplicacion (*)
    DIV         = 4  # division (/)
    POTE        = 5  # potencia (**)
    MODU        = 6  # modulo (%)
    UMENOS      = 7
    INCREMENTO  = 8  # ++
    DECREMENTO  = 9  # --

class Operador_Relacional(Enum):
    
    IGUALACION = 1  # (==)
    DIFERENCIA = 2  # (=!)
    MENORQUE   = 3  # (<)
    MAYORQUE   = 4  # (>)
    MENORIGUAL = 5  # (<=)
    MAYORIGUAL = 6  # (>=)


class Operador_Logico(Enum):
    
    OR  = 1  # (||)
    AND = 2  # (&&)
    NOT = 3  # (!)

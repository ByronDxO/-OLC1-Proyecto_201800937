from Interprete.TS.Tipo import Operador_Aritmetico, Tipo
from Interprete.Expresiones.Identificador import Identificador
from Interprete.TS.Exception import Exception
from Interprete.Abstract.Instruccion import Instruccion
from Interprete.TS.Simbolo import Simbolo


class IncrementoDecremento(Instruccion):

    def __init__(self, identificador, tipo, fila, columna):
        self.identificador = identificador
        self.tipo = tipo
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        if self.tipo == Operador_Aritmetico.INCREMENTO:
            simbolo = table.getTabla(self.identificador.lower())
            if simbolo.tipo == Tipo.ENTERO or simbolo.tipo == Tipo.DECIMAL:
                value = simbolo.valor + 1
                self.tipo = simbolo.tipo
        elif self.tipo == Operador_Aritmetico.DECREMENTO:
            simbolo = table.getTabla(self.identificador.lower())
            if simbolo.tipo == Tipo.ENTERO or simbolo.tipo == Tipo.DECIMAL:
                value = simbolo.valor - 1
                self.tipo = simbolo.tipo
        else:
            return Exception("Semantico", "Variable " + self.identificador + " Diferente tipo de dato.", self.fila, self.columna)

        simbolo_nuevo = Simbolo(self.identificador, self.tipo, self.fila, self.columna, value)
        result = table.actualizarTabla(simbolo_nuevo)
        

        if isinstance(result, Exception): return result
        return None


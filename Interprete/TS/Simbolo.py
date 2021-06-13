from Interprete.TS.Tipo import Tipo

class Simbolo():
    
    def __init__(self, id, tipo, fila, columna, valor):
        self.id = id
        self.tipo = tipo
        self.fila = fila
        self.columna = columna
        self.valor = valor
        # aqui podria ir una referencia self.ref


    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_tipo(self):
        return self.tipo

    def set_tipo(self, tipo):
        self.tipo = tipo

    def get_fila(self):
        return self.fila
    
    def set_fila(self, fila):
        self.fila = fila

    def get_columna(self):
        return self.columna

    def set_columna(self, columna):
        self.columna = columna
    
    def get_valor(self):
        return self.valor

    def set_valor(self, valor):
        self.valor = valor

    def __str__(self):
        return self.id + "-" + self.tipo + "-[" + self.fila + "," + self.columna +"]-" + self.valor
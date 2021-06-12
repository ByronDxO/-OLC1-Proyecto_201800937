'''
    AMBITO -> Es un entorno, es la parte del codigo donde pueden acceder las variables.
    AMBITO -> Determina en qué partes del programa una entidad puede ser usada.

    En la tabla de simbolos nos facilita usar un diccionario para poder ir encontrando las datos.

'''



from Interprete.TS.Exception import Exception


class TablaSimbolo:
    def __init__(self, anterior = None):
        self.tabla = {} # Diccionario Vacio
        self.anterior = anterior
        self.funciones = []

    def setTabla(self, simbolo):      # Agregar una variable
        if simbolo.id.lower() in self.tabla :
            return Exception("Semantico", "Variable " + simbolo.id + " ya existe", simbolo.fila, simbolo.columna)
        else:
            self.tabla[simbolo.id.lower()] = simbolo
            return None

    def getTabla(self, id):            # obtener una variable
        tablaActual = self
        while tablaActual.tabla != None:
            if id in tablaActual.tabla :
                return tablaActual.tabla[id]
            else:
                tablaActual = tablaActual.anterior
        return None

    def actualizarTabla(self, simbolo):
        tablaActual = self
        while tablaActual != None:
            if simbolo.id in tablaActual.tabla :
                if tablaActual.tabla[simbolo.id].getTipo() == simbolo.getTipo():
                    tablaActual.tabla[simbolo.id].setValor(simbolo.getValor())
                    tablaActual.tabla[simbolo.id].setTipo(simbolo.getTipo())
                    return None 
                
                return Exception("Semantico", "Tipo de dato Diferente en Asignacion", simbolo.getFila(), simbolo.getColumna()) 
            else:
                tablaActual = tablaActual.anterior
        return Exception("Semantico", "Variable No encontrada en Asignacion", simbolo.getFila(), simbolo.getColumna())
        
        
    

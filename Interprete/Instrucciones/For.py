from Interprete.Instrucciones.IncrementoDecremento import IncrementoDecremento
from Interprete.Instrucciones.Declaracion import Declaracion
from Interprete.Instrucciones.Asignacion import Asignacion
from Interprete.Abstract.Instruccion import Instruccion
from Interprete.TS.Exception import Exception
from Interprete.TS.Tipo import Tipo
from Interprete.TS.TablaSimbolo import TablaSimbolo
from Interprete.Instrucciones.Break import Break

class For(Instruccion):
    def __init__(self, variable, condicion, actualizacion, instrucciones,  fila, columna):
        self.variable = variable
        self.condicion = condicion
        self.instrucciones = instrucciones
        self.actualizacion = actualizacion
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        # print(self.variable.identificador) # variable declarada o asignada
        
        if isinstance(self.variable, Declaracion): tabla_nueva = TablaSimbolo(table) 
        elif isinstance(self.variable, Asignacion): tabla_nueva = table
        else:  return Exception("Semantico", "No hay declaracion o asignacion.", self.fila, self.columna)
        
        declaracion = self.variable.interpretar(tree, tabla_nueva)
        if isinstance(declaracion, Exception): return declaracion

        while True:

            condicion = self.condicion.interpretar(tree, tabla_nueva)
            if isinstance(condicion, Exception): return condicion

            if self.condicion.tipo == Tipo.BOOLEANO:

                if bool(condicion) == True:   # VERIFICA SI ES VERDADERA LA CONDICION
                    
                    nuevaTabla = TablaSimbolo(tabla_nueva)       #NUEVO ENTORNO
                    for instruccion in self.instrucciones:
                        result = instruccion.interpretar(tree, nuevaTabla) #EJECUTA INSTRUCCION ADENTRO DEL IF
                        if isinstance(result, Exception) :
                            tree.get_excepcion().append(result)
                            tree.update_consola(result.__str__())
                        if isinstance(result, Break): return None
                    
                    update = self.actualizacion.interpretar(tree, nuevaTabla)
                    if isinstance(update, Exception): return update
                else:
                    break
            else:
                return Exception("Semantico", "Tipo de dato no booleano en IF.", self.fila, self.columna)
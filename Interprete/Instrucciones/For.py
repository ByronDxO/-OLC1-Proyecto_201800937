from Interprete.Instrucciones.IncrementoDecremento import IncrementoDecremento
from Interprete.Instrucciones.Declaracion import Declaracion
from Interprete.Instrucciones.Asignacion import Asignacion
from Interprete.Abstract.Instruccion import Instruccion
from Interprete.TS.Exception import Exception
from Interprete.TS.Tipo import Tipo
from Interprete.TS.TablaSimbolo import TablaSimbolo
from Interprete.Instrucciones.Break import Break
from Interprete.Instrucciones.Return import Return
from Interprete.Instrucciones.Continue import Continue
from Interprete.Abstract.NodoAST import NodoAST

class For(Instruccion):
    def __init__(self, variable, condicion, actualizacion, instrucciones,  fila, columna):
        self.variable = variable
        self.condicion = condicion
        self.instrucciones = instrucciones
        self.actualizacion = actualizacion
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        
        tabla_nueva = TablaSimbolo(table) # Inicia el primer Ambito.
        declaracion = self.variable.interpretar(tree, tabla_nueva)
        if isinstance(declaracion, Exception): return declaracion

        while True:

            condicion = self.condicion.interpretar(tree, tabla_nueva)
            if isinstance(condicion, Exception): return condicion

            if self.condicion.tipo == Tipo.BOOLEANO: # Aqui verifica si la condicion es una expresion logica, sino lanza una Exception.

                if bool(condicion) == True:  # Si cumple la condicion se Ejecuta y si no se sale.
                    
                    nuevaTabla = TablaSimbolo(tabla_nueva)       # Inicia el segundo ambito.
                    for instruccion in self.instrucciones:       # Inicia ejecutando las instrucciones adentro del For.
                        result = instruccion.interpretar(tree, nuevaTabla) 
                        if isinstance(result, Exception) :
                            tree.get_excepcion().append(result)
                            tree.update_consola(result.__str__())
                        if isinstance(result, Break): return None
                        if isinstance(result, Return): return result
                        if isinstance(result, Continue): break
                    
                    update = self.actualizacion.interpretar(tree, nuevaTabla) # Aqui hace la actualizacion de un incremeno, decremento o asignacion.
                    if isinstance(update, Exception): return update

                else:
                    break
            else:
                return Exception("Semantico", "Tipo de dato no booleano en For.", self.fila, self.columna)


    def getNodo(self):
        nodo = NodoAST("FOR")
        nodo.agregarHijoNodo(self.variable.getNodo())
        nodo.agregarHijoNodo(self.condicion.getNodo())
        instrucciones = NodoAST("INSTRUCCIONES")
        for instruccion in self.instrucciones:
            instrucciones.agregarHijoNodo(instruccion.getNodo())
        nodo.agregarHijoNodo(instrucciones)

        nodo.agregarHijoNodo(self.actualizacion.getNodo())
        return nodo
import Ejercicio1
import pandas as pd
import numpy as np
df = pd.read_csv('pokemon.csv')
print(df)


class pokemon():
    def __init__(self, nombre, tipo1, tipo2, numero):
        self.numero = numero
        self.nombre = nombre
        self.tipo1 = tipo1
        self.tipo2 = tipo2

pokem = pokemon(None, None, None, None)
arbol_pokemon = Ejercicio1.nodoArbol(pokem)

def crear_pok(fila):
    pokem = pokemon(fila['Name'], fila['Type 1'], fila['Type 2'], fila['#'])
    return pokem

for i in range(len(df)):
    pok = crear_pok(df.iloc[i])
    arbol_pokemon.insertar_nodo(pok)

arbol_pokemon.inorden()
import arbol_pokemon
import pandas as pd
import numpy as np
df = pd.read_csv('pokemon.csv')
print(df)


class pokemon():
    def __init__(self, nombre, tipo1, tipo2, numero, clave):
        self.clave = clave
        self.numero = numero
        self.nombre = nombre
        self.tipo1 = tipo1
        self.tipo2 = tipo2




def crear_pok(fila):
    pokem = pokemon(fila['Name'], fila['Type 1'], fila['Type 2'], fila['#'], fila['#'])
    return pokem

def cargar_arbol():
    arboll = None
    for i in range(len(df)):
        pok = crear_pok(df.iloc[i])
        print(pok.nombre)
        arboll.insertar_nodo(pok)

cargar_arbol()
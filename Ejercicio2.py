import arbol_pokemon
import pandas as pd
import numpy as np
df = pd.read_csv('pokemon.csv')
print(df)


class pokemon():
    '''
    clase pokemon, que va a ser la informacion del nodo en el árbol
    '''
    def __init__(self, nombre, tipo1, tipo2, numero, clave):
        self.clave = clave
        self.numero = numero
        self.nombre = nombre
        self.tipo1 = tipo1
        self.tipo2 = tipo2


def crear_pok(fila, filtro):
    '''
    funcion que nos crea un objeto llamado pokemon, con un filtro para crear los árboles
    '''
    pokem = pokemon(fila['Name'], fila['Type 1'], fila['Type 2'], fila['#'], fila[filtro])
    return pokem

def cargar_arbol(filtro):
    '''
    funcion que crea el árbol dependiendo del atributo filtro del pokemon
    '''
    arboll = arbol_pokemon.nodoArbol(None)
    for i in range(len(df)):
        pok = crear_pok(df.iloc[i], filtro)
        arboll.insertar_nodo(pok)

#creamos los árboles por los tres parámetros
cargar_arbol('#')
cargar_arbol('Name')
cargar_arbol('Type 1')
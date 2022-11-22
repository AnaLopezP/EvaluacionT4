import arbol_pokemon
import pandas as pd
import numpy as np
'''class pokemon():
    '''
    #clase pokemon, que va a ser la informacion del nodo en el árbol
'''
    def __init__(self, nombre, tipo1, tipo2, numero, clave):
        self.clave = clave
        self.numero = numero
        self.nombre = nombre
        self.tipo1 = tipo1
        self.tipo2 = tipo2



def crear_pok(fila, filtro):
    '''
    #funcion que nos crea un objeto llamado pokemon, con un filtro para crear los árboles
'''
    pokem = pokemon(fila['Name'], fila['Type 1'], fila['Type 2'], fila['#'], fila[filtro])
    return pokem

def cargar_arbol(filtro):
    '''
    #funcion que crea el árbol dependiendo del atributo filtro del pokemon
'''
    pokemon_raiz = pokemon('Bulbasaur', 'Grass', 'Poison', 1, df.iloc[0])
    arboll = arbol_pokemon.nodoArbol(pokemon_raiz)
    for i in range(1, 800):
        pok = crear_pok(df.iloc[i], filtro)
        print(pok)
        arboll.insertar_nodo(pok)
        print(arboll)
    return arboll

#creamos los árboles por los tres parámetros
a1_numero = cargar_arbol('#')
a2_nombre = cargar_arbol('Name')
a3_tipo = cargar_arbol('Type 1')'''



df = pd.read_csv('pokemon.csv')
print(df)

lista = []
for i in df.iloc:
    dicc = {}
    dicc['Nombre'] = i['Name']
    dicc['Tipo 1'] = i['Type 1']
    dicc['Tipo 2'] = i['Type 2']
    dicc['Numero'] = i['#']
    lista.append(dicc)

#print(lista)

'''a1_numero = arbol_pokemon.nodoArbol(lista[0])
print(a1_numero.info)
print(a1_numero.info['Nombre'])
for i in range(1, 800):
    a1_numero.insertar_nodo(lista[i], 'Numero')'''

def crear_arbol(raiz, filtro):
    for i in range(1, 800):
        raiz.insertar_nodo(lista[i], filtro)
    return raiz


a1_numero = arbol_pokemon.nodoArbol(lista[0])
a2_nombre = arbol_pokemon.nodoArbol(lista[0])
a3_tipo = arbol_pokemon.nodoArbol(lista[0])
crear_arbol(a1_numero, 'Numero')
crear_arbol(a2_nombre, 'Nombre')
crear_arbol(a3_tipo, 'Tipo 1')

numero_2 = []
a1_numero.buscar_xnumero(2, numero_2)
print(numero_2)

nombre = []
a2_nombre.buscar_bien('h', nombre)
print(nombre)
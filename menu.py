import Ejercicio1
import Ejercicio2
import arbol_pokemon
import helpers
from operator import itemgetter
import pandas as pd

def iniciar():
    while True:
        helpers.limpiar_pantalla()

        print("QUE EJERCICIO QUIERES VER:")
        print("[1] Ejercicio 1: Huffman")
        print("[2] Ejercicio 2: Pokemon")
        print("[3] Ejercicio 3")
        print("[4] Ninguno")

        decision = int(input("> "))
        if decision == 1:
            frecuencias =  {'A': 0.2, 
                'F': 0.17,
                '1': 0.13,
                '3': 0.21,
                '0': 0.05,
                'M': 0.09,
                'T': 0.15}

    
            lista = []
            frecuencias = sorted(frecuencias.items(), key= itemgetter(1))
            frecuencias = dict(frecuencias)
            for i in frecuencias:
                dato = Ejercicio1.info(i, frecuencias[i])
                raiz = Ejercicio1.nodoArbol(dato)
                lista.append(raiz)
            #print(lista)
            lista = sorted(lista)

            while len(lista) > 1:
                ArbolAux1 = lista.pop(0)
                ArbolAux2 = lista.pop(0)
                datoaux = Ejercicio1.info(None, ArbolAux1.info.frecuencia+ArbolAux2.info.frecuencia)
                ArbolNuevo = Ejercicio1.nodoArbol(datoaux)
                ArbolNuevo.izq = ArbolAux1
                ArbolNuevo.der = ArbolAux2
                lista.append(ArbolNuevo)
                lista = sorted(lista)

            '''for i in range(len(lista)):
                print(lista[i])'''

            ArbolFinal = lista.pop()
            #nodoArbol.inorden(ArbolFinal)  
            asociados = {}
            letras = ['A', 'F', '1', '3', '0', 'M', 'T']
            for i in range(len(letras)):
                numeros = []
                x, y = Ejercicio1.nodoArbol.camino(ArbolFinal, letras[i], False, numeros)
                asociados[letras[i]] = y
            #print(asociados)
            mensaje_encriptado = []
            mensaje = input('Introduzca un mensaje a encriptar, con los caracteres A, F, 1, 3, 0, M, T: ')
            for i in mensaje:
                if i in asociados:
                    mensaje_encriptado.append(asociados[i])
            print('MENSAJE ENCRIPTADO:')
            print(mensaje_encriptado)
            cod = []
            desencriptacion = Ejercicio1.desencriptar(mensaje_encriptado, asociados, cod)
            print('MENSAJE DESENCRIPTADO:')
            print(desencriptacion)

        if decision == 2:
            df = pd.read_csv('pokemon.csv')
            lista = []
            for i in df.iloc:
                dicc = {}
                dicc['Nombre'] = i['Name']
                dicc['Tipo 1'] = i['Type 1']
                dicc['Tipo 2'] = i['Type 2']
                dicc['Numero'] = i['#']
                lista.append(dicc)
            a1_numero = arbol_pokemon.nodoArbol(lista[0])
            a2_nombre = arbol_pokemon.nodoArbol(lista[0])
            a3_tipo = arbol_pokemon.nodoArbol(lista[0])
            Ejercicio2.crear_arbol(a1_numero, 'Numero', lista)
            Ejercicio2.crear_arbol(a2_nombre, 'Nombre', lista)
            Ejercicio2.crear_arbol(a3_tipo, 'Tipo 1', lista)

            numero_2 = []
            a1_numero.buscar_xnumero(2, numero_2)

            nombre = []
            a2_nombre.buscar_bien('h', nombre)

            tipo_fuego = []
            a3_tipo.buscar_xtipo('Fire', tipo_fuego)
            print('-----------------------POKEMONS TIPO FUEGO---------------------------')
            print(tipo_fuego)

            tipo_electro = []
            a3_tipo.buscar_xtipo('Electric', tipo_electro)
            print('-------------------POKEMONS TIPO ELECTRO---------------------')
            print(tipo_electro)

            tipo_agua = []
            a3_tipo.buscar_xtipo('Water', tipo_agua)
            print('-------------------POKEMONS TIPO AGUA---------------------')
            print(tipo_agua)

            tipo_planta = []
            a3_tipo.buscar_xtipo('Grass', tipo_planta)
            print('-------------------POKEMONS TIPO PLANTA---------------------')
            print(tipo_planta)

            print('Los pokemons que son débiles a Jolteon son aquellos de tipo: agua y volador')
            print('\n')
            deb_jolteon = []
            a3_tipo.buscar_xtipo('Water', deb_jolteon)
            a3_tipo.buscar_xtipo('Flying', deb_jolteon)
            print(deb_jolteon)
            print('\n')
            print('Los pokemons débiles a Lycanroc son los de tipo: Bicho, fuego, hielo y volador')
            print('\n')
            deb_lycanroc = []
            a3_tipo.buscar_xtipo('Bug', deb_lycanroc)
            a3_tipo.buscar_xtipo('Fire', deb_lycanroc)
            a3_tipo.buscar_xtipo('Ice', deb_lycanroc)
            a3_tipo.buscar_xtipo('Flying', deb_lycanroc)
            print(deb_lycanroc)
            print('\n')
            print('Como Tyrantrum es de tipo roca y dragón, es fuerte contra los mismos que Lycanroc más los que son débiles contra tipo dragón, que es el tipo dragón')
            print('\n')
            deb_tyrantrum = deb_lycanroc
            a3_tipo.buscar_xtipo('Dragon', deb_tyrantrum)
            print(deb_tyrantrum)
            print('\n')
            tipos = []
            a3_tipo.tipos(tipos)
            print('--------------------TIPOS DE POKEMONS---------------------')
            print(tipos)

            for i in tipos:
                todos = []
                a3_tipo.buscar_xtipo(i, todos)
                print('\n')
                print('NUMERO DE POKEMONS TIPO: ' + str(i))
                print(len(todos))

            print('-----------------------------POKEMONS ORDENADOS POR NUMERO DE MANERA ASCENDENTE--------------------------')
            listanum = []
            a1_numero.ordenascendente(listanum)
            for i in range(0, 5):
               print(listanum[i])
            print('\n')
            print('---------------------------POKEMONS ORDENADOS POR NOMBRE ASCENDENTE------------------------------')
            listanombre = []
            a2_nombre.ordenascendente(listanombre)
            for i in range(0, 5):
                print(listanombre[i])

            print('\n')
            print('---------------------------------POKEMONS ORDENADOS POR NIVEL POR NOMBRE----------------------')
            nombrenivel = []
            a2_nombre.por_nivel(nombrenivel)
            for i in range(0, 5):
                print(nombrenivel[i])

        if decision == 3:
            print('En proceso...')

        if decision == 4:
            print('Saliendo')
            break

        input("\nPresiona ENTER  para continuar")
iniciar()
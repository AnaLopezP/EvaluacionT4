import Ejercicio1
import Ejercicio2
import helpers
from operator import itemgetter

def iniciar():
    while True:
        helpers.limpiar_pantalla()

        print("QUE EJERCICIO QUIERES VER:")
        print("[1] Ejercicio 1")
        print("[2] Ejercicio 2")
        print("[3] Ejercicio 3")
        print("[4] Ninguno")

        decision = int(input("> "))
        if decision == "1":
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
            l = []
            x, y = Ejercicio1.nodoArbol.camino(ArbolFinal, 'A', False, l)
            print(x, y)
            print(y)
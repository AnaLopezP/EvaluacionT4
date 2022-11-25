import random

class nodoVertice:
    def __init__(self):
        '''
        crea un nodo vértice con la información cargada
        '''
        self.maravilla = None
        self.sig = None
        self.visitado = False
        self.adyacentes = None
    
    def insertarMaravilla(self, mar):
        '''
        insertamos un objeto maravilla de la clase maravilla
        '''
        self.maravilla = maravilla(mar.nombre, mar.pais, mar.tipo)

    def insertarAdyacente(self, maravilla, distancia):
        nodo = Adyacente(maravilla,distancia)
        if self.adyacentes == None:
            self.adyacentes = nodo #si el vertice no tiene ningun adyacente, lo ponemos y listo
        else: 
            #si ya hay adyacentes, incrustamos el nuevo al principio de la lista y desplazamos los demas
            adyacenteAux = self.adyacentes
            self.adyacentes = nodo
            self.adyacentes.sig = adyacenteAux

    '''Estas funciones las ponemos en esta clase y no en la clase de adyacentes porque añadimos adyacentes AL VERTICE'''

class maravilla:
    def __init__(self, nombre, pais, tipo):
        self.nombre = nombre
        self.pais = pais
        self.tipo = tipo


class Adyacente:
    def __init__(self, info, distancia):
        self.maravilla = info
        self.sig = None
        self.distancia = distancia

class Grafo:
    def __init__(self):
        '''
        crea un grafo vacío
        '''
        self.inicio = None
        self.tamaño = 0
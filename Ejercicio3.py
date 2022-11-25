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

class maravilla:
    def __init__(self, nombre, pais, tipo):
        self.nombre = nombre
        self.pais = pais
        self.tipo = tipo


class Adyacente :
    def __init__(self, info, distancia):
        self.maravilla = info
        self.sig = None
        self.distancia = distancia
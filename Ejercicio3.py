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


class maravilla:
    def __init__(self, nombre, pais, tipo):
        self.nombre = nombre
        self.pais = pais
        self.tipo = tipo
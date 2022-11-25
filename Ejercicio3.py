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

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

    def __str__(self):
        return str(self.maravilla.nombre)+ ' ' + str(self.maravilla.tipo) + ' ' + str(self.maravilla.pais) + ' vertices adyacentes: ' + str(cadena) 

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

    def insertar(self, dato):
        '''
        inserta vertices con un dato de una maravilla al grafo
        '''
        nodo = nodoVertice()
        nodo.insertarMaravilla(dato.maravilla)
        if self.inicio is None:
            self.inicio = nodo
        else:
            GrafoAux = self.inicio
            self.inicio = nodo
            self.inicio.sig = GrafoAux
            self.tamaño += 1
            #sigue la misma logica que la funcion insertar adyacentes, pero con los vértices del grafo
        
    def pintar(self):
        vertice = self.inicio
        while vertice is not None:
            if not vertice.visitado:
                print(str(vertice))
                vertice = vertice.sig

#CODIGO
m1 = maravilla('MurallaChina', ['China'], 'ARQ')
m2 = maravilla('Petra', ['Jordania'], 'ARQ')
m3 = maravilla("Coliseo",["Italia"],"ARQ")
m4 = maravilla("ChichenItza",["Mexico"],"ARQ")
m5 = maravilla("Grancañon",["EEUU"],"NAT")
m6 = maravilla("CristoRedentor",["Brasil"],"ARQ")
m7 = maravilla("TajMahal",["India"],"ARQ")

v1 = nodoVertice()
v1.insertarMaravilla(m1)
print("MARAVILLA 1 EN EL VERTITE 1: "+ v1.maravilla.nombre)
v2 = nodoVertice()
v2.insertarMaravilla(m2)
v3 = nodoVertice()
v3.insertarMaravilla(m3)
v4 = nodoVertice()
v4.insertarMaravilla(m4)
v5 = nodoVertice()
v5.insertarMaravilla(m5)
v6 = nodoVertice()
v6.insertarMaravilla(m6)
v7 = nodoVertice()
v7.insertarMaravilla(m7)

grafo = Grafo()
grafo.insertar(v1)
grafo.insertar(v2)
grafo.insertar(v3)
grafo.insertar(v4)
grafo.insertar(v5)
grafo.insertar(v6)
grafo.insertar(v7)

grafo.pintar()


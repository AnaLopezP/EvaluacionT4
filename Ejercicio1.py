from operator import itemgetter

class nodoArbol(object):
    def __init__(self, info):
        self.izq = None
        self.der = None
        self.info = info

    def __gt__(self, nodoArbol):
        return self.info.frecuencia> nodoArbol.info.frecuencia

    def __str__(self):
        return "Letra: " + str(self.info.simbolo) + " Frecuencia: " + str(self.info.frecuencia)

    def eliminar_nodo(raiz, clave):
        x = None
        if raiz is not None:
            if clave < raiz.info:
                raiz.izq, x = nodoArbol.eliminar_nodo(raiz.izq, clave)
            elif clave > raiz.info:
                raiz.der, x = nodoArbol.eliminar_nodo(raiz.der, clave)
            else:
                x = raiz.info
                if raiz.izq is None:
                    raiz = raiz.der
                elif raiz.der is None:
                    raiz = raiz.izq
                else:
                    raiz.izq, aux = nodoArbol.remplazar(raiz.izq)
                    raiz.info = aux.info
        return raiz, x

    def insertar_nodo(raiz, dato):
        if raiz is None:
            raiz = nodoArbol(dato)
        elif dato < raiz.info:
            raiz.izq = nodoArbol.insertar_nodo(raiz.izq, dato)
        else:
            raiz.der = nodoArbol.insertar_nodo(raiz.der, dato)
        return raiz

    def arbol_vacio(raiz):
        return raiz is None

    def remplazar(raiz):
        aux = None
        if raiz.der is None:
            aux = raiz
            raiz = raiz.izq
        else:
            raiz.der, aux = nodoArbol.remplazar(raiz.der)
        return raiz, aux

    def buscar(raiz, clave):
        pos = None
        if raiz is not None:
            if raiz.info == clave:
                pos = raiz
            elif clave < raiz.info:
                pos = nodoArbol.buscar(raiz.izq, clave)
            else:
                pos = nodoArbol.buscar(raiz.der, clave)
        return pos

    def inorden(raiz):
        if raiz is not None:
            nodoArbol.inorden(raiz.izq)
            print(raiz.info)
            nodoArbol.inorden(raiz.der)

    def preorden(raiz):
        if raiz is not None:
            print(raiz.info)
            nodoArbol.preorden(raiz.izq)
            nodoArbol.preorden(raiz.der)

    def postorden(raiz):
        if raiz is not None:
            nodoArbol.postorden(raiz.der)
            print(raiz.info)
            nodoArbol.postorden(raiz.izq)

    def camino(raiz, clave, encontrado, cadena):
        if not encontrado:
            if raiz is not None:
                if raiz.der == None and raiz.izq == None:
                    print('He llegado a una hoja: ' + str(raiz.info))
                    if str(raiz.info.simbolo) == clave:
                        print('La he encontrado: ' + str(raiz.info.simbolo))
                        encontrado = True
                        print(cadena) 
                    
                else:
                    cadena.append('0')
                    encontrado, cadena = nodoArbol.camino(raiz.izq, clave, encontrado, cadena)
                    cadena.append('1')
                    encontrado, cadena = nodoArbol.camino(raiz.der, clave, encontrado, cadena)
                    
          
        return encontrado, cadena


class info():
    def __init__(self, simbolo, frecuencia):
        self.simbolo = simbolo
        self.frecuencia = frecuencia
    def __str__(self):
        return "Letra: " + str(self.simbolo) + " Frecuencia: " + str(self.frecuencia)

    

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
    dato = info(i, frecuencias[i])
    raiz = nodoArbol(dato)
    lista.append(raiz)
#print(lista)
lista = sorted(lista)

while len(lista) > 1:
    ArbolAux1 = lista.pop(0)
    ArbolAux2 = lista.pop(0)
    datoaux = info(None, ArbolAux1.info.frecuencia+ArbolAux2.info.frecuencia)
    ArbolNuevo = nodoArbol(datoaux)
    ArbolNuevo.izq = ArbolAux1
    ArbolNuevo.der = ArbolAux2
    lista.append(ArbolNuevo)
    lista = sorted(lista)

'''for i in range(len(lista)):
    print(lista[i])'''

ArbolFinal = lista.pop()
#nodoArbol.inorden(ArbolFinal)   

x, y =nodoArbol.camino(ArbolFinal, 'T', False, [])
print(x, y)

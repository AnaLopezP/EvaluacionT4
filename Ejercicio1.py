class nodoArbol(object):
    def __init__(self, info):
        self.izq = None
        self.der = None
        self.info = info
    
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
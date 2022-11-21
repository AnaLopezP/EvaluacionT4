class nodoArbol(object):
    def __init__(self, info):
        self.izq= None
        self.der = None
        self.info = info
        
    def eliminar_nodo(raiz, clave):
        '''
        Elimina el elemento del árbol y lo devuelve si lo encuentra
        
        '''
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
    
    def insertar_nodo(raiz, dato, filtro):
        '''
        Insertamos el nodo en el árbol
        '''
        if raiz is None:
            raiz = nodoArbol(dato)                        
        elif dato[filtro] < raiz.info[filtro]:
            raiz.izq = nodoArbol.insertar_nodo(raiz.izq, dato, filtro)
        else:
            raiz.der = nodoArbol.insertar_nodo(raiz.der, dato, filtro)
        return raiz
    
    def arbolvacio(raiz):
        '''
        Devuelve True si el árbol está vacío
        '''
        return raiz is None
    
    def remplazar (raiz):
        '''
        Determina el nodo que remplazará al que se elimina
        '''
        aux = None
        if raiz.der is None:
            aux = raiz
            raiz = raiz.izq
        else:
            raiz.der, aux = nodoArbol.remplazar(raiz.der)
        return raiz, aux
    
    
    def buscar(raiz, clave):
        '''
        Devuelve la dirección del nodo buscado
        '''
        pos = None
        if raiz is not None:
            if raiz.info == clave:
                pos = raiz
            elif clave < raiz.info:
                pos = nodoArbol.buscar(raiz.izq, clave)
            else:
                pos = nodoArbol.buscar(raiz.der, clave)
        return pos
                
    def buscar_bien(raiz, caracter):
        if caracter in raiz.info['Nombre']:
            print(raiz.info['Nombre'])
            nodoArbol.buscar_bien(raiz.izq, caracter)
            nodoArbol.buscar_bien(raiz.der, caracter)
        else:
            nodoArbol.buscar_bien(raiz.izq, caracter)
            nodoArbol.buscar_bien(raiz.der, caracter)
    
    def inorden(raiz):
        '''
        Hace el barrido inorden del árbol
        '''
        if raiz is not None:
            nodoArbol.inorden(raiz.izq)
            print(raiz.info)
            nodoArbol.inorden(raiz.der)
    
    def preorden(raiz):
        '''
        Realiza el barrido preorden del árbol
        '''
        if raiz is not None:
            print(raiz.info)    
            nodoArbol.preorden(raiz.izq)
            nodoArbol.preorden(raiz.der)
    
    def postorden(raiz):
        '''
        Realiza el barrido postorden del árbol
        '''
        if raiz is not None:
            nodoArbol.postorden(raiz.der)
            print(raiz.info)
            nodoArbol.postorden(raiz.izq)
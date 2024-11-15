import heapq
from .models import City, Route

def dijkstra(start_city):
    ciudades = City.objects.all()
    distances = {ciudad: float('inf') for ciudad in ciudades}
    distances[start_city] = 0
    previous_cities = {ciudad: None for ciudad in ciudades}
    
    visitar = []
    heapq.heappush(visitar, (0, start_city))

    while visitar != []:
        distancia_actual, ciudad_actual = heapq.heappop(visitar)

        if distancia_actual > distances[ciudad_actual]:
            continue

        rutas = Route.objects.filter(start_city=ciudad_actual)

        for ruta in rutas:
            vecino = ruta.end_city
            nueva_distancia = distancia_actual + ruta.distance

            if nueva_distancia < distances[vecino]:
                distances[vecino] = nueva_distancia
                previous_cities[vecino] = ciudad_actual
                heapq.heappush(visitar, (nueva_distancia, vecino))

    return distances, previous_cities

def get_shortest_path(start_city, end_city):
    distances, previous_cities = dijkstra(start_city)
    path = []
    city = end_city

    while previous_cities[city]:
        path.insert(0, city)
        city = previous_cities[city]
    path.insert(0, city)

    return path, distances[end_city]

class ArbolBinarioBusqueda: # Define la clase para representar un Árbol Binario de Búsqueda.

    def __init__(self):  # Es el constructor de la clase, se llama al crear una instancia de ArbolBinarioBusqueda.
        self.raiz = None # Inicializa el atributo "raiz" como None, indicando que el árbol comienza vacío.
        self.tamano = 0  # Inicializa el atributo "tamano" en 0, que representa el número de nodos en el árbol.

    def agregar(self,clave,valor): # Define el método para agregar un nuevo nodo con una clave y un valor al árbol.
        if self.raiz: # Verifica si el árbol ya tiene una raíz.
            self._agregar(clave,valor,self.raiz) # Si hay raíz, llama al método _agregar para buscar el lugar adecuado a partir de la raíz.
        else:  # Si el árbol está vacío (sin raíz)...
            self.raiz = NodoArbol(clave,valor) # Crea un nuevo nodo y lo establece como la raíz del árbol.
        self.tamano = self.tamano + 1 # Incrementa el tamaño del árbol en 1, ya que se ha agregado un nuevo nodo.

    def _agregar(self,clave,valor,nodoActual):  # Método privado para agregar un nodo en la posición correcta del árbol.
        if clave < nodoActual.clave: # Si la clave del nuevo nodo es menor que la clave del nodo actual...
            if nodoActual.tieneHijoIzquierdo(): # Verifica si el nodo actual tiene un hijo izquierdo.
                self._agregar(clave,valor,nodoActual.hijoIzquierdo)# Llama recursivamente a _agregar en el hijo izquierdo.
            else: # Si no hay hijo izquierdo...
                nodoActual.hijoIzquierdo = NodoArbol(clave,valor,padre=nodoActual)  # Crea un nuevo nodo como hijo izquierdo.
        else: # Si la clave del nuevo nodo es mayor o igual que la clave del nodo actual...
            if nodoActual.tieneHijoDerecho():  # Verifica si el nodo actual tiene un hijo derecho.
                self._agregar(clave,valor,nodoActual.hijoDerecho)# Llama recursivamente a _agregar en el hijo derecho.
            else: # Si no hay hijo derecho...
                nodoActual.hijoDerecho = NodoArbol(clave,valor,padre=nodoActual) # Crea un nuevo nodo como hijo derecho.

    def __setitem__(self,c,v): # Método para permitir el uso de la sintaxis de asignación con corchetes (similar a un diccionario).
        self.agregar(c,v) # Llama al método "agregar" para insertar el par clave-valor en el árbol.

    def obtener(self,clave): # Método para obtener el valor asociado a una clave específica en el árbol.
        if self.raiz:# Verifica si el árbol tiene una raíz (es decir, si no está vacío).
            res = self._obtener(clave,self.raiz) # Llama al método privado _obtener para buscar la clave a partir de la raíz.
            if res:  # Si _obtener devuelve un nodo (clave encontrada)...
                return res.cargaUtil # Retorna el valor (carga útil) asociado a la clave encontrada.
            else: # Si _obtener devuelve None (clave no encontrada)...
                return None  # Retorna None indicando que la clave no se encuentra en el árbol.
        else:   # Si el árbol está vacío (sin raíz)...
            return None # Retorna None porque no hay elementos en el árbol.

    def _obtener(self,clave,nodoActual): # Método privado para buscar un nodo con la clave especificada, comenzando desde nodoActual.
        if not nodoActual: # Si nodoActual es None (nodo inexistente), significa que la clave no está en el árbol.
            return None # Retorna None indicando que la clave no se encuentra.
        elif nodoActual.clave == clave: # Si la clave del nodo actual coincide con la clave buscada...
            return nodoActual # Retorna el nodo actual, ya que es el nodo buscado.
        elif clave < nodoActual.clave: # Si la clave buscada es menor que la clave del nodo actual...
            return self._obtener(clave,nodoActual.hijoIzquierdo) # Llama recursivamente a _obtener en el hijo izquierdo.
        else: # Si la clave buscada es mayor que la clave del nodo actual...
            return self._obtener(clave,nodoActual.hijoDerecho)  # Llama recursivamente a _obtener en el hijo derecho.
    
    def obtener_claves(self): # Método para obtener una lista de todas las claves en el árbol.
        claves = []  # Inicializa una lista vacía para almacenar las claves de los nodos.
        self._obtener_claves(self.raiz, claves) # Llama al método privado _obtener_claves, comenzando desde la raíz, para llenar la lista con las claves.
        return claves # Retorna la lista de claves obtenida.

    def _obtener_claves(self, nodoActual, claves):# Define la función _obtener_claves, que recibe un nodo actual y una lista de claves
        if nodoActual: # Verifica si el nodo actual no es nulo
            self._obtener_claves(nodoActual.hijoIzquierdo, claves)  # Recorrer el hijo izquierdo
            claves.append(nodoActual.clave)  # Añadir la clave del nodo actual
            self._obtener_claves(nodoActual.hijoDerecho, claves)  # Recorrer el hijo derecho

    def obtener_lista(self): # Define la función obtener_lista 
        return [self.obtener(clave) for clave in self.obtener_claves()]  # Devuelve una lista de valores obtenidos para cada clave en el árbol

    def __getitem__(self,clave):  # Define el método __getitem__ para acceder a valores usando la sintaxis de índice (ej: objeto[clave])
        res = self.obtener(clave) # Llama al método obtener con la clave dada y guarda el resultado en res
        if res: # Si res no es None (es decir, si encontró un valor para la clave)
            return res # Retorna el valor encontrado
        else:  # Si no encontró un valor (res es None)
            raise KeyError('Error, la clave no está en el árbol') # Lanza una excepción KeyError si la clave no existe en el árbol

    def __contains__(self,clave):  # Define el método especial __contains__ para verificar si una clave está en el árbol
        if self._obtener(clave,self.raiz):  # Llama al método _obtener para buscar la clave desde la raíz
            return True # Devuelve True si la clave fue encontrada
        else:
            return False # Devuelve False si la clave no fue encontrada

    def longitud(self): # Define el método longitud para obtener el tamaño del árbol
        return self.tamano  # Retorna el tamaño del árbol almacenado en el atributo tamano

    def __len__(self):   # Define el método especial __len__ para obtener la longitud del árbol con len()
        return self.tamano # Retorna el tamaño del árbol, igual que longitud()

    def __iter__(self):  # Define el método especial __iter__ para hacer el árbol iterable
        return self.raiz.__iter__() # Llama al método __iter__ de la raíz para iterar sobre los nodos del árbol

    def eliminar(self,clave): # Define el método eliminar para eliminar un nodo con la clave dada
        if self.tamano > 1:  # Verifica si el árbol tiene más de un nodo
            nodoAEliminar = self._obtener(clave,self.raiz)  # Busca el nodo a eliminar a partir de la raíz
            if nodoAEliminar: # Si el nodo a eliminar existe
                self.remover(nodoAEliminar) # Llama al método remover para eliminar el nodo
                self.tamano = self.tamano-1 # Decrementa el tamaño del árbol en 1
            else:  # Si no se encontró el nodo
                raise KeyError('Error, la clave no está en el árbol') # Lanza una excepción si la clave no existe
        elif self.tamano == 1 and self.raiz.clave == clave: # Caso especial: si hay solo un nodo y coincide con la clave
            self.raiz = None  # Elimina la raíz estableciéndola en None
            self.tamano = self.tamano - 1 # Decrementa el tamaño del árbol en 1
        else:  # Si el árbol tiene un solo nodo y la clave no coincide o está vacío
            raise KeyError('Error, la clave no está en el árbol') # Lanza una excepción si la clave no existe

    def __delitem__(self,clave):  # Define el método especial __delitem__ para eliminar un elemento usando la sintaxis "del objeto[clave]"
        self.eliminar(clave)  # Llama al método eliminar para eliminar el nodo con la clave dada

    def remover(self,nodoActual):  # Define el método remover para eliminar un nodo específico del árbol
        if nodoActual.esHoja():  # Caso 1: si el nodo es una hoja (no tiene hijos)
            if nodoActual == nodoActual.padre.hijoIzquierdo:  # Verifica si el nodo es el hijo izquierdo de su padre
                nodoActual.padre.hijoIzquierdo = None # Elimina el nodo estableciendo el hijo izquierdo del padre en None
            else: # Si el nodo es el hijo derecho de su padre
                nodoActual.padre.hijoDerecho = None # Elimina el nodo estableciendo el hijo derecho del padre en None
        elif nodoActual.tieneAmbosHijos(): # Caso 2: si el nodo tiene ambos hijos (es un nodo interior)
            suc = nodoActual.encontrarSucesor()  # Encuentra el sucesor del nodo (el menor nodo en el subárbol derecho)
            suc.empalmar() # Desconecta el sucesor de su ubicación actual
            nodoActual.clave = suc.clave # Reemplaza la clave del nodo actual con la clave del sucesor
            nodoActual.cargaUtil = suc.cargaUtil # Reemplaza la carga útil del nodo actual con la del sucesor

        else: # Caso 3: este nodo tiene un solo hijo
            if nodoActual.tieneHijoIzquierdo():  # Si el nodo tiene un hijo izquierdo
                if nodoActual.esHijoIzquierdo(): # Si el nodo actual es el hijo izquierdo de su padre
                    nodoActual.hijoIzquierdo.padre = nodoActual.padre  # Ajusta el padre del hijo izquierdo para que apunte al padre del nodo actual
                    nodoActual.padre.hijoIzquierdo = nodoActual.hijoIzquierdo # Conecta el hijo izquierdo del nodo actual al lugar que ocupaba el nodo actual en el árbol
                elif nodoActual.esHijoDerecho(): # Si el nodo actual es el hijo derecho de su padre
                    nodoActual.hijoIzquierdo.padre = nodoActual.padre # Ajusta el padre del hijo izquierdo para que apunte al padre del nodo actual
                    nodoActual.padre.hijoDerecho = nodoActual.hijoIzquierdo# Conecta el hijo izquierdo del nodo actual al lugar que ocupaba el nodo actual en el árbol
                else: # Si el nodo es la raíz del árbol
                    nodoActual.reemplazarDatoDeNodo(nodoActual.hijoIzquierdo.clave, nodoActual.hijoIzquierdo.cargaUtil, nodoActual.hijoIzquierdo.hijoIzquierdo, nodoActual.hijoIzquierdo.hijoDerecho) # Reemplaza los datos del nodo actual con los del hijo izquierdo
            else:# Si el nodo tiene un hijo derecho (no tiene hijo izquierdo)
                if nodoActual.esHijoIzquierdo(): # Si el nodo actual es el hijo izquierdo de su padre
                    nodoActual.hijoDerecho.padre = nodoActual.padre  # Ajusta el padre del hijo derecho para que apunte al padre del nodo actual
                    nodoActual.padre.hijoIzquierdo = nodoActual.hijoDerecho # Conecta el hijo derecho del nodo actual al lugar que ocupaba el nodo actual en el árbol
                elif nodoActual.esHijoDerecho():  # Si el nodo actual es el hijo derecho de su padre
                    nodoActual.hijoDerecho.padre = nodoActual.padre  # Ajusta el padre del hijo derecho para que apunte al padre del nodo actual
                    nodoActual.padre.hijoDerecho = nodoActual.hijoDerecho  # Conecta el hijo derecho del nodo actual al lugar que ocupaba el nodo actual en el árbol
                else: # Si el nodo es la raíz del árbol
                    nodoActual.reemplazarDatoDeNodo(nodoActual.hijoDerecho.clave, nodoActual.hijoDerecho.cargaUtil, nodoActual.hijoDerecho.hijoIzquierdo, nodoActual.hijoDerecho.hijoDerecho) # Reemplaza los datos del nodo actual con los del hijo derecho

    def inorden(self): # Define el metodo que inicia el recorrido en inorden
        self._inorden(self.raiz)# Llama a la función recursiva _inorden con la raíz del árbol

    def _inorden(self,arbol): # Define el metodo para el recorrido en inorden
        if arbol != None: # Si el nodo actual no es None
            self._inorden(arbol.hijoIzquierdo)# Llama a _inorden para recorrer el subárbol izquierdo
            print(arbol.clave) # Imprime la clave del nodo actual
            self._inorden(arbol.hijoDerecho)# Llama a _inorden para recorrer el subárbol derecho

    def postorden(self): # Define el metodo que inicia el recorrido en post orden 
        self._postorden(self.raiz) # Llama a la función recursiva _postorden con la raíz del árbol

    def _postorden(self, arbol): # Define el metodo para el recorrido en postorden
        if arbol: # Si el nodo actual no es None
            self._postorden(arbol.hijoDerecho) # Llama a _postorden para recorrer el subárbol derecho
            self._postorden(arbol.hijoIzquierdo) # Llama a _postorden para recorrer el subárbol izquierdo
            print(arbol.clave)# Imprime la clave del nodo actua

    def preorden(self): # Define el metodo que inicia el recorrido en preorden
        self._preorden(self.raiz) # Llama a la función recursiva _preorden con la raíz del árbol

    def _preorden(self,arbol):  # Define el metodo para el recorrido en preorden
        if arbol:# Si el nodo actual no es None
            print(arbol.clave)# Imprime la clave del nodo actual
            self._preorden(arbol.hijoIzquierdo)#Llama a _preorden para recorrer el subárbol izquierdo 
            self._preorden(arbol.hijoDerecho) # Llama a _preorden para recorrer el subárbol derecho

class NodoArbol:
    def __init__(self,clave,valor,izquierdo=None,derecho=None,padre=None):
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = izquierdo
        self.hijoDerecho = derecho
        self.padre = padre
        self.factorEquilibrio = 0

    def tieneHijoIzquierdo(self):
        return self.hijoIzquierdo

    def tieneHijoDerecho(self):
        return self.hijoDerecho

    def esHijoIzquierdo(self):
        return self.padre and self.padre.hijoIzquierdo == self

    def esHijoDerecho(self):
        return self.padre and self.padre.hijoDerecho == self

    def esRaiz(self):
        return not self.padre

    def esHoja(self):
        return not (self.hijoDerecho or self.hijoIzquierdo)

    def tieneAlgunHijo(self):
        return self.hijoDerecho or self.hijoIzquierdo

    def tieneAmbosHijos(self):
        return self.hijoDerecho and self.hijoIzquierdo

    def reemplazarDatoDeNodo(self,clave,valor,hizq,hder):
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = hizq
        self.hijoDerecho = hder
        if self.tieneHijoIzquierdo():
            self.hijoIzquierdo.padre = self
        if self.tieneHijoDerecho():
            self.hijoDerecho.padre = self

    def encontrarSucesor(self):
        suc = None
        if self.tieneHijoDerecho():
            suc = self.hijoDerecho.encontrarMin()
        else:
            if self.padre:
                if self.esHijoIzquierdo():
                    suc = self.padre
                else:
                    self.padre.hijoDerecho = None
                    suc = self.padre.encontrarSucesor()
                    self.padre.hijoDerecho = self
        return suc

    def empalmar(self):
        if self.esHoja():
            if self.esHijoIzquierdo():
                self.padre.hijoIzquierdo = None
            else:
                self.padre.hijoDerecho = None
        elif self.tieneAlgunHijo():
            if self.tieneHijoIzquierdo():
                if self.esHijoIzquierdo():
                    self.padre.hijoIzquierdo = self.hijoIzquierdo
                else:
                    self.padre.hijoDerecho = self.hijoIzquierdo
                self.hijoIzquierdo.padre = self.padre
            else:
                if self.esHijoIzquierdo():
                    self.padre.hijoIzquierdo = self.hijoDerecho
                else:
                    self.padre.hijoDerecho = self.hijoDerecho
                self.hijoDerecho.padre = self.padre

    def encontrarMin(self):
        actual = self
        while actual.tieneHijoIzquierdo():
            actual = actual.hijoIzquierdo
        return actual

    def __iter__(self):
        if self:
            if self.tieneHijoIzquierdo():
                for elem in self.hijoIzquierdo:
                    yield elem
            yield self.clave
            if self.tieneHijoDerecho():
                for elem in self.hijoDerecho:
                    yield elem
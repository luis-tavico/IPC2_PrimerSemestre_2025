class Nodo:
    def __init__(self, dato=None, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente

class ListaEnlazada():
    def __init__(self):
        self.primero = None

    def push(self, dato):
        if self.primero is None:
            self.primero = Nodo(dato=dato)
            return
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = Nodo(dato=dato)

    def pop(self):
        primero = self.primero
        if self.primero != None:            
            self.primero = self.primero.siguiente
        if primero != None:
            primero.siguiente = None
        return primero

    def values(self):
        values = self.primero
        return values
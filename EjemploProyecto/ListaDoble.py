from Celda import Celda

class Nodo:
    def __init__(self, dato=None, siguiente=None, anterior=None):
        self.dato = dato
        self.siguiente = siguiente
        self.anterior = anterior

class ListaDobleEnlazada:
    def __init__(self):
        self.primero = None
    
    def insertar(self, dato):
        nodo = Nodo(dato=dato)
        if self.primero is None:
            self.primero = nodo
        else:
            actual = self.primero
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nodo
            nodo.anterior = actual

    def eliminar(self, dato):
        actual = self.primero
        while actual and actual.dato != dato:
            actual = actual.siguiente
        if actual is None:
            return
        if actual.anterior is None: 
            self.primero = actual.siguiente
            if self.primero:
                self.primero.anterior = None
        else:
            actual.anterior.siguiente = actual.siguiente
        if actual.siguiente:
            actual.siguiente.anterior = actual.anterior
        actual.siguiente = None
        actual.anterior = None

    def buscar(self, dato):
        actual = self.primero
        anterior = None
        while actual and actual.dato != dato:
            anterior = actual
            actual = actual.siguiente
        if actual:
            return True
        else:
            return False

    def recorrer(self):
        actual = self.primero
        while actual:
            if actual.dato.getInerte():
                print("X", end=" ")
            else:
                print("O", end=" ")
            actual = actual.siguiente
        print("")
    
    def datos(self):
        datos = self.primero
        return datos
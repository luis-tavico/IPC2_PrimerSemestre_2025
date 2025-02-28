from Celda import Celda
from ListaDoble import ListaDobleEnlazada

def cargarDatos(lista):
    lista.insertar(Celda("VAWL", 1, 1, 1, False))
    lista.insertar(Celda("VED", 2, 1, 2, False))
    lista.insertar(Celda("WQSD", 3, 1, 3, False))
    lista.insertar(Celda("GXS", 4, 2, 1, False))
    lista.insertar(Celda("XC", 5, 2, 2, False))
    lista.insertar(Celda("VF", 6, 2, 3, False))
    lista.insertar(Celda("WER", 7, 3, 1, False))
    lista.insertar(Celda("YTR", 8, 3, 2, False))
    lista.insertar(Celda("WEAS", 9, 3, 3, False))

def borrarDatos(lista):
    lista = ListaDobleEnlazada()

lista = ListaDobleEnlazada()
while(True):
    print("1. Cargar Datos")
    print("2. Convertir Celula a Inerte")
    print("3. Imprimir Lista")
    print("4. Borrar Datos")
    print("5. Salir")
    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        cargarDatos(lista)
    elif opcion == 2:
        celula = input("Ingrese la celula: ")
        actual = lista.datos()
        anterior = None
        while actual and actual.dato.getCelula() != celula:
            anterior = actual
            actual = actual.siguiente
        if actual:
            actual.dato.setInerte(True)
            print("Celula convertida a inerte")
        else:
            print("Celula no encontrada")       
    elif opcion == 3:
        lista.recorrer()
    elif opcion == 4:
        borrarDatos(lista)
    elif opcion == 5:
        break
    else:
        print("Opcion no valida")
from ListaEnlazadaSimple import ListaEnlazadaSimple
from ListaEnlazadaDobleCeldas import ListaEnlazadaDobleCeldas
from Celda import Celda
from Experimento import Experimento
from Tejido import Tejido
from ParejaProteina import ParejaProteina
from Archivo import Archivo
from Grafico import Grafico

def cambiarEstadoInerte(rejilla, posicionCelda):
    filas = rejilla.datos()
    while filas:
        columnas = filas.dato
        columnas.cambiarEstadoInerte(posicionCelda)
        filas = filas.siguiente

def buscarProteina(celda, proteina1, proteina2):
    posCelula1 = None
    posCelula2 = None
    if (celda.dato.getCelula() == proteina1) and not(celda.dato.getInerte()):
        # Buscar hacia adelante o hacia abajo
        actual = celda.siguiente
        while actual:
            if not actual.dato.getInerte():
                if actual.dato.getCelula() == proteina2:
                    # Obtener posiciones
                    posCelula1 = celda.dato.getPosicion()
                    posCelula2 = actual.dato.getPosicion()
                    break
                else:
                    break
            else:
                actual = actual.siguiente
        # Comprobar si las celulas cancerigenas han sido encontradas
        if posCelula1 is None and posCelula2 is None:
            # Buscar hacia atras o hacia arriba
            actual = celda.anterior
            while actual:
                if not actual.dato.getInerte():
                    if actual.dato.getCelula() == proteina2:
                        # Obtener posiciones
                        posCelula1 = celda.dato.getPosicion()
                        posCelula2 = actual.dato.getPosicion()
                        break
                    else:
                        break
                else:
                    actual = actual.anterior
    return posCelula1, posCelula2

if __name__ == "__main__":

    listaExperimentos = ListaEnlazadaSimple()
    
    while True:   
        print("+--------------------------------------------+")
        print("|               MENU PRINCIPAL               |")
        print("+--------------------------------------------+")
        print("|1. Inicializar Sistema                      |")
        print("|2. Crear Catalogo de Experimentos           |")
        print("|3. Desarrollar Experimento                  |")
        print("|4. Mostrar Datos del Estudiante             |")
        print("|5. Salir                                    |")
        print("+--------------------------------------------+")
        opcion = int(input("Ingrese una opcion: "))

        if opcion == 1:
            listaExperimentos = ListaEnlazadaSimple()
            print("¡Sistema inicializado exitosamente!")
        elif opcion == 2:
            ruta = input("Ingrese la ruta del archivo XML: ")
            nuevoArchivo = Archivo(ruta)
            nuevoArchivo.leer(listaExperimentos)
            print("¡Catalogo de experimentos creado exitosamente!")
        elif opcion == 3:
            while True:
                print("+--------------------------------------------+")
                print("|           DESARROLLAR EXPERIMENTO          |")
                print("+--------------------------------------------+")
                print("|1. Cargar Manualmente                       |")
                print("|2. Cargar del Catalogo                      |")
                print("|3. Regresar                                 |")
                print("+--------------------------------------------+")
                opcion = int(input("Ingrese una opcion: "))

                if opcion == 1:
                    nuevoExperimento = Experimento()
                    nombre = input("Ingrese el nombre: ")
                    filas = int(input("Ingrese la cantidad de filas: "))
                    columnas = int(input("Ingrese la cantidad de columnas: "))
                    # Tejido
                    rejilla = input("Ingrese la rejilla: ")                   
                    rejilla = rejilla.replace("\n", " ").split()
                    # Obtener valores en orden de filas
                    rejillaOrdenFil = ListaEnlazadaSimple()
                    posCol = 0
                    for i in range(filas):
                        filaRejilla = ListaEnlazadaDobleCeldas()
                        for j in range(columnas):
                            nuevaCelda = Celda(rejilla[posCol], (posCol+1), (i+1), (j+1),  False)
                            filaRejilla.insertar(nuevaCelda)
                            posCol += 1
                        rejillaOrdenFil.insertar(filaRejilla)
                    # Otener valores en orden de columnas
                    rejillaOrdenCol = ListaEnlazadaSimple()
                    posFil = 0
                    posCol = 0
                    for j in range(columnas):
                        posFil = posCol
                        columnaRejilla = ListaEnlazadaDobleCeldas()
                        for i in range(filas):
                            nuevaCelda = Celda(rejilla[posFil], (posFil+1), (posFil+1), (posCol+1),  False)
                            columnaRejilla.insertar(nuevaCelda)
                            posFil += columnas
                        rejillaOrdenCol.insertar(columnaRejilla)
                        posCol += 1
                    # Crear nuevo tejido
                    nuevoTejido = Tejido(filas, columnas, rejillaOrdenFil, rejillaOrdenCol)
                    # Proteinas
                    listaProteinas = ListaEnlazadaSimple()
                    while True:
                        nuevaParejaProteina = ParejaProteina()
                        proteina1 = input("Ingrese la primera proteina: ")
                        proteina2 = input("Ingrese la segunda proteina: ")
                        nuevaParejaProteina.setProteina1(proteina1)
                        nuevaParejaProteina.setProteina2(proteina2)
                        listaProteinas.insertar(nuevaParejaProteina)
                        opcion = input("¿Desea ingresar otra pareja de proteinas? (s/n): ")
                        if opcion == "n":
                            break
                    # Crear nuevo experimento
                    nuevoExperimento.setNombre(nombre)
                    nuevoExperimento.setFilasEnTejido(filas)
                    nuevoExperimento.setColumnasEnTejido(columnas)
                    nuevoExperimento.setTejido(nuevoTejido)
                    nuevoExperimento.setProteinas(listaProteinas)
                    listaExperimentos.insertar(nuevoExperimento)
                    
                elif opcion == 2:
                    print("+--------------------------------------------+")
                    print("|             ELIJA UN EXPERIMENTO           |")
                    print("+--------------------------------------------+")
                    experimentos = listaExperimentos.datos()
                    posPaciente = 1
                    while experimentos:
                        print(f"|{posPaciente}. {experimentos.dato.getNombre():<40}|")  
                        posPaciente += 1
                        experimentos = experimentos.siguiente
                    print("+--------------------------------------------+")
                    posPaciente = int(input("Ingrese una opcion: "))

                    while True:
                        print("+--------------------------------------------+")
                        print("|              ELIJA UNA OPCION              |")
                        print("+--------------------------------------------+")
                        print("|1. Modificar                                |")
                        print("|2. Ejecutar                                 |")
                        print("|3. Regresar                                 |")
                        print("+--------------------------------------------+")
                        opcion = int(input("Ingrese una opcion: "))
                        if opcion == 1:
                            print("Modificar")
                        elif opcion == 2:
                            while True:
                                print("+--------------------------------------------+")
                                print("|              ELIJA UNA OPCION              |")
                                print("+--------------------------------------------+")
                                print("|1. Ejecutar Directamente                    |")
                                print("|2. Ejecutar Paso a Paso                     |")
                                print("|3. Regresar                                 |")
                                print("+--------------------------------------------+")
                                opcion = int(input("Ingrese una opcion: "))

                                if opcion == 1:
                                    print("Ejecutar Directamente")
                                elif opcion == 2:
                                    experimentos = listaExperimentos.datos()
                                    pos = 1
                                    # Buscar experimento selccionado
                                    while pos < posPaciente:
                                        experimentos = experimentos.siguiente
                                        pos += 1
                                    # Obtener experimento
                                    experimento = experimentos.dato
                                    # Obtener datos del experimento
                                    tejido = experimento.getTejido()
                                    listaProteinas = experimento.getProteinas()
                                    # Crear variables para almacenar las proteinas
                                    proteina1 = ""
                                    proteina2 = ""
                                    # Crear variable para almacenar la cantidad de celulas inertes
                                    celulasInertes = 0
                                    # Crear variable para almacenar el numero de estado
                                    numeroEstado = 0
                                    # Obtener proteinas del experimento
                                    listaProteinas = listaProteinas.datos()
                                    # Crear variables para almacenar las posiciones
                                    posCelula1 = None
                                    posCelula2 = None
                                    # Obtener rejillas
                                    rejillaOrdenFil = tejido.getRejillaOrdenFil()
                                    rejillaOrdenCol = tejido.getRejillaOrdenCol()
                                    # Buscar proteinas en las rejillas
                                    while listaProteinas:
                                        # Crear variables para recorrer las rejillas
                                        PosFilaActual = 1
                                        # Obtener proteinas
                                        proteina1 = listaProteinas.dato.getProteina1()
                                        proteina2 = listaProteinas.dato.getProteina2()
                                        # Buscar proteinas que coincidan con las celulas cancerigenas en la rejilla
                                        filsRejillaOrdFil = rejillaOrdenFil.datos()
                                        while filsRejillaOrdFil:
                                            colsRejillaOrdFil = filsRejillaOrdFil.dato.datos()
                                            filsRejillaOrdCol = rejillaOrdenCol.datos()
                                            while colsRejillaOrdFil:
                                                # Buscar horizontalmente
                                                posCelula1, posCelula2 = buscarProteina(colsRejillaOrdFil, proteina1, proteina2)
                                                if posCelula1 is None and posCelula2 is None:
                                                    posCelula1, posCelula2 = buscarProteina(colsRejillaOrdFil, proteina2, proteina1)
                                                # Comprobar si las celulas cancerigenas han sido encontradas
                                                if posCelula1 is None and posCelula2 is None:
                                                    # Obtener las columnas
                                                    colsRejillaOrdCol = filsRejillaOrdCol.dato.datos()
                                                    pos = 1
                                                    # Obtener la columna actual
                                                    while pos < PosFilaActual:
                                                        colsRejillaOrdCol = colsRejillaOrdCol.siguiente
                                                        pos += 1
                                                    # Buscar verticalmente
                                                    posCelula1, posCelula2 = buscarProteina(colsRejillaOrdCol, proteina1, proteina2)
                                                    if posCelula1 is None and posCelula2 is None:
                                                        posCelula1, posCelula2 = buscarProteina(colsRejillaOrdCol, proteina2, proteina1)
                                                # Fin
                                                if posCelula1 is None and posCelula2 is None:
                                                    # Cambiar columna en fila y fila en columna
                                                    colsRejillaOrdFil = colsRejillaOrdFil.siguiente
                                                    filsRejillaOrdCol = filsRejillaOrdCol.siguiente
                                                else:
                                                    break
                                            if not(posCelula1 is None) and not(posCelula2 is None):
                                                # Cambiar estado inerte en rejilla de filas
                                                cambiarEstadoInerte(tejido.getRejillaOrdenFil(), posCelula1)
                                                cambiarEstadoInerte(tejido.getRejillaOrdenFil(), posCelula2)
                                                # Cambiar estado inerte en rejilla de columnas
                                                cambiarEstadoInerte(tejido.getRejillaOrdenCol(), posCelula1)
                                                cambiarEstadoInerte(tejido.getRejillaOrdenCol(), posCelula2)
                                                # Incrementar celulas inertes
                                                celulasInertes += 2
                                                # Incrementar numero de estado
                                                numeroEstado += 1
                                                # Graficar
                                                grafico = Grafico(numeroEstado, experimento.getNombre(), rejillaOrdenFil, experimento.getFilasEnTejido(), experimento.getColumnasEnTejido())
                                                grafico.graficar()
                                                # Inicializar variables
                                                posCelula1 = None
                                                posCelula2 = None
                                                PosFilaActual = 1
                                                filsRejillaOrdFil = rejillaOrdenFil.datos()
                                            else:
                                                # Cambiar fila
                                                filsRejillaOrdFil = filsRejillaOrdFil.siguiente
                                                PosFilaActual += 1
                                        # Fin de la busqueda
                                        listaProteinas = listaProteinas.siguiente                                     

                                    # Imprimir rejilla para ver cambios
                                    f = rejillaOrdenFil.datos()
                                    while f:
                                        c = f.dato.datos()
                                        while c:
                                            print(c.dato.getInerte(), end="\t")
                                            c = c.siguiente
                                        print()
                                        f = f.siguiente

                                    # Obtener porcentaje de celulas inertes
                                    porcentaje = celulasInertes  * 100 / (experimento.getFilasEnTejido() * experimento.getColumnasEnTejido())
                
                                    print()
                                    print(f"Porcentaje de celulas inertes: {porcentaje}%")

                                    if porcentaje < 30:
                                        print("El medicamento no es efectivo.")
                                    elif porcentaje >= 30 and porcentaje < 60:
                                        print("El medicamento es efectivo.")
                                    else:
                                        print("El medicamento es fatal.")

                                elif opcion == 3:
                                    break
                                else:
                                    print("¡Ingrese una opcion valida!")
                        elif opcion == 3:
                            break
                        else:
                            print("¡Ingrese una opcion valida!")
                elif opcion == 3:
                    break
                else:
                    print("¡Ingrese una opcion valida!")
        elif opcion == 4:
            print("+---------------------------------------------------------------------------------------------+")
            print("|                                         INFORMACION                                         |")
            print("+---------------------------------------------------------------------------------------------+")
            print("| Nombre:   | Pedro Luis Pu Tavico                                                            |")
            print("| Carnet:   | 202000562                                                                       |")
            print("| Curso:    | Introduccion a la Programacion y Computacion 2                                  |")
            print("| Carrera:  | Ingenieria en Ciencias y Sistemas                                               |")
            print("| Semestre: | Primer Semestre 2025                                                            |")
            print("| Enlace:   | https://github.com/luis-tavico/IPC2_Proyecto1_202000562/tree/main/Documentacion |")
            print("+---------------------------------------------------------------------------------------------+")
        elif opcion == 5:
            print("Ejecucion Finalizada.")
            break
        else:
            print("¡Ingrese una opcion valida!")
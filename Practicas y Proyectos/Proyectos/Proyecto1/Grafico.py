import os

class Grafico:
    def __init__(self, numeroEstado, nombre, rejilla, filas, columnas):
        self.numeroEstado = numeroEstado
        self.nombre = nombre
        self.rejilla = rejilla
        self.filas = filas
        self.columnas = columnas

    def graficar(self):
        cadenaAGraficar = "digraph Grafica {\n\tnodesep=\"0 equally\"\n\tranksep=\"0.02 equally\"\n\tnode[shape=box fillcolor=\"white\" style=filled fontcolor=black color=\"gray\" fontname=\"arial\"]\n\tsubgraph cluster_rejilla {\n"
        cadenaAGraficar += "\t\tlabel = \"Estado " + str(self.numeroEstado) + "\"\n\t\tfontcolor = \"black\"\n\t\tfontname = \"arial\"\n\t\tbgcolor = \"white\"\n\t\tcolor = white\n\t\traiz[label=\"\" color=\"white\"]\n\t\tedge[dir=\"none\" style=invisible]\n"    
        fila = ""
        columna = ""
        unionNodo = ""
        alinearNodo = ""
        for numero in range(self.filas):
            fila += '\t\tfila'+ str(numero+1) + '[label="'+ str(numero+1) + '" color="white"];\n'
        for numero in range(self.columnas):
            columna += '\t\tcolumna'+ str(numero+1) + '[label="'+ str(numero+1) + '" color="white"];\n'
        cadenaAGraficar += fila
        cadenaAGraficar += columna
        fila = ""
        columna = ""
        for numero in range(self.filas-1):
            fila += '\t\tfila'+ str(numero+1) +'->fila'+ str(numero+2) +'\n'
        for numero in range(self.columnas-1):
            columna += '\t\tcolumna'+ str(numero+1) +'->columna'+ str(numero+2) +'\n'
        cadenaAGraficar += fila
        cadenaAGraficar += columna
        cadenaAGraficar += '\t\traiz->fila1\n\t\traiz->columna1\n'
        rankColumnas = '\t\t{rank = same;raiz'
        for numero in range(self.columnas):
            rankColumnas += ';columna'+ str(numero+1)
        rankColumnas += '}\n'
        cadenaAGraficar += rankColumnas
        pos = 1
        for numFila in range(self.filas):
            unionNodo += '\t\tfila' + str(numFila+1)
            alinearNodo += '\t\t{rank=same;fila'+ str(numFila+1)
            for numColumna in range(self.columnas):
                unionNodo += '->nodo'+ str(pos) 
                alinearNodo += ';nodo'+ str(pos)
                pos += 1
            unionNodo += '\n'
            alinearNodo += '}\n'
        pos = 1
        f = self.rejilla.datos()
        while f:
            c = f.dato.datos()
            while c:
                if c.dato.getInerte():
                    cadenaAGraficar += '\t\tnodo'+ str(pos) +'[label=\"'+ c.dato.getCelula() +'\", fillcolor=red]\n'
                else:
                    cadenaAGraficar += '\t\tnodo'+ str(pos) +'[label=\"'+ c.dato.getCelula() +'\", fillcolor=white]\n'
                pos += 1
                c = c.siguiente
            f = f.siguiente
        cadenaAGraficar += unionNodo
        cadenaAGraficar += alinearNodo
        cadenaAGraficar += '   }\n}'
        txt = 'grafica.txt'
        with open(txt, 'w') as grafica:
            grafica.write(cadenaAGraficar)
        pdf = self.nombre + '_estado' + str(self.numeroEstado) + '.pdf'
        os.system("dot.exe -Tpdf " + txt + " -o " + pdf)
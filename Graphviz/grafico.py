import os

def graficar(filas, columnas):
    codigo = 'digraph G {\nnode [fontname="Helvetica,Arial,sans-serif"]\na0 [shape=none label=<\n\t<TABLE border="0" cellspacing="1" cellpadding="5">'
    for i in range(filas):
        codigo += '\n\t\t<TR>'
        for j in range(columnas):
            codigo += f'\n\t\t\t<TD bgcolor="green">{i},{j}</TD>'
        codigo += '\n\t\t</TR>'
    codigo += '\n\t    </TABLE>\n\t>];\n}'

    txt = 'grafica.txt'
    with open(txt, 'w') as grafica:
        grafica.write(codigo)
    pdf = 'grafico.pdf'
    os.system("dot.exe -Tpdf " + txt + " -o " + pdf)

graficar(5, 5)
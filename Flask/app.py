from flask import Flask, render_template, request

app = Flask(__name__)

# Diccionario de opciones
menu = {
    "Comida": ["Pizza", "Hamburguesa", "Ensalada"],
    "Bebida": ["Agua", "Coca-Cola", "Jugo"],
    "Postre": ["Helado", "Pastel", "Fruta"]
}

@app.route("/", methods=["GET", "POST"])
def menu_seleccion():
    categoria = None
    opcion = None

    if request.method == "POST":
        categoria = request.form.get("categoria")
        opcion = request.form.get("opcion")

        # Si ya tiene opción, mostramos resultado
        if opcion:
            return render_template("index.html", categorias=menu.keys(),
                                   categoria=categoria, opciones=menu[categoria], opcion=opcion)

        # Si solo tiene categoría, mostramos sus opciones
        if categoria:
            return render_template("index.html", categorias=menu.keys(),
                                   categoria=categoria, opciones=menu[categoria])

    return render_template("index.html", categorias=menu.keys())

if __name__ == "__main__":
    app.run(debug=True)

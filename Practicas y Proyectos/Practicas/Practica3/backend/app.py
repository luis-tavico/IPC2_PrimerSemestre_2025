from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite peticiones desde el frontend

# Base de datos simulada
productos = [
    {"id": 1, "nombre": "Laptop",    "precio": 4900, "marca": "Dell"},
    {"id": 2, "nombre": "Mouse",     "precio": 450,  "marca": "Logitech"},
    {"id": 3, "nombre": "Teclado",   "precio": 220,  "marca": "Corsair"},
    {"id": 4, "nombre": "Monitor",   "precio": 1300, "marca": "Samsung"},
    {"id": 5, "nombre": "Impresora", "precio": 800,  "marca": "HP"}
]

# Obtener todos los productos
@app.route('/productos', methods=['GET'])
def obtener_productos():
    return jsonify(productos)

# Obtener un solo producto por ID
@app.route('/productos/<int:id>', methods=['GET'])
def obtener_producto(id):
    producto = next((p for p in productos if p["id"] == id), None)
    if producto:
        return jsonify(producto)
    return jsonify({"error": "Producto no encontrado"}), 404

# Crear un producto
@app.route('/productos', methods=['POST'])
def crear_producto():
    nuevo_producto = request.json
    nuevo_producto["id"] = len(productos) + 1
    productos.append(nuevo_producto)
    return jsonify(nuevo_producto), 201

# Actualizar un producto
@app.route('/productos/<int:id>', methods=['PUT'])
def actualizar_producto(id):
    for producto in productos:
        if producto["id"] == id:
            producto.update(request.json)
            return jsonify(producto)
    return jsonify({"error": "Producto no encontrado"}), 404

# Eliminar un producto
@app.route('/productos/<int:id>', methods=['DELETE'])
def eliminar_producto(id):
    global productos
    productos = [p for p in productos if p["id"] != id]
    return jsonify({"message": "Producto eliminado"}), 200

if __name__ == '__main__':
    app.run(port=5000, debug=True)
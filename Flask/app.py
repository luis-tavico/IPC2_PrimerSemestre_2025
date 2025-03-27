from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista en memoria para almacenar clientes
clientes = []
cliente_id_contador = 1

def buscar_cliente(clientes, cliente_id):
    for c in clientes:
        if c["id"] == cliente_id:
            return c
    return None

@app.route("/")
def index():
    return "Bienvenido al sistema de clientes"

# Obtener todos los clientes
@app.route("/clientes", methods=["GET"])
def get_clientes():
    return jsonify(clientes)

# Agregar un nuevo cliente
@app.route("/clientes", methods=["POST"])
def add_cliente():
    global cliente_id_contador
    data = request.json
    
    if "nombre" not in data or not data["nombre"]:
        return jsonify({"error": "El nombre es obligatorio"}), 400
    if "email" not in data or not data["email"]:
        return jsonify({"error": "El email es obligatorio"}), 400
    
    cliente = {
        "id": cliente_id_contador,
        "nombre": data["nombre"],
        "email": data["email"],
        "telefono": data.get("telefono", ""),
        "direccion": data.get("direccion", ""),
        "productos_adquiridos": data.get("productos_adquiridos", []),
        "total": sum(p["precio"] * p["cantidad"] for p in data.get("productos_adquiridos", []))
    }
    clientes.append(cliente)
    cliente_id_contador += 1
    return jsonify({"mensaje": "Cliente agregado exitosamente."}), 201

# Agregar varios clientes
@app.route("/clientes/varios", methods=["POST"])
def add_varios_clientes():
    global cliente_id_contador
    data = request.json
    
    if not isinstance(data, list):
        return jsonify({"error": "Se espera una lista de clientes"}), 400

    nuevos_clientes = []
    for cliente_data in data:
        if "nombre" not in cliente_data or not cliente_data["nombre"]:
            return jsonify({"error": "Cada cliente debe tener un nombre"}), 400
        if "email" not in cliente_data or not cliente_data["email"]:
            return jsonify({"error": "Cada cliente debe tener un email"}), 400

        cliente = {
            "id": cliente_id_contador,
            "nombre": cliente_data["nombre"],
            "email": cliente_data["email"],
            "telefono": cliente_data.get("telefono", ""),
            "direccion": cliente_data.get("direccion", ""),
            "productos_adquiridos": cliente_data.get("productos_adquiridos", []),
            "total": sum(p["precio"] * p["cantidad"] for p in cliente_data.get("productos_adquiridos", []))
        }
        clientes.append(cliente)
        nuevos_clientes.append(cliente)
        cliente_id_contador += 1

    return jsonify({"mensaje": "Clientes agregados exitosamente."}), 201

# Obtener un cliente por ID
@app.route("/clientes/<int:cliente_id>", methods=["GET"])
def get_cliente(cliente_id):
    cliente = buscar_cliente(clientes, cliente_id)
    if cliente:
        return jsonify(cliente)
    return jsonify({"error": "Cliente no encontrado"}), 404

# Actualizar un cliente
@app.route("/clientes/<int:cliente_id>", methods=["PUT"])
def update_cliente(cliente_id):
    data = request.json
    cliente = buscar_cliente(clientes, cliente_id)

    if not cliente:
        return jsonify({"error": "Cliente no encontrado"}), 404
    
    cliente["nombre"] = data.get("nombre", cliente["nombre"])
    cliente["email"] = data.get("email", cliente["email"])
    cliente["telefono"] = data.get("telefono", cliente["telefono"])
    cliente["direccion"] = data.get("direccion", cliente["direccion"])
    cliente["productos_adquiridos"] = data.get("productos_adquiridos", cliente["productos_adquiridos"])
    cliente["total"] = sum(p["precio"] * p["cantidad"] for p in cliente["productos_adquiridos"])
    
    return jsonify({"mensaje": "Cliente actualizado exitosamente."})

# Eliminar un cliente
@app.route("/clientes/<int:cliente_id>", methods=["DELETE"])
def delete_cliente(cliente_id):
    global clientes
    cliente = buscar_cliente(clientes, cliente_id)
    
    if not cliente:
        return jsonify({"error": "Cliente no encontrado"}), 404
    
    clientes = [c for c in clientes if c["id"] != cliente_id]
    return jsonify({"mensaje": "Cliente eliminado exitosamente."})

if __name__ == "__main__":
    app.run(debug=True)
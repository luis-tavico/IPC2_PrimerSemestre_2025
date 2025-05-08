import requests
from django.shortcuts import render, redirect
from django.http import JsonResponse

API_URL = "http://127.0.0.1:5000/productos"

# Leer productos
def lista_productos(request):
    respuesta = requests.get(API_URL)
    productos = respuesta.json() if respuesta.status_code == 200 else []
    return render(request, 'productos/lista_productos.html', {'productos': productos})

# Crear producto
def crear_producto(request):
    if request.method == "POST":
        nombre = request.POST['nombre']
        marca = request.POST['marca']
        precio = request.POST['precio']
        requests.post(API_URL, json={"nombre": nombre, "marca": marca, "precio": precio})
        return redirect('lista_productos')
    return render(request, 'productos/crear_producto.html')

# Actualizar producto
def actualizar_producto(request, id):
    if request.method == "POST":
        nombre = request.POST['nombre']
        marca = request.POST['marca']
        precio = request.POST['precio']
        requests.put(f"{API_URL}/{id}", json={"nombre": nombre, "marca": marca, "precio": precio})
        return redirect('lista_productos')

    producto = requests.get(f"{API_URL}/{id}").json()
    return render(request, 'productos/actualizar_producto.html', {'producto': producto})

# Eliminar producto
def eliminar_producto(request, id):
    requests.delete(f"{API_URL}/{id}")
    return redirect('lista_productos')
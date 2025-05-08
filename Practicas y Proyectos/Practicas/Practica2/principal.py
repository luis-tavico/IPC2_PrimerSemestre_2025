import tkinter as tk
from tkinter import messagebox
from listaEnlazada import ListaEnlazada
from modeloOrden import Orden
from modeloPizza import Pizza
from grafica import Graficar

class Principal:
    def __init__(self, root):
        self.ordenes = ListaEnlazada()
        self.root = root
        self.root.title("Sistema de Pizzas")
        self.root.geometry("400x300")
        self.root.config(bg="#f0f0f0")
        
        self.numeroOrden = 0
        self.tiempoEnCola = 0

        # Titulo
        title_label = tk.Label(self.root, text="Menu Principal", font=("Helvetica", 16), bg="#f0f0f0")
        title_label.pack(pady=20)

        # Botones
        self.botonNuevaOrden = tk.Button(self.root, text="Nueva Orden", font=("Helvetica", 12), bg="#4CAF50", fg="white", command=self.nueva_orden)
        self.botonNuevaOrden.pack(pady=10, ipadx=10)

        self.botonEntregarOrden = tk.Button(self.root, text="Entregar Orden", font=("Helvetica", 12), bg="#2196F3", fg="white", command=self.entregar_orden)
        self.botonEntregarOrden.pack(pady=10, ipadx=10)

        self.botonVerOrdenes = tk.Button(self.root, text="Ver Ordenes", font=("Helvetica", 12), bg="#FF5722", fg="white", command=self.ver_ordenes)
        self.botonVerOrdenes.pack(pady=10, ipadx=10)

        self.botonSalir = tk.Button(self.root, text="Salir", font=("Helvetica", 12), bg="#9E9E9E", fg="white", command=self.salir)
        self.botonSalir.pack(pady=10, ipadx=10)

    def nueva_orden(self):
        ventanaNuevaOrden = tk.Toplevel(self.root)
        ventanaNuevaOrden.title("Nueva Orden")
        ventanaNuevaOrden.geometry("400x500")
        
        # Variables para almacenar pizzas temporalmente
        temp_pizzas = []
        
        tk.Label(ventanaNuevaOrden, text="Nombre del Cliente:", font=("Helvetica", 12)).pack(pady=5)
        entry_cliente = tk.Entry(ventanaNuevaOrden, font=("Helvetica", 12))
        entry_cliente.pack(pady=5)
        
        # Frame para agregar pizzas
        frame_pizza = tk.Frame(ventanaNuevaOrden)
        frame_pizza.pack(pady=10, fill="x")
        
        tk.Label(frame_pizza, text="Especialidad:", font=("Helvetica", 12)).grid(row=0, column=0, padx=5, pady=5)
        
        # Usando Combobox en lugar de Entry para especialidades
        especialidades = ["Pepperoni", "Hawaiana", "Vegetariana", "Cuatro Quesos"]
        combo_especialidad = tk.StringVar()
        combo_especialidad.set(especialidades[0])
        dropdown_especialidad = tk.OptionMenu(frame_pizza, combo_especialidad, *especialidades)
        dropdown_especialidad.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(frame_pizza, text="Cantidad:", font=("Helvetica", 12)).grid(row=1, column=0, padx=5, pady=5)
        entry_cantidad = tk.Entry(frame_pizza, font=("Helvetica", 12), width=5)
        entry_cantidad.insert(0, "1")
        entry_cantidad.grid(row=1, column=1, padx=5, pady=5)
        
        # Frame para mostrar pizzas agregadas
        frame_lista = tk.Frame(ventanaNuevaOrden)
        frame_lista.pack(pady=10, fill="both", expand=True)
        
        tk.Label(frame_lista, text="Pizzas en esta orden:", font=("Helvetica", 12, "bold")).pack(anchor="w", padx=10)
        
        listbox_pizzas = tk.Listbox(frame_lista, font=("Helvetica", 11), width=40, height=8)
        listbox_pizzas.pack(padx=10, pady=5, fill="both", expand=True)
        
        def agregar_pizza():
            try:
                especialidad = combo_especialidad.get()
                cantidad = int(entry_cantidad.get())
                if cantidad <= 0:
                    messagebox.showwarning("Cantidad inválida", "La cantidad debe ser mayor a 0.")
                    return
                
                tiempo = {"pepperoni": 12, "hawaiana": 15, "vegetariana": 18, "cuatro quesos": 20}.get(especialidad.lower(), 0)
                
                # Agregar a la lista temporal
                temp_pizzas.append({
                    "especialidad": especialidad,
                    "cantidad": cantidad,
                    "tiempo": tiempo
                })
                
                # Actualizar listbox
                listbox_pizzas.insert(tk.END, f"{cantidad} x {especialidad} - Tiempo: {tiempo} min cada una")
                
                # Limpiar campos
                combo_especialidad.set(especialidades[0])
                entry_cantidad.delete(0, tk.END)
                entry_cantidad.insert(0, "1")
                
            except ValueError:
                messagebox.showwarning("Entrada inválida", "Por favor ingrese una cantidad válida.")
        
        def eliminar_pizza():
            seleccion = listbox_pizzas.curselection()
            if seleccion:
                index = seleccion[0]
                listbox_pizzas.delete(index)
                temp_pizzas.pop(index)
        
        def finalizar_orden():
            if not temp_pizzas:
                messagebox.showwarning("Sin pizzas", "Debe agregar al menos una pizza a la orden.")
                return
                
            nombre_cliente = entry_cliente.get().strip()
            if not nombre_cliente:
                messagebox.showwarning("Sin nombre", "Debe ingresar el nombre del cliente.")
                return
                
            # Crear orden
            pizzas = ListaEnlazada()
            tiempoTotal = 0
            cantidad_total = 0
            
            for pizza_info in temp_pizzas:
                for _ in range(pizza_info["cantidad"]):
                    nuevaPizza = Pizza(pizza_info["especialidad"], f"{pizza_info['tiempo']} min")
                    pizzas.push(nuevaPizza)
                    tiempoTotal += pizza_info["tiempo"]
                    cantidad_total += 1
            
            self.tiempoEnCola += tiempoTotal
            self.numeroOrden += 1
            
            nuevaOrden = Orden(
                self.numeroOrden, 
                nombre_cliente, 
                cantidad_total, 
                pizzas, 
                f"{tiempoTotal} min", 
                str(self.tiempoEnCola)
            )
            
            self.ordenes.push(nuevaOrden)
            messagebox.showinfo("Orden Agregada", f"Orden de {nombre_cliente} agregada con éxito.\nTotal de pizzas: {cantidad_total}\nTiempo estimado: {tiempoTotal} min")
            ventanaNuevaOrden.destroy()
        
        # Frame para botones de control de pizzas
        frame_botones_pizza = tk.Frame(ventanaNuevaOrden)
        frame_botones_pizza.pack(pady=5)
        
        boton_agregar_pizza = tk.Button(frame_botones_pizza, text="Agregar Pizza", font=("Helvetica", 11), 
                                        bg="#4CAF50", fg="white", command=agregar_pizza)
        boton_agregar_pizza.grid(row=0, column=0, padx=5, pady=5)
        
        boton_eliminar_pizza = tk.Button(frame_botones_pizza, text="Eliminar Pizza", font=("Helvetica", 11), 
                                         bg="#F44336", fg="white", command=eliminar_pizza)
        boton_eliminar_pizza.grid(row=0, column=1, padx=5, pady=5)
        
        # Botón finalizar orden
        boton_finalizar = tk.Button(ventanaNuevaOrden, text="Finalizar Orden", font=("Helvetica", 12), 
                                    bg="#2196F3", fg="white", command=finalizar_orden)
        boton_finalizar.pack(pady=15)

    def entregar_orden(self):
        ordenTerminada = self.ordenes.pop()
        if ordenTerminada != None:
            grafica = Graficar()
            grafica.graficarOrdenTerminada(ordenTerminada)
            messagebox.showinfo("Orden Entregada", f"Orden {ordenTerminada.numeroOrden} entregada con éxito.")
        else:
            messagebox.showwarning("No hay Ordenes", "¡No hay órdenes para entregar!")

    def ver_ordenes(self):
        ordenes = self.ordenes.values()
        if ordenes == None:
            messagebox.showwarning("No hay Ordenes", "¡No hay órdenes para mostrar!")
        else:
            grafica = Graficar()
            grafica.graficarOrdenes(ordenes)

    def salir(self):
        confirmacion = messagebox.askyesno("Confirmar Salida", "¿Estás seguro de que quieres salir?")
        if confirmacion:
            self.root.quit()


if __name__ == "__main__":
    root = tk.Tk()
    app = Principal(root)
    root.mainloop()
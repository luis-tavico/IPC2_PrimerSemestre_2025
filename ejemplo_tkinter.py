import tkinter as tk
from tkinter import messagebox, ttk

# Función para manejar el botón de enviar
def enviar_datos():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    genero = var_genero.get()
    terminos = var_terminos.get()
    seleccion_lista = listbox.get(listbox.curselection()) if listbox.curselection() else "Ninguno"

    if not nombre or not edad:
        messagebox.showwarning("Advertencia", "Debe ingresar su nombre y edad.")
        return

    if not terminos:
        messagebox.showwarning("Advertencia", "Debe aceptar los términos y condiciones.")
        return

    mensaje = f"Nombre: {nombre}\nEdad: {edad}\nGénero: {genero}\nPaís: {seleccion_lista}\nAceptó términos: Sí"
    messagebox.showinfo("Datos enviados", mensaje)

# Función para limpiar los campos
def limpiar():
    entry_nombre.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    var_genero.set("Ninguno")
    var_terminos.set(0)
    listbox.selection_clear(0, tk.END)
    text_comentarios.delete("1.0", tk.END)

# Configuración de la ventana principal
root = tk.Tk()
root.title("Formulario de Registro")
root.geometry("500x500")

# Menú principal
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Submenú "Archivo"
menu_archivo = tk.Menu(menu_bar, tearoff=0)
menu_archivo.add_command(label="Nuevo", command=limpiar)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=root.quit)
menu_bar.add_cascade(label="Archivo", menu=menu_archivo)

# Etiqueta y entrada para el nombre
tk.Label(root, text="Nombre:").pack(pady=5)
entry_nombre = tk.Entry(root, width=40)
entry_nombre.pack()

# Etiqueta y entrada para la edad
tk.Label(root, text="Edad:").pack(pady=5)
entry_edad = tk.Entry(root, width=40)
entry_edad.pack()

# Radio buttons para género
var_genero = tk.StringVar(value="Ninguno")
tk.Label(root, text="Género:").pack(pady=5)
frame_genero = tk.Frame(root)
frame_genero.pack()
tk.Radiobutton(frame_genero, text="Masculino", variable=var_genero, value="Masculino").pack(side=tk.LEFT)
tk.Radiobutton(frame_genero, text="Femenino", variable=var_genero, value="Femenino").pack(side=tk.LEFT)
tk.Radiobutton(frame_genero, text="Otro", variable=var_genero, value="Otro").pack(side=tk.LEFT)

# Listbox para selección de país
tk.Label(root, text="País:").pack(pady=5)
listbox = tk.Listbox(root, height=4)
paises = ["Guatemala", "México", "Colombia", "Argentina"]
for pais in paises:
    listbox.insert(tk.END, pais)
listbox.pack()

# Checkbutton para aceptar términos y condiciones
var_terminos = tk.IntVar()
chk_terminos = tk.Checkbutton(root, text="Acepto los términos y condiciones", variable=var_terminos)
chk_terminos.pack(pady=5)

# Área de texto
tk.Label(root, text="Comentarios:").pack(pady=5)
text_comentarios = tk.Text(root, height=4, width=40)
text_comentarios.pack()

# Botones de acción
frame_botones = tk.Frame(root)
frame_botones.pack(pady=10)
btn_enviar = tk.Button(frame_botones, text="Enviar", command=enviar_datos)
btn_enviar.pack(side=tk.LEFT, padx=10)
btn_limpiar = tk.Button(frame_botones, text="Limpiar", command=limpiar)
btn_limpiar.pack(side=tk.LEFT, padx=10)

# Bucle principal
root.mainloop()
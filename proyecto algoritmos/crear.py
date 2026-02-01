import tkinter as tk
from tkinter import messagebox #ventanas emergentes
import random

tuplita = ([], [], [], [], [], [], [])
mostrarLista = list(tuplita)

def registrar():
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    telefono = entry_telefono.get()
    direccion = entry_direccion.get()
    opcion = paquete_var.get()

    #si es que alguno de estos campos ta vacio
    if nombre == "" or apellido == "" or telefono == "" or direccion == "": 
        messagebox.showerror("Error", "Completa todos los campos")
        return

    mostrarLista[0].append(nombre)
    mostrarLista[1].append(apellido)
    mostrarLista[2].append(int(telefono))
    mostrarLista[3].append(direccion)

    if opcion == "PC + Monitor":
        precio = 500
    elif opcion == "PC + Monitor 4K":
        precio = 2000
    elif opcion == "Laptop Pro IA":
        precio = 1500
    else:
        precio = 3000

    mostrarLista[4].append(precio)
    mostrarLista[5].append(precio * 1.15)
    mostrarLista[6].append(random.randint(1, 1000))

    #("titulo de la ventana emergente", "mensaje de la ventana")
    messagebox.showinfo("Registro", "Registro guardado con éxito")

    #limpiar la basura de los campos
    entry_nombre.delete(0, tk.END)
    entry_apellido.delete(0, tk.END)
    entry_telefono.delete(0, tk.END)
    entry_direccion.delete(0, tk.END)

#-----------------------------------------------------------------
#leer datos

def mostrar_pedidos():
    if len(mostrarLista[0]) == 0:
        messagebox.showinfo("Pedidos", "No existen pedidos registrados")
        return

    texto = ""

    for i in range(len(mostrarLista[0])):
        texto += f"""
Pedido #{i + 1}
Código: {mostrarLista[6][i]}
Nombre: {mostrarLista[0][i]} {mostrarLista[1][i]}
Teléfono: {mostrarLista[2][i]}
Dirección: {mostrarLista[3][i]}
Total sin IVA: ${mostrarLista[4][i]}
Total con IVA: ${mostrarLista[5][i]:.2f}
------------------------------
"""

    messagebox.showinfo("Lista de pedidos", texto)
#---------------------------------------------------------


ventana = tk.Tk() #ventana principal
ventana.title("Caja Registradora - Crear")  #titulo de la ventana
ventana.geometry("400x400") #medidas de la ventana... la vida es puro sufrimiento

'''
".pack()" hace que por defecto se ponga en un lugar de la ventana
"entry_nombre = tk.Entry(ventana)" por que va dentro de la ventana llamada "ventana"
'''
tk.Label(ventana, text="Nombre").pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

tk.Label(ventana, text="Apellido").pack()
entry_apellido = tk.Entry(ventana)
entry_apellido.pack()

tk.Label(ventana, text="Teléfono").pack()
entry_telefono = tk.Entry(ventana)
entry_telefono.pack()

tk.Label(ventana, text="Dirección").pack()
entry_direccion = tk.Entry(ventana)
entry_direccion.pack()

tk.Label(ventana, text="Paquete").pack()

#"tk.StringVar()" es una barrita pa que haya varias opciones, el set("ejemplito es el que va por defecto")
paquete_var = tk.StringVar()
paquete_var.set("PC + Monitor")

opciones = [
    "PC + Monitor",
    "PC + Monitor 4K",
    "Laptop Pro IA",
    "Servidor Potente"
]

#el "*opciones" es para que todas las opciones se traten como una sola y no como una lista, no quitar
tk.OptionMenu(ventana, paquete_var, *opciones).pack()

tk.Button(
    ventana, #pertenece a la ventana "ventana"
    text="Registrar",
    #cuanto se pulsa el boton se ejecuta la funcion llamada "registrar", sin parentesis para que se ejecute solo cuando se pulsa
    command=registrar, 
    bg="green",
    fg="white"
).pack(pady=10) #el pady es para que haya espacio verticalmente, 10 pixeles en este caso

tk.Button(
    ventana,
    text="Mostrar pedidos",
    command=mostrar_pedidos,
    bg="blue",
    fg="white"
).pack(pady=10)

#hace que la ventana se mantenga abierta, sin esto la ventana se abre y se cierra de una

ventana.mainloop()

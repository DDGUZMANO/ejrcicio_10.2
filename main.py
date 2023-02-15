# En este segundo ejercicio, tendréis que crear una interfaz sencilla la cual debe de contener una lista de elementos seleccionables, también debe de tener un label con el texto que queráis.

from tkinter import *
ventana = Tk()


def funcAgregar():
    lista.insert(END,txtProductos.get())

lista = Listbox(ventana)
for item in []:
    lista.insert(END, item)
pieDePagina = Label(ventana,text = 'Esta lista de mercado hará mas facil tu vida')
encabezado = Label(ventana,text='Lista para Mercado')
labelAgregarProductos = Label(ventana,text='Agregue acá sus productos')
entrada = StringVar
txtProductos = Entry(ventana, textvariable=entrada)
botonAgregar = Button(ventana,text='Agregar', command=funcAgregar)



encabezado.pack()
lista.pack()
labelAgregarProductos.pack(ipady=20)
txtProductos.pack()
botonAgregar.pack()
pieDePagina.pack()
ventana.mainloop()
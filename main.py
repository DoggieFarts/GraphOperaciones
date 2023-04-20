import tkinter
from tkinter import LEFT
from tkinter import *

top = tkinter.Tk()
top.geometry('500x500')
#L1 = tkinter.Label(top, text="Función objetivo")
#L1.pack(side = LEFT)
#E1 = Entry(top)
#E1.pack(side = RIGHT)

fObjetivo = tkinter.Frame(top)
def only_numbers(char):
    return char.isdigit()
validationNumber = fObjetivo.register(only_numbers)

def only_plus_or_minus(char):
    valido = False
    if(char == '+' or char == '-'):
        valido = True
    return valido
validationSing = fObjetivo.register(only_plus_or_minus)

fObjetivo.pack(pady=10,padx=10)
label1 = tkinter.Label(fObjetivo, text="Función objetivo: Z = ")
label1.grid(row = 0, column = 0, padx= 5, pady= 5)
# Entry para X1
entry1 = tkinter.Entry(fObjetivo, width=5, validate="key", validatecommand=(validationNumber, '%S'))
entry1.grid(row=0, column = 1)
# Label para X1
label2 = tkinter.Label(fObjetivo, text="X_1")
label2.grid(row = 0, column = 2, padx= 5, pady= 5)
# Entry para el signo
entry2 = tkinter.Entry(fObjetivo, width=3, validate="key", validatecommand=(validationSing,'%S'))
entry2.grid(row=0, column = 3)
# Entry para X2
entry3 = tkinter.Entry(fObjetivo, width=5, validate="key", validatecommand=(validationNumber, '%S'))
entry3.grid(row=0, column = 4, padx=7)
# Label para X2
label4 = tkinter.Label(fObjetivo, text="X_2")
label4.grid(row = 0, column = 5, padx= 5, pady= 5)

def agregarRestriccion():
    boton = tkinter.Button(top, text="Agregar restricción", command = agregarRestriccion)
    boton.pack()

top.mainloop()

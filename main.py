import tkinter
from tkinter import LEFT
from tkinter import *
from tkinter import messagebox
import numpy as np
from tokenize import tokenize, untokenize
from io import BytesIO

top = tkinter.Tk()
top.geometry('500x500')


def validacionNum(char):
        return char.isdigit()
validation = top.register(validacionNum)



def calcular():
    datosRes1 = []
    datosRes2 = []
    datosRes3 = []
    valorRes1 = restriccion1.get()
    valorRes2 = restriccion2.get()
    valorRes3 = restriccion3.get()

#Token de la restriccion 1:
    tokenRes1 = tokenize(BytesIO(valorRes1.encode('utf-8')).readline)
    non_empty = [t for t in tokenRes1 if t.line != '']
    for tokenRes1 in non_empty:
        datosRes1.append(tokenRes1.string)
    datosRes1 = np.array(datosRes1)
    print(datosRes1)
#Token de la restriccion 2
    tokenRes2 = tokenize(BytesIO(valorRes2.encode('utf-8')).readline)
    non_empty = [t for t in tokenRes2 if t.line != '']
    for tokenRes2 in non_empty:
       datosRes2.append(tokenRes2.string)
    datosRes2 = np.array(datosRes2)
    print(datosRes2)
#Token de la restriccion 3
    tokenRes3 = tokenize(BytesIO(valorRes3.encode('utf-8')).readline)
    non_empty = [t for t in tokenRes3 if t.line != '']
    for tokenRes3 in non_empty:
       datosRes3.append(tokenRes3.string)
    datosRes3 = np.array(datosRes3)
    print(datosRes3)





labelFunObj = tkinter.Label(top, text="Función objetivo")
labelFunObj.grid(row=0, column=0)
entryFunObj = tkinter.Entry(top).grid(row=0, column=1)

#Restriccion 1
labelNumRes=tkinter.Label(top,text="Restricción numero 1: ")
labelNumRes.grid(row=1,column=0)
restriccion1 = tkinter.Entry(top)
restriccion1.grid(row=1, column=1)
#Restriccion 2
labelNumRes=tkinter.Label(top,text="Restricción numero 2: ")
labelNumRes.grid(row=2,column=0)
restriccion2 = tkinter.Entry(top)
restriccion2.grid(row=2, column=1)
#Restriccion 3
labelNumRes=tkinter.Label(top,text="Restricción numero 3: ")
labelNumRes.grid(row=3,column=0)
restriccion3 = tkinter.Entry(top)
restriccion3.grid(row=3, column=1)



calcularButton = tkinter.Button(text="Calcular", command=calcular)
calcularButton.grid(row=4,column=0)








top.mainloop()

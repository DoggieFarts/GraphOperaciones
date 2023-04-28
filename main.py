import tkinter
from tkinter import LEFT
from tkinter import *
from tkinter import messagebox
import numpy as np

top = tkinter.Tk()
top.geometry('500x500')

def validacionNum(char):
        return char.isdigit()
validation = top.register(validacionNum)



def calcular():
    valorRes1 = restriccion1.get()
    valorRes2 = restriccion2.get()
    valorRes3 = restriccion3.get()
    print(valorRes1)





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

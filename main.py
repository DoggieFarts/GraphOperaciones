import tkinter
from tkinter import LEFT
from tkinter import *
from tkinter import messagebox
import numpy as np

top = tkinter.Tk()
top.geometry('500x500')
numero = 0
def validacionNum(char):
        return char.isdigit()
validation = top.register(validacionNum)

#def eliminarRest(int):
#    int = int-1
#    return int

def obtenerNum():
    numero = int(number_of_inputs.get())


    for j in range(numero):
      l=tkinter.Label(top,text="Restricciones" + str(j+1)).grid(row=j+3,column=0)
      e=tkinter.Entry(top, width=5).grid(row=j+3,column=1)
      l2=tkinter.Label(top, width=3,text="X_" + str(j+1)).grid(row=j+3,column=2) #label para x_1
      global e2
      e2 =tkinter.Entry(top, width=5).grid(row=j+3,column=3) #entry x_1
      # 1, 3, 5
      e3=tkinter.Entry(top, width=2).grid(row=j+3,column=4) #entry para signo
      e4=tkinter.Entry(top, width=5).grid(row=j+3,column=5) # entry para x_2
      l3=tkinter.Label(top, width=3,text="X_" + str(j+1)).grid(row=j+3,column=6) # label para x_2
      l4=tkinter.Label(top, width=3,text=" = ").grid(row=j+3,column=7) # label para =
      e5=tkinter.Entry(top, width=5).grid(row=j+3,column=8)
      #b = tkinter.Button(text="Eliminar restriccion", command=eliminarRest(numero)).grid(row=j+3, column=7)


def calcular():
    a = [e2 for x in range(numero)]
    print(a)

labelFunObj = tkinter.Label(top, text="Función objetivo")
labelFunObj.grid(row=0, column=0)
entryFunObj = tkinter.Entry(top).grid(row=0, column=1)

labelNumRes=tkinter.Label(top,text="Número de restricciones: ")
labelNumRes.grid(row=1,column=0)
number_of_inputs = tkinter.Entry(top, validate="key", validatecommand=(validation,"%S"))
number_of_inputs.grid(row=1,column=1)

obtenerNum = tkinter.Button(text="Obtener número de restricciones", command=obtenerNum)
obtenerNum.grid(row=2,column=0)

calcularButton = tkinter.Button(text="Calcular", command=calcular)
calcularButton.grid(row=2,column=1)








top.mainloop()

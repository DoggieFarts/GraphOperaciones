import tkinter
from tkinter import LEFT
from tkinter import *
from tkinter import messagebox

top = tkinter.Tk()
top.geometry('500x500')
numero = 0
def validacionNum(char):
        return char.isdigit()
validation = top.register(validacionNum)

def obtenerNum():
    numero = int(number_of_inputs.get())

    for j in range(numero):
      l=tkinter.Label(top,text="Restricciones" + str(j+1)).grid(row=j+3,column=0)
      e=tkinter.Entry(top).grid(row=j+3,column=1)



labelNumRes=tkinter.Label(top,text="Número de restricciones: ")
labelNumRes.grid(row=0,column=0)
number_of_inputs = tkinter.Entry(top, validate="key", validatecommand=(validation,"%S"))
number_of_inputs.grid(row=0,column=1)

obtenerNum = tkinter.Button(text="Obtener número de restricciones", command=obtenerNum)
obtenerNum.grid(row=2,column=0)

labelFunObj=tkinter.Label(top,text="Función objetivo")
labelFunObj.grid(row=1,column=0)
entryFunObj= tkinter.Entry(top).grid(row=1, column=1)






top.mainloop()

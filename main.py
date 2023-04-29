import tkinter
from tkinter import LEFT
from tkinter import *
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from tokenize import tokenize, untokenize
from io import BytesIO

top = tkinter.Tk()
top.geometry('500x500')

punto1Res1 = []
punto2Res1 = []
punto1Res2 = []
punto2Res2 = []
punto1Res3 = []
punto2Res3 = []
def validacionNum(char):
        return char.isdigit()
validation = top.register(validacionNum)

def graficar():
    plt.plot(punto2Res1,punto1Res1)
    plt.plot(punto2Res2, punto1Res2)
    plt.plot(punto2Res3, punto1Res3)
    plt.show()

def calcular():
    global datosRes1
    global datosRes2
    global datosRes3
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
    temp = int(datosRes1[6])
    temp2 = int(datosRes1[3])
    temp3 = temp/temp2
    punto1Res1.append(0)
    punto1Res1.append(temp3)
    print(punto1Res1[0])
    print(punto1Res1[1])
    temp = int(datosRes1[6])
    temp2 = int(datosRes1[0])
    temp3 = temp / temp2
    punto2Res1.append(temp3)
    punto2Res1.append(0)
    print(punto2Res1[0])
    print(punto2Res1[1])

#Token de la restriccion 2
    tokenRes2 = tokenize(BytesIO(valorRes2.encode('utf-8')).readline)
    non_empty = [t for t in tokenRes2 if t.line != '']
    for tokenRes2 in non_empty:
       datosRes2.append(tokenRes2.string)
    datosRes2 = np.array(datosRes2)#print(datosRes2)
    temp = int(datosRes2[6])
    temp2 = int(datosRes2[3])
    temp3 = temp / temp2
    punto1Res2.append(0)
    punto1Res2.append(temp3)#print(punto1Res2[0]) #print(punto1Res2[1])
    temp = int(datosRes2[6])
    temp2 = int(datosRes2[0])
    temp3 = temp / temp2
    punto2Res2.append(temp3)
    punto2Res2.append(0)#print(punto2Res2[0])#print(punto2Res2[1])
#Token de la restriccion 3
    tokenRes3 = tokenize(BytesIO(valorRes3.encode('utf-8')).readline)
    non_empty = [t for t in tokenRes3 if t.line != '']
    for tokenRes3 in non_empty:
       datosRes3.append(tokenRes3.string)
    datosRes3 = np.array(datosRes3)
    #print(datosRes3)
    temp = int(datosRes3[6])
    temp2 = int(datosRes3[3])
    temp3 = temp / temp2
    punto1Res3.append(0)
    punto1Res3.append(temp3)#print(punto1Res3[0])#print(punto1Res3[1])
    temp = int(datosRes3[6])
    temp2 = int(datosRes3[0])
    temp3 = temp / temp2
    punto2Res3.append(temp3)
    punto2Res3.append(0)#print(punto2Res3[0])#print(punto2Res3[1])

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

graficarButton =  tkinter.Button(text="Graficar", command=graficar)
graficarButton.grid(row=4, column=1)






top.mainloop()

import tkinter
from tkinter import LEFT
from tkinter import *
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
import math
from tokenize import tokenize, untokenize
from io import BytesIO

top = tkinter.Tk()
top.geometry('500x500')

def validacionNum(char):
        return char.isdigit()
validation = top.register(validacionNum)

#stringResCombinacion = ""
#stringResultado = ""
#combinacionFinal = 0
def my_reset():
    for widget in top.winfo_children():
        if isinstance(widget, tkinter.Entry):
            widget.delete(0, 'end')
        if isinstance(widget, tkinter.Radiobutton):
            seleccion.set(1)
        #if isinstance(widget, tkinter.Label):
            #widget.config(text=f"")

def graficar():
    plt.plot(punto2Res1, punto1Res1)
    plt.plot(punto2Res2, punto1Res2)
    plt.plot(punto2Res3, punto1Res3)
    plt.plot(punto1Inters1, punto2Inters1, marker="o")
    plt.plot(punto1Inters2, punto2Inters2, marker="o")
    plt.plot(punto1Inters3, punto2Inters3, marker="o")
    plt.plot(0, extremoY, marker="o")
    plt.plot(extremoX, 0, marker="o")
    #print(np.max(ys))
    #print(np.max(xs))
    #plt.figure()
    plt.grid()
    plt.show()
def calcular():
    global datosFuncObj
    global datosRes1
    global datosRes2
    global datosRes3
    global resultadoFinal
    combinacionFinal = 0
    datosFuncObj = []
    datosRes1 = []
    datosRes2 = []
    datosRes3 = []
    resultadoFinal = []
    valorFuncObj = entryFunObj.get()
    valorRes1 = restriccion1.get()
    valorRes2 = restriccion2.get()
    valorRes3 = restriccion3.get()
    global punto1Inters1
    global punto2Inters1
    global punto1Inters2
    global punto2Inters2
    global punto1Inters3
    global punto2Inters3
    global extremoY
    global extremoX
    global x1FuncObj
    global x2FuncObj
    global seleccion
    global punto1Res1
    global punto2Res1
    global punto1Res2
    global punto2Res2
    global punto1Res3
    global punto2Res3
    global xs
    global ys
    global stringResCombinacion
    global stringResultado
    global numResFinal
    punto1Res1 = []
    punto2Res1 = []
    punto1Res2 = []
    punto2Res2 = []
    punto1Res3 = []
    punto2Res3 = []
    xs = []
    ys = []
    stringResCombinacion = ""
    stringResultado = ""
    numResFinal = 0
#Token para la func objetivo
    tokenFuncObj = tokenize(BytesIO(valorFuncObj.encode('utf-8')).readline)
    non_empty = [t for t in tokenFuncObj if t.line != '']
    for tokenFuncObj in non_empty:
        datosFuncObj.append(tokenFuncObj.string)
    datosFuncObj = np.array(datosFuncObj)
    x1FuncObj = int(datosFuncObj[2])#valor de x1
    x2FuncObj = int(datosFuncObj[5])#valor de x2
    print(datosFuncObj[2]) #valor de x1
    print(datosFuncObj[5]) #valor de x2
#Token de la restriccion 1:
    tokenRes1 = tokenize(BytesIO(valorRes1.encode('utf-8')).readline)
    non_empty = [t for t in tokenRes1 if t.line != '']
    for tokenRes1 in non_empty:
        datosRes1.append(tokenRes1.string)
    datosRes1 = np.array(datosRes1)
    temp = float(datosRes1[6])
    temp2 = float(datosRes1[3])
    temp3 = temp/temp2
    punto1Res1.append(0)
    punto1Res1.append(temp3) #print(punto1Res1[0]) #print(punto1Res1[1])
    #punto1Res1 = np.array(punto2Res1)
    ys.append(temp3)
    #print(ys[0])
    temp = float(datosRes1[6])
    temp2 = float(datosRes1[0])
    temp3 = temp / temp2
    punto2Res1.append(temp3)
    xs.append(temp3)
    #print(xs[0])
    punto2Res1.append(0) #print(punto2Res1[0]) #print(punto2Res1[1])

#Token de la restriccion 2
    tokenRes2 = tokenize(BytesIO(valorRes2.encode('utf-8')).readline)
    non_empty = [t for t in tokenRes2 if t.line != '']
    for tokenRes2 in non_empty:
       datosRes2.append(tokenRes2.string)
    datosRes2 = np.array(datosRes2)#print(datosRes2)
    temp = float(datosRes2[6])
    temp2 = float(datosRes2[3])
    temp3 = temp / temp2
    punto1Res2.append(0)
    punto1Res2.append(temp3) #print(punto1Res2[0]) print(punto1Res2[1])
    ys.append(temp3)
    #print(ys[1])
    temp = float(datosRes2[6])
    temp2 = float(datosRes2[0])
    temp3 = temp / temp2
    punto2Res2.append(temp3)
    xs.append(temp3)
    #print(xs[1])
    punto2Res2.append(0)#print(punto2Res2[0])#print(punto2Res2[1])

#Token de la restriccion 3
    tokenRes3 = tokenize(BytesIO(valorRes3.encode('utf-8')).readline)
    non_empty = [t for t in tokenRes3 if t.line != '']
    for tokenRes3 in non_empty:
       datosRes3.append(tokenRes3.string)
    datosRes3 = np.array(datosRes3) #print(datosRes3)
    temp = float(datosRes3[6])
    temp2 = float(datosRes3[3])
    temp3 = temp / temp2
    punto1Res3.append(0)
    punto1Res3.append(temp3)#print(punto1Res3[1])print(punto1Res3[0])
    ys.append(temp3)
    #print(ys[2])
    temp = float(datosRes3[6])
    temp2 = float(datosRes3[0])
    temp3 = temp / temp2
    punto2Res3.append(temp3)
    xs.append(temp3)
    #print(xs[2])
    punto2Res3.append(0)#print(punto2Res3[0])#print(punto2Res3[1])
    #print("---")
    #print(np.max(ys))
    #print(np.max(xs))

    # intersección linea uno con línea dos
    value1 = float(datosRes1[0])
    value2 = float(datosRes1[3])
    value3 = float(datosRes2[0])
    value4 = float(datosRes2[3])
    value5 = float(datosRes1[6])
    value6 = float(datosRes2[6])
    A = np.array([[value1, value2], [value3,value4]])
    B = np.array([value5, value6])
    X = np.linalg.inv(A).dot(B)
    punto1Inters1 = X[0]
    punto2Inters1 = X[1]
    # intersección linea uno con línea tres
    value1 = float(datosRes1[0])
    value2 = float(datosRes1[3])
    value3 = float(datosRes3[0])
    value4 = float(datosRes3[3])
    value5 = float(datosRes1[6])
    value6 = float(datosRes3[6])
    A = np.array([[value1, value2], [value3, value4]])
    B = np.array([value5, value6])
    X = np.linalg.inv(A).dot(B)
    punto1Inters2 = X[0]
    punto2Inters2 = X[1]
    # intersección linea dos con línea tres
    value1 = float(datosRes2[0])
    value2 = float(datosRes2[3])
    value3 = float(datosRes3[0])
    value4 = float(datosRes3[3])
    value5 = float(datosRes2[6])
    value6 = float(datosRes3[6])
    A = np.array([[value1, value2], [value3, value4]])
    B = np.array([value5, value6])
    X = np.linalg.inv(A).dot(B)
    punto1Inters3 = X[0]
    punto2Inters3 = X[1]

    # evaluamos lo que tenga el radioButton, 1 es máximizar y 2 es minimizar
    if seleccion.get() == 1:
        extremoY = np.min(ys)
        extremoX = np.min(xs)
    elif seleccion.get() == 2:
        extremoY = np.max(ys)
        extremoX = np.max(xs)

    # Ahora calculamos el resultado para minimizar
    tempRes = (punto1Inters1 * x1FuncObj) + (punto2Inters1 * x2FuncObj)
    resultadoFinal.append(tempRes)
    tempRes = (punto1Inters2 * x1FuncObj) + (punto2Inters2 * x2FuncObj)
    resultadoFinal.append(tempRes)
    tempRes = (punto1Inters3 * x1FuncObj) + (punto2Inters3 * x2FuncObj)
    resultadoFinal.append(tempRes)
    # extremos
    tempRes = (0 * x1FuncObj) + (extremoY * x2FuncObj)
    resultadoFinal.append(tempRes)
    tempRes = (extremoX * x1FuncObj) + (0 * x2FuncObj)
    resultadoFinal.append(tempRes)
    #Calcular que restricción tenemos que evitar, siempre se evita la más pequeña
    #first = second = math.inf
    if seleccion.get() == 1: # máximizar
        first = second = resultadoFinal[0]
        for i in range(len(resultadoFinal), 0):
            if resultadoFinal[i] > first:
                first = resultadoFinal[i]
                #first = resultadoFinal[i]
                #combinacionFinal = i
            elif (resultadoFinal[i] > second and resultadoFinal[i] != first):
                second = resultadoFinal[i]
                combinacionFinal = i
        print(second)
        numResFinal = second
    elif seleccion.get() == 2: # minimizar
        first = second = math.inf
        for i in range(0, len(resultadoFinal)):
            if resultadoFinal[i] < first:
                second = first
                first = resultadoFinal[i]
            elif (resultadoFinal[i] < second and resultadoFinal[i] != first):
                second = resultadoFinal[i]
                combinacionFinal = i
        print(second)
        numResFinal = second
    #imprimimos el resultado
    if combinacionFinal == 0:
        stringResCombinacion = "La mejor combinación es con x1 = "+str(punto1Inters1)+" y con x2 = "+str(punto2Inters1)
        stringResultado = "Dando como resultado: "+str(numResFinal)+" unidades."
        #print("La mejor combinación es con x1 = "+str(punto1Inters1)+" y con x2 = "+str(punto2Inters1))
    elif combinacionFinal == 1:
        stringResCombinacion = "La mejor combinación es con x1 = "+str(punto1Inters2)+" y con x2 = "+str(punto2Inters2)
        stringResultado = "Dando como resultado: " + str(numResFinal) + " unidades."
        #print("La mejor combinación es con x1 = "+str(punto1Inters2)+" y con x2 = "+str(punto2Inters2))
    elif combinacionFinal == 2:
        stringResCombinacion = "La mejor combinación es con x1 = "+str(punto1Inters3)+" y con x2 = "+str(punto2Inters3)
        stringResultado = "Dando como resultado: " + str(numResFinal) + " unidades."
        #print("La mejor combinación es con x1 = "+str(punto1Inters3)+" y con x2 = "+str(punto2Inters3))
    elif combinacionFinal == 3:
        stringResCombinacion = "La mejor combinación es con x1 = 0 y con x2 = "+str(extremoY)
        stringResultado = "Dando como resultado: " + str(numResFinal) + " unidades."
        #print("La mejor combinación es con x1 = 0 y con x2 = "+str(extremoY))
    elif combinacionFinal == 4:
        stringResCombinacion = "La mejor combinación es con x1 = "+str(extremoX)+" y con x2 = 0"
        stringResultado = "Dando como resultado: " + str(numResFinal) + " unidades."
        #print("La mejor combinación es con x1 = "+str(extremoX)+" y con x2 = 0")
    #print(np.min(resultadoFinal))
    #función para obtener el segundo más chico de los resultados
    resCombEtiqueta = tkinter.Label(top, text=stringResCombinacion)
    resCombEtiqueta.grid(row=8, column=1)
    resEtiqueta = tkinter.Label(top, text=stringResultado)
    resEtiqueta.grid(row=9, column=1)
    print()

labelFunObj = tkinter.Label(top, text="Función objetivo")
labelFunObj.grid(row=0, column=0)
entryFunObj = tkinter.Entry(top)
entryFunObj.grid(row=0, column=1)
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

seleccion = tkinter.IntVar()
seleccion.set(1)
rBtnMax = tkinter.Radiobutton(top, text="Máximizar", variable=seleccion, value=1)
rBtnMax.grid(row=4, column=0)

rBtnMin = tkinter.Radiobutton(top, text="Minimizar", variable=seleccion, value=2)
rBtnMin.grid(row=4, column=1)

calcularButton = tkinter.Button(top, text="Calcular", command=calcular)
calcularButton.grid(row=5,column=0)

graficarButton = tkinter.Button(top, text="Graficar", command=graficar)
graficarButton.grid(row=5, column=1)

resetButton = tkinter.Button(top, text="Reset", command=lambda: my_reset())
resetButton.grid(row=5, column=2)

top.mainloop()





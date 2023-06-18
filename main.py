import tkinter
import numpy as np
import matplotlib.pyplot as plt
import math
from tokenize import tokenize
from io import BytesIO
from tkinter import *


top = tkinter.Tk()
top.geometry('800x600')

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
        if isinstance(widget, tkinter.Label):
            widget.config(text=f"")
        if isinstance(widget, tkinter.Label):
            widget.destroy()
    labelFunObj = tkinter.Label(top, text="Función objetivo", font=("Arial",16))
    labelFunObj.grid(row=0, column=0)
    labelNumRes = tkinter.Label(top, text="Restricción numero 1: ")
    labelNumRes.grid(row=1, column=0)
    labelNumRes = tkinter.Label(top, text="Restricción numero 2: ")
    labelNumRes.grid(row=2, column=0)

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
    ArregloOrdenado1 = []
    ArregloOrdenado2 = []
    ArregloOrdenado3 = []
    ArregloOrdenado4 = []
    valorFuncObj = entryFunObj.get()
    valorRes1 = restriccion1.get()
    valorRes2 = restriccion2.get()
    #valorRes3 = restriccion3.get()
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
    x1FuncObj = int(datosFuncObj[2])#valor de x1, aquí se guarda el 36
    x2FuncObj = int(datosFuncObj[5])#valor de x2, aquí se guarda el 40
    x3FuncObj = int(datosFuncObj[8])#valor de x3, aquí se guarda el 28

#Token de la restriccion 1:
    tokenRes1 = tokenize(BytesIO(valorRes1.encode('utf-8')).readline)
    non_empty = [t for t in tokenRes1 if t.line != '']
    for tokenRes1 in non_empty:
        datosRes1.append(tokenRes1.string)
    datosRes1 = np.array(datosRes1)
    # aquí ya tenemos

#Token de la restriccion 2
    tokenRes2 = tokenize(BytesIO(valorRes2.encode('utf-8')).readline)
    non_empty = [t for t in tokenRes2 if t.line != '']
    for tokenRes2 in non_empty:
       datosRes2.append(tokenRes2.string)
    datosRes2 = np.array(datosRes2)#print(datosRes2)

#datosRes1 y datosRes2
    ArregloOrdenado1.append(datosRes1[0]) # aquí se guarda el 6 pos0
    ArregloOrdenado1.append(datosRes2[0]) # aquí se guarda el 2 pos1
    ArregloOrdenado1.append(x1FuncObj)    # aquí se guarda el 36 pos2

    temp = float(ArregloOrdenado1[2])
    temp2 = float(ArregloOrdenado1[1])
    temp3 = temp/temp2

    punto1Res1.append(0)
    punto1Res1.append(temp3)
    # aquì guardas ys.append(temp3)
    ys.append(temp3)


    temp = float(ArregloOrdenado1[2])
    temp2 = float(ArregloOrdenado1[0])
    temp3 = temp/temp2

    punto2Res1.append(temp3)
    punto2Res1.append(0)
    xs.append(temp3)


    #hacemos división entre 36 y 2,y guardamos  punto1Res1.append(0) y  punto1Res1.append(resultado de la div) y guardamos el res en ys.append(temp3)
    #hacemos división entre 36 y 6,y punto2Res1.append(resultado de la div) guardamos  punto2Res1.append(0) y guardar el res de la div en xs.append(res de la div)

    ArregloOrdenado2.append(datosRes1[3]) # aquí se guarda el 5 res1
    ArregloOrdenado2.append(datosRes2[3]) # aquí se guarda el 5 res2
    ArregloOrdenado2.append(x2FuncObj)    # aquí se guarda el 40

    temp = float(ArregloOrdenado2[2])
    temp2 = float(ArregloOrdenado2[1])
    temp3 = temp/temp2

    punto1Res2.append(0)
    punto1Res2.append(temp3)
    ys.append(temp3)


    temp = float(ArregloOrdenado2[2])
    temp2 = float(ArregloOrdenado2[0])
    temp3 = temp/temp2

    punto2Res2.append(temp3)
    punto2Res2.append(0)
    xs.append(temp3)


    # hacemos la división entre 40 y 5 res 1, y guardamos punto1Res2.append(0) y punto1Res2.append(resultado de la div) y guardar el resultado en en ys.append(resultado de la div)
    # hacemos división entre 40 y 5 res 2, y guardamos  punto2Res2.append(temp3) y guardamos punto2Res2.append(0) y guardas xs.append(temp3)

    ArregloOrdenado3.append(datosRes1[6]) # aquí se guarda el 2 pos0
    ArregloOrdenado3.append(datosRes2[6]) # aquí se guarda el 4 pos1
    ArregloOrdenado3.append(x3FuncObj)    # aquí se guarda el 28 pos2

    temp = float(ArregloOrdenado3[2])
    temp2 = float(ArregloOrdenado3[1])
    temp3 = temp/temp2

    punto1Res3.append(0)
    punto1Res3.append(temp3)
    ys.append(temp3)


    temp = float(ArregloOrdenado3[2])
    temp2 = float(ArregloOrdenado3[0])
    temp3 = temp/temp2

    punto2Res3.append(temp3)
    punto2Res3.append(0)
    xs.append(temp3)



    #ahora guardamos los datos de la restricción
    ArregloOrdenado4.append(datosRes1[9])  # aquí se guarda el 5 para la func obj
    ArregloOrdenado4.append(datosRes2[9])  # aquí se guarda el 3 para la func obj

    #hacemos la división entre 28 y 4 y guardamos punto1Res3.append(0) y punto1Res3.append(temp3) y ys.append(temp3)
    #hacemos la división entre 28 y 2 y guardamos punto2Res3.append(temp3) y punto2Res3.append(0) y xs.append(temp3)
    #------------------------------- los valores ordenados se guardan bien
    # intersección linea uno con línea dos
    value1 = float(ArregloOrdenado1[0])
    value2 = float(ArregloOrdenado1[1])
    value3 = float(ArregloOrdenado2[0])
    value4 = float(ArregloOrdenado2[1])
    value5 = float(ArregloOrdenado1[2])
    value6 = float(ArregloOrdenado2[2])

    A = np.array([[value1, value2], [value3,value4]])
    B = np.array([value5, value6])
    X = np.linalg.inv(A).dot(B)
    punto1Inters1 = X[0]
    punto2Inters1 = X[1]
    # intersección linea uno con línea tres
    value1 = float(ArregloOrdenado1[0])
    value2 = float(ArregloOrdenado1[1])
    value3 = float(ArregloOrdenado3[0])
    value4 = float(ArregloOrdenado3[1])
    value5 = float(ArregloOrdenado1[2])
    value6 = float(ArregloOrdenado3[2])
    A = np.array([[value1, value2], [value3, value4]])
    B = np.array([value5, value6])
    X = np.linalg.inv(A).dot(B)
    punto1Inters2 = X[0]
    punto2Inters2 = X[1]
    # intersección linea dos con línea tres
    value1 = float(ArregloOrdenado2[0])
    value2 = float(ArregloOrdenado2[1])
    value3 = float(ArregloOrdenado3[0])
    value4 = float(ArregloOrdenado3[1])
    value5 = float(ArregloOrdenado2[2])
    value6 = float(ArregloOrdenado3[2])
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
    tempRes = (punto1Inters1 * float(ArregloOrdenado4[0])) + (punto2Inters1 * float(ArregloOrdenado4[1]))
    resultadoFinal.append(tempRes)
    tempRes = (punto1Inters2 * float(ArregloOrdenado4[0])) + (punto2Inters2 * float(ArregloOrdenado4[1]))
    resultadoFinal.append(tempRes)
    tempRes = (punto1Inters3 * float(ArregloOrdenado4[0])) + (punto2Inters3 * float(ArregloOrdenado4[1]))
    resultadoFinal.append(tempRes)
    # extremos
    tempRes = (0 * float(ArregloOrdenado4[0])) + (extremoY * float(ArregloOrdenado4[1]))
    resultadoFinal.append(tempRes)
    tempRes = (extremoX * float(ArregloOrdenado4[0])) + (0 * float(ArregloOrdenado4[1]))
    resultadoFinal.append(tempRes)

    #Calcular que restricción tenemos que evitar, siempre se evita la más pequeña
    #first = second = math.inf
    if seleccion.get() == 1: # 1-máximizar, pero ahora lo inventirmos
        first = second = 0
        for i in range(0, len(resultadoFinal)):
            if resultadoFinal[i] > first:
                second = first
                first = resultadoFinal[i]
                #first = resultadoFinal[i]
                #combinacionFinal = i
            elif (resultadoFinal[i] > second and resultadoFinal[i] != first):
                second = resultadoFinal[i]
                combinacionFinal = i

        numResFinal = second
    elif seleccion.get() == 2: # 2-minimizar, pero ahora lo inventirmos
        first = second = math.inf
        for i in range(0, len(resultadoFinal)):
            if resultadoFinal[i] < first:
                second = first
                first = resultadoFinal[i]
            elif (resultadoFinal[i] < second and resultadoFinal[i] != first):
                second = resultadoFinal[i]
                combinacionFinal = i

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
    resCombEtiqueta = tkinter.Label(top, text=stringResCombinacion, font=("Arial",15))
    resCombEtiqueta.grid(row=8, column=1)
    resEtiqueta = tkinter.Label(top, text=stringResultado, font=("Arial",15))
    resEtiqueta.grid(row=9, column=1)


labelFunObj = tkinter.Label(top, text="Función objetivo", font=("Arial",16))
labelFunObj.grid(row=0, column=0)
entryFunObj = tkinter.Entry(top)
entryFunObj.grid(row=0, column=1)
#Restriccion 1
labelNumRes=tkinter.Label(top,text="Restricción numero 1: ", font=("Arial",16))
labelNumRes.grid(row=1,column=0)
restriccion1 = tkinter.Entry(top)
restriccion1.grid(row=1, column=1)
#Restriccion 2
labelNumRes=tkinter.Label(top,text="Restricción numero 2: ", font=("Arial",16))
labelNumRes.grid(row=2,column=0)
restriccion2 = tkinter.Entry(top)
restriccion2.grid(row=2, column=1)
#Restriccion 3
#labelNumRes=tkinter.Label(top,text="Restricción numero 3: ", font=("Arial",16))
#labelNumRes.grid(row=3,column=0)
#restriccion3 = tkinter.Entry(top)
#restriccion3.grid(row=3, column=1)

seleccion = tkinter.IntVar()
seleccion.set(1)
rBtnMax = tkinter.Radiobutton(top, text="Minimizar", variable=seleccion, value=1)
rBtnMax.grid(row=4, column=0)

rBtnMin = tkinter.Radiobutton(top, text="Máximizar", variable=seleccion, value=2)
rBtnMin.grid(row=4, column=1)

calcularButton = tkinter.Button(top, text="Calcular", command=calcular)
calcularButton.grid(row=5,column=0)

graficarButton = tkinter.Button(top, text="Graficar", command=graficar)
graficarButton.grid(row=5, column=1)

resetButton = tkinter.Button(top, text="Reset", command=lambda: my_reset())
resetButton.grid(row=5, column=2)

instrucciones = tkinter.Label(top, text="Instrucciones de uso del programa\n 1.- Escribir función objetivo y restricciones de la manera \"Wx1+Wx2+Wx3\"\n 2.- Seleccionar a minimizar o a maximizar \n 3.- Dar click en cálcular \n 4.- Dar click en gráficar \n 5.- En caso de querer ingresar otro problema dar click en reset", font=("Arial",12), justify= LEFT)
instrucciones.grid(row=7,column=1)

top.mainloop()





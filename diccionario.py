# -*- coding: utf-8 -*-
#Rodrigo Becerra
texto="La Tabla de Sesiones es un documento en el que se detalla el conjunto de Proyectos de Ley u otras materias, que serán tratadas en una Sesión de la Cámara de Diputados. La Tabla se coloca a disposición de la ciudadanía antes del inicio de la Sesión."

listaTexto=texto.split() #Cada palabra del texto, la añade como un elemento de la lista

frecPalabras=[]

def Diccionario(listaTexto): #Funcion que retorna un diccionario
    for i in listaTexto:
        contador=0
        contador=listaTexto.count(i)
        frecPalabras.append(contador)
    return dict(zip(listaTexto,frecPalabras))

def OrdenDesc(frec): #Funcion que ordena los elementos de manera Descendente
    orden=[]
    for i in frec:
        orden.append([frec[i],i])
    orden.sort(reverse=True)
    return orden

diccionario=Diccionario(listaTexto)
diccFinal=OrdenDesc(diccionario)
print "Texto: ", texto
print "Diccionario: ", diccionario
print "Palabras más repetidas: "
for i in diccFinal:
    print i



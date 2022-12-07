#SGDI Practica 4 Ovidio Zea
"""Declaramos que esta solución es fruto exclusivamente de nuestro
trabajo personal. No hemos sido ayudados por ninguna otra persona
ni hemos obtenido la solución de fuentes externas, y tampoco hemos
compartido nuestra solución con otras personas. Declaramos además
que no hemos realizado de manera deshonesta ninguna otra actividad
que pueda mejorar nuestros resultados ni perjudicar los resultados
de los demás.
"""
import string
import os
from os.path import join, getsize
# Dada una linea de texto, devuelve una lista de palabras no vacias 
# convirtiendo a minusculas y eliminando signos de puntuacion por los extremos
# Ejemplo:
#   > extrae_palabras("Hi! What is your name? John.")
#   ['hi', 'what', 'is', 'your', 'name', 'john']
def extrae_palabras(linea):
  return filter(lambda x: len(x) > 0, 
    map(lambda x: x.lower().strip(string.punctuation), linea.split()))

class VectorialIndex2(object):
    def __init__(self, directorio):
        print(directorio)
        numDocs = 0
        archivos = {}
        indiceRepeticiones = {}
        for (root, dirs, files) in os.walk(directorio):
            for file in files:
                filePath = root+"/"+file
                archivos[numDocs] = filePath
                content = open(filePath, "r", encoding="ISO-8859-1", errors="replace")
                for line in content:
                    for palabra in extrae_palabras(line):
                        indiceRepeticiones[palabra]
                        print(palabra)
                numDocs += 1
        print("Total files: ", numDocs)
        print(archivos)
                #print(open(filePath, "r", encoding="ISO-8859-1").read())
                
        pass

class VectorialIndex(object):
    def __init__(self, directorio):
        print(directorio)
        numDocs = 0
        archivos = {}
        indiceRepeticiones = {"ejemplo": [(0,1), (1,2)]}
        if "ejemplo" in indiceRepeticiones :
            print("valor ejemplo: ",indiceRepeticiones.get("ejemplo")[0])
            indiceRepeticiones["ejemplo"].insert(0,(0,3))
            indiceRepeticiones["ejemplo"].insert(3,(5,3))
            indiceRepeticiones["ejemplo"].insert(3,(5,4))
            indiceRepeticiones["ejemplo"].insert(2,(2,100))
            indiceRepeticiones["ejemplo"][0] = (0,99) #posición cero de la lista 
            print("valor Tupla posicion 0: ",indiceRepeticiones["ejemplo"][0][1])
            print("valor Tupla posicion 5: ",indiceRepeticiones["ejemplo"][3][1])
        else :
            indiceRepeticiones["ejemplo2"] = [(0,3)]
        print("Total files: ", numDocs)
        print(archivos)
        print(indiceRepeticiones)
                #print(open(filePath, "r", encoding="ISO-8859-1").read())
                
        pass

    def consulta_vectorial(self, consulta, n=3):
        pass

    def consulta_conjuncion(self, consulta):
        pass

if __name__ == "__main__" :
    print("Ovidio")
    vec = VectorialIndex("C:/SGDI/SGDI4/20news-18828")
    #vec = VectorialIndex("/home/usuario_vms/Icaro/SGDI4/20news-18828")
    #vec = VectorialIndex("/home/usuario_vms/Icaro/SGDI4/mini_collection")
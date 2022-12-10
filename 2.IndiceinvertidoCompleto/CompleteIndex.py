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
import time
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


class CompleteIndex(object):
    indiceCompleto= {}
    archivos = {}

    def __init__(self, directorio, compresion=None):
        start_time = time.time()
        numDoc = 0  
        for (root, dirs, files) in os.walk(directorio):
            for file in files:
                filePath = root+"/"+file
                self.archivos[numDoc] = (filePath, 0)
                content = open(filePath, "r", encoding="ISO-8859-1", errors="replace")
                repeticionesTemp = {}
                position = 0
                for word in extrae_palabras(content.read()):                   
                    if word in repeticionesTemp :  #si ya existe la palabra en el indice                            
                        repeticionesTemp[word].append(position)                 
                    else :
                        repeticionesTemp[word] = [position]
                    position += 1
                for word in repeticionesTemp :
                    if word in self.indiceCompleto :
                        self.indiceCompleto[word].append((numDoc, repeticionesTemp[word]))
                    else :
                        self.indiceCompleto[word]  = [(numDoc, repeticionesTemp[word])]
                numDoc += 1
        #print(self.archivos)
        print("Total files: ", numDoc)
        #print(self.archivos)
        #print(self.indiceCompleto)
        print("--- %s seconds ---" % (time.time() - start_time))
        #print(open(filePath, "r", encoding="ISO-8859-1").read())
        pass

    def consulta_frase(self, frase):
        pass

    def num_bits(self):
        pass

if __name__ == "__main__" :
    #vec = CompleteIndex("C:/SGDI/SGDI4/20news-18828")
    vec = CompleteIndex("C:/SGDI/20news-18828")
    #print(vec.consulta_frase("DES Diffie-Hellman", n=5))
    #print(vec.consulta_conjuncion("DES Diffie-Hellman"))
    #vec = VectorialIndex("/home/usuario_vms/Icaro/SGDI4/20news-18828")
    #vec = VectorialIndex("/home/usuario_vms/Icaro/SGDI4/mini_collection")
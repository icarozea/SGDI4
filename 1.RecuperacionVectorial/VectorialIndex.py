# Insertar aqui la cabecera

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


class VectorialIndex(object):
    def __init__(self, directorio):
        print(directorio)
        for (root, dirs, files) in os.walk(directorio):
            for file in files:
                filePath = root+"/"+file
                print("files: ", filePath)
                print(open(filePath, "r", encoding="ISO-8859-1").read())
        pass

    def consulta_vectorial(self, consulta, n=3):
        pass

    def consulta_conjuncion(self, consulta):
        pass

if __name__ == "__main__" :
    print("Ovidio")
    vec = VectorialIndex("/home/usuario_vms/Icaro/SGDI4/20news-18828")
    #vec = VectorialIndex("/home/usuario_vms/Icaro/SGDI4/mini_collection")
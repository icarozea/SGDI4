# Insertar aqui la cabecera

import string
import os
import time
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
    indiceRepeticiones = {}
    archivos = {}

    def __init__(self, directorio):
        start_time = time.time()
        numDoc = 0 
        count  = 0       
        for (root, dirs, files) in os.walk(directorio):
            for file in files:
                filePath = root+"/"+file
                self.archivos[numDoc] = filePath
                content = open(filePath, "r", encoding="ISO-8859-1", errors="replace")
                for line in content:
                    for word in extrae_palabras(line):
                        if word in self.indiceRepeticiones :  #si ya existe la palabra en el indice                            
                            tuple = dict(self.indiceRepeticiones[word]).get(numDoc)
                            if tuple :# si ya existe el documento en la palabra
                                count += 1 
                                index = self.indiceRepeticiones[word].index((numDoc, tuple))
                                tuple += 1                        
                                self.indiceRepeticiones[word][index] = (numDoc,tuple)
                            else :
                                self.indiceRepeticiones[word].insert(numDoc,(numDoc,1))                        
                        else :
                            self.indiceRepeticiones[word] = [(numDoc,1)]
                numDoc += 1
        print("Total files: ", numDoc)
        #print(self.archivos)
        print("--- %s seconds ---" % (time.time() - start_time))
        #print(open(filePath, "r", encoding="ISO-8859-1").read())
                
        pass

    def consulta_vectorial(self, consulta, n=3):
        print(self.indiceRepeticiones)
        pass

    def consulta_conjuncion(self, consulta):
        pass

if __name__ == "__main__" :
    print("Ovidio")
    vec = VectorialIndex("C:/SGDI/SGDI4/20news-18828")
    #vec = VectorialIndex("C:/SGDI/20news-18828")
    vec.consulta_vectorial("mathew", n=5)
    #vec = VectorialIndex("/home/usuario_vms/Icaro/SGDI4/20news-18828")
    #vec = VectorialIndex("/home/usuario_vms/Icaro/SGDI4/mini_collection")
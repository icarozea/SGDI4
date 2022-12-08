# Insertar aqui la cabecera

import string
import os
import time
import math
from os.path import join, getsize
# Dada una linea de texto, devuelve una lista de palabras no vacias 
# convirtiendo a minusculas y eliminando signos de puntuacion por los extremos
# Ejemplo:
#   > extrae_palabras("Hi! What is your name? John.")
#   ['hi', 'what', 'is', 'your', 'name', 'john']
def extrae_palabras(linea):
  return filter(lambda x: len(x) > 0, 
    map(lambda x: x.lower().strip(string.punctuation), linea.split()))

def vectorPesos(vecList, totalFiles):
    for entradaDic in vecList:
        count = 0
        docs = len(vecList[entradaDic])
        #print(entradaDic,vecList[entradaDic])
        for Pareja in vecList[entradaDic] :
            # TF = 1+ log Frecuencia o 0 y IDF= log (documentos donde aparece/total documentos) peso=TF*IDF
            #print(Pareja)
            TF = 0
            if Pareja[1]>0:
                TF = 1 + math.log2(Pareja[1])
            IDF = math.log2(totalFiles/docs)
            TFIDF = TF*IDF 
            vecList[entradaDic][count] = (Pareja[0], TFIDF)
            count += 1
            
def normaFichero(DicList, VecList):
    for EntradaDic in VecList:
        for Pareja in VecList[EntradaDic] :
            DicList[Pareja[0]] = (DicList[Pareja[0]][0], DicList[Pareja[0]][1]+(Pareja[1]**2))
    for fichero in DicList:
        DicList[fichero] = (DicList[fichero][0], math.sqrt(DicList[fichero][1]))

def bestScore(k, scores):
    return sorted(scores.items(), key=lambda item: item[1], reverse=True)[0:k]


class VectorialIndex(object):
    indiceRepeticiones = {}
    archivos = {}
    def __init__(self, directorio):
        start_time = time.time()
        numDoc = 0  
        for (root, dirs, files) in os.walk(directorio):
            for file in files:
                filePath = root+"/"+file
                self.archivos[numDoc] = (filePath, 0)
                content = open(filePath, "r", encoding="ISO-8859-1", errors="replace")
                repeticionesTemp = {}
                for line in content:
                    for word in extrae_palabras(line):
                        if word in repeticionesTemp :  #si ya existe la palabra en el indice                            
                            repeticionesTemp[word] += 1                 
                        else :
                            repeticionesTemp[word] = 1
                for word in repeticionesTemp :
                    if word in self.indiceRepeticiones :
                        self.indiceRepeticiones[word].append((numDoc, repeticionesTemp[word]))
                    else :
                        self.indiceRepeticiones[word]  = [(numDoc, repeticionesTemp[word])]
                numDoc += 1
        vectorPesos(self.indiceRepeticiones, len(self.archivos))
        normaFichero(self.archivos, self.indiceRepeticiones)
        #print(self.archivos)
        #print("Total files: ", numDoc)
        #print(self.archivos)
        #print(self.indiceRepeticiones)
        print("--- %s seconds ---" % (time.time() - start_time))
        #print(open(filePath, "r", encoding="ISO-8859-1").read())
                
        pass

    def consulta_vectorial(self, consulta, n):
        scores = {}
        for word in extrae_palabras(consulta):
            if word in self.indiceRepeticiones:
                pesos = self.indiceRepeticiones[word]
                for (d,w) in pesos :
                    if d in scores :
                        scores[d] += w
                    else :
                        scores[d] = 0
                        scores[d] += w
        for d in scores :
            scores[d] = scores[d]/ self.archivos[d][1] #dividimos entre la norma

        best = {}
        for (d, val) in bestScore(n, scores):
            best[self.archivos[d][0]] = val

        return best

    def consulta_conjuncion(self, consulta):                
        List = extrae_palabras(consulta)
        PrimeraIteracion = True 
        resultado = list()
        for palabra in List :
            ListaParejas = self.indiceRepeticiones[palabra] 
            if PrimeraIteracion :
                resultado = ListaParejas
                PrimeraIteracion = False
            else :        
                Relementos = len(resultado) #numero de elementos candidato a resultado
                Lelementos = len(ListaParejas) #numero de ficheros que contienen una palabra especifica
                Riterador = 0
                Literador = 0
                resultado2 = list()
                while Riterador<Relementos and Literador<Lelementos :
                    if(ListaParejas[Literador][0]<resultado[Riterador][0]) :
                        Literador += 1
                    elif(ListaParejas[Literador][0]>resultado[Riterador][0]) :
                        Riterador += 1
                    else :
                        resultado2.append(resultado[Riterador])
                        Literador += 1
                        Riterador += 1
                resultado = resultado2
        LisrR = list()
        for (key, w) in resultado:
            LisrR.append(self.archivos[key][0]) 
        return LisrR

if __name__ == "__main__" :
    #vec = VectorialIndex("C:/SGDI/SGDI4/20news-18828")
    vec = VectorialIndex("C:/SGDI/20news-18828")
    print(vec.consulta_vectorial("DES Diffie-Hellman", n=5))
    print(vec.consulta_conjuncion("DES Diffie-Hellman"))
    #vec = VectorialIndex("/home/usuario_vms/Icaro/SGDI4/20news-18828")
    #vec = VectorialIndex("/home/usuario_vms/Icaro/SGDI4/mini_collection")

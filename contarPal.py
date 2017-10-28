#---------------------------- Imports ---------------------------------
from time import *
from re import *
from nltk.stem.snowball import SnowballStemmer
import os
#----------------------------------------------------------------------
stemmer = SnowballStemmer("spanish") # seleccionar el idioma del stemmer


inicio = time() # iniciar a contar segundos desde que se inician los algoritmos
lista = os.listdir("C:\\Users\\Luis Mora\\Desktop\\nltk-3.2.5\\spanish_billion_words\\sbw_00")
os.chdir("C:\\Users\\Luis Mora\\Desktop\\nltk-3.2.5\\spanish_billion_words\\sbw_00")
#print(lista)
for nombrearchivo in lista: #Recorre cada archivo que se encuentra en el directorio
    # Abrir archivo para lectura
    with open(nombrearchivo,encoding="utf8") as archivo:
        diccionarioPalabras = {} # diccionario para guardar ocurrencia de palabras
        terminos = {}
        frecuenciaTerminos = {} # diccionario para agrupar palabras según su longitud
        for linea in archivo:
            palabras = linea.split() # separar línea en palabras, por espacio en blanco
            for palabra in palabras:
                palabra = palabra.lower().strip(".,\n\t") # cambiar a minúscula y quitar puntuación
                if palabra not in diccionarioPalabras:
                    diccionarioPalabras[palabra] = 1
                else:
                    diccionarioPalabras[palabra] += 1
            #..............Hasta aqui 9 segundos...
            for termino in palabras:
                termino = stemmer.stem(termino)
            #print(palabra)
            if termino not in terminos:
                terminos[termino] = 1
            else:
                terminos[termino] += 1


                # Agrupar según longitud
                #longitud = len(palabra)
                #if longitud not in grupo:
                 #   grupo[longitud] = { palabra } # Usaremos un conjunto de palabras (sin repetir)
                #else:
                 #   grupo[longitud].add( palabra )

    # Cerrar archivo al finalizar
    archivo.close()
    print("archivo procesado: ", str(nombrearchivo) )
os.chdir("C:\\Users\\Luis Mora\\Desktop\\nltk-3.2.5")
dos = open("hmm.txt",'w+',encoding = "utf8")
for llave in diccionarioPalabras:
    dos.write(str(llave))
    dos.write(str(" : "))
    dos.write(str(diccionarioPalabras[llave]))
    dos.write('\n')
dos.close()
# Mostrar información
print('Total de palabras distintas:', len(diccionarioPalabras))

#print('Las diez palabras más comunes son:')
#for palabra in sorted( diccionarioPalabras, key = diccionarioPalabras.get, reverse=True )[:10]:
 #   print('\t',palabra,':',diccionarioPalabras[palabra],'ocurrencias')

final = time()
total = final - inicio
print("tiempo total: ",total, " segundos")
#for llave in diccionarioPalabras:
 #   print (llave, ": ", diccionarioPalabras[llave])

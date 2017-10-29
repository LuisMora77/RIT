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
diccionarioPalabras = {} # diccionario para guardar ocurrencia de palabras
terminos = {}
frecuenciaTerminos = {} # diccionario para agrupar palabras según su longitud
for nombrearchivo in lista: #Recorre cada archivo que se encuentra en el directorio
    with open(nombrearchivo,encoding="utf8") as archivo:
        #a = archivo.read()
        #archivo2 = sub('[^a-zá-úñ]',"",a)
        for linea in archivo:
            a = sub(r"(?:^|\s)(?=\S*[^\u0000-\u007FáéíóúüñÁÉÍÓÚÜÑ¿¡])\S+","",linea)
            palabras = a.split() # separar línea en palabras, por espacio en blanco
            for palabra in palabras:
                palabra = palabra.lower().strip(".,\n\t") # cambiar a minúscula y quitar puntuación
                if palabra not in diccionarioPalabras:
                    diccionarioPalabras[palabra] = 1
                    a = stemmer.stem(palabra)
                    if a not in terminos:
                        terminos[a] = [str(palabra)]
                    else:    
                        terminos[a] += [str(palabra)]
                    if a not in frecuenciaTerminos:
                        frecuenciaTerminos[a] = 1
                    else:
                        frecuenciaTerminos[a] +=1
                else:
                    diccionarioPalabras[palabra] += 1
    archivo.close()
    #print("archivo procesado: ", str(nombrearchivo), "Tiempo: ", time() - inicio )
os.chdir("C:\\Users\\Luis Mora\\Desktop\\nltk-3.2.5")
dos = open("hmm.txt",'w+',encoding = "utf8")
for llave in terminos:
    dos.write(str(llave))
    dos.write(str(" : "))
    dos.write(str(terminos[llave]))
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

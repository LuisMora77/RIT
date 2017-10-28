#---------------------------- Imports ---------------------------------
from time import *
from re import *
import stem
import os
#----------------------------------------------------------------------
"""
Ejemplo de uso de diccionario (estructura de datos) para contar palabras en un archivo
"""

'''
Leeremos un archivo de texto para hacer un resumen de la ocurrencia de las palabras
(cuántas veces aparece cada palabra en el texto). También agruparemos las palabras
según su cantidad de letras (longitud)
'''
inicio = time() # iniciar a contar segundos desde que se inician los algoritmos
#lista = os.listdir("C:\\Users\\Luis Mora\\Desktop\\pruebasRIT\\spanish_billion_words\\sbw_00")
os.chdir("C:\\Users\\Luis Mora\\Desktop\\pruebasRIT\\spanish_billion_words\\sbw_00")
#print(lista)
for i in lista:
    # Abrir archivo para lectura
    nombrearchivo = i
    with open(nombrearchivo,encoding="utf8") as archivo:
        palabrass = {} # diccionario para guardar ocurrencia de palabras
        terminos = {}
        grupo = {} # diccionario para agrupar palabras según su longitud
        for linea in archivo:
            palabras = linea.split() # separar línea en palabras, por espacio en blanco
            for palabra in palabras:
                palabra = palabra.lower().strip(".,\n\t") # cambiar a minúscula y quitar puntuación
                #print(palabra)
                if palabra not in palabrass:
                    palabrass[palabra] = 1
                else:
                    palabrass[palabra] += 1
                # Agrupar según longitud
                #longitud = len(palabra)
                #if longitud not in grupo:
                 #   grupo[longitud] = { palabra } # Usaremos un conjunto de palabras (sin repetir)
                #else:
                 #   grupo[longitud].add( palabra )

    # Cerrar archivo al finalizar
    archivo.close()

# Mostrar información
print('Total de palabras distintas:', len(palabrass))

print('Las diez palabras más comunes son:')
for palabra in sorted( palabrass, key = palabrass.get, reverse=True )[:10]:
    print('\t',palabra,':',palabrass[palabra],'ocurrencias')
final = time()
total = final - inicio
print("tiempo total: ",total, " segundos")
#for llave in palabrass:
 #   print (llave, ": ", palabrass[llave])

#Importacion de Mth para la raiz
import math
'''


Dada la siguiente estructura de datos

[(10,2), (8,7), (5,4), (3,11), (10,11)]

Use:
Función map
Dos funciones anónimas
que permita presentar en otra lista; para las primeras posiciones
la raiz cuadrada, para las segundas posiciones el cuadrado del número

'''
lista = [(10,2), (8,7), (5,4), (3,11), (10,11)]
#obtener posicion 0
raiz= lambda x: x[0] 
#obtener la poxsicion 1
cuadrado =lambda x: x[1]
#Funciones que aplica la raiz y el cuadrado a los valores de las posiciones 
funciones = lambda x: (math.sqrt(raiz(x)), cuadrado(x)**2)
#Impresion de datos
print(list(map(funciones, lista)))

'''
Dada la siguiente estructura de datos

[10,2,8,7,5,4,3,11,0, 1]

Use:
Función map
Una función anónima
que permita presentar en otra lista, cada elemento elevado a la tercera potencia
'''
lista= [10,2,8,7,5,4,3,11,0, 1]
#Creacion de la funcion que eleva cada elemento a la potencia 3
funcion= lambda x : x**3
'''a cada elemento de la lista realiza iteraciones aplicando 
la función y presenta en una lista
'''
print(list(map(funcion, lista)))


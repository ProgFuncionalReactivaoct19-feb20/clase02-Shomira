'''
Tuplas y uss del lambda
'''
datos = (
	(100, 170),
	(200, 180),
	)
#obtener la posicion 0
anios = lambda x: x[0]
#obtener la poxsicion 1
estatura =lambda x: x[1]
#operaciones dentro de la funcion lambda
funciones = lambda x: (anios(x)/12.0, estatura(x)/100)
#map permite iterar en una estructura una función 
print(list(map(funciones, datos)))
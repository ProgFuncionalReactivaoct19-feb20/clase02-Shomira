#Ejemplo y ussus del lambda 
#Cada elemento de datos, tiene(edad, estatura)
datos = ((30, 1.79), (25, 1.60), (35, 1.68))
#Funcion anonima Lambdab que recoge la posicion 2
dato = lambda x: x[2]
#Funcion anonima Lambdab que recoge la posicion 0
edad = lambda x: x[1] *100
'''
Envio de parametros a las funciones
realiza elanalisis y resolución de dentro hacia fuera
'''
print (edad(dato(datos)))
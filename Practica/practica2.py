'''
Desarrollar una función anónima que permita retornar la siguiente salida, ejemplo:

CUENCA capital de AZUAY

La llamada a la función es

print(cadena_personalizada("Cuenca", "Azuay"))
'''
#Creacion de la funcion anonima y concatenacion de una cadena 
cadena_personalizada = lambda x, y : "%s capital de  %s" %(x, y)
#Impresion de cadena 
print(cadena_personalizada( "CUENCA", "AZUAY"))
 

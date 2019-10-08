'''
Desarrollar la función anónima que retorne True or False si el número dado es par.

Ejemplo de llamada

print(valor_par(2))
print(valor_par(3))
print(valor_par(11))
'''
#Ingreso de datos
valor= input("Ingrese un valor ")
valor = int(valor)
'''Creacioón de la funcion anonima que retorna un boleano 
dada la condicion que la variable obtiene el residuo
''' 
valor_par = lambda x: x%2==0
#Imporesión de datos utilizando la funcion y envio de parametros
print(valor_par(valor))

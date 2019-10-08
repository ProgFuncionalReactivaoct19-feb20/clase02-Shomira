#Ejemplos de funciopn Lambda


lista =[10, 2, 3, 5]
#Se crea una funcion anonima Lambda que le da  a  x el valor de la lista en la posicion 2
mifuncion = lambda x: x[2]
#llamada a la funcion y se le pasa un parametro 
print(mifuncion(lista))
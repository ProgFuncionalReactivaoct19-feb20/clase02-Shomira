

lista = [10, 2, 3, 5]
funciones = lambda x: x+100
'''los datos de la lista lo aplica en la funcion´anonima 
   y obtiene el minimo
''' 
print(min(list(map(funciones, lista))))
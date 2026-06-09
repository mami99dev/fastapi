# La tupla es una coleccion ordenada, indexada e inmutable de elementos

my_tuple = (1, 2, 3, 4, 'Hola', True, False, 2, [1, 2], { 'name': 'Isaac' })

print(my_tuple)
# Acceder al numero de veces que aparece el valor en la tupla
print(my_tuple.count(2))
# Acceder al indice de la tupla donde aparece el valor
print(my_tuple.index('Hola'))

# Es inmutable
# my_tuple[1] = 20
# print(my_tuple)

# Las tuplas se recomienda usarse como una forma de tener valores fijos, por ejemplo:
week = ('Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo')

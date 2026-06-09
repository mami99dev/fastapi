# El diccionario se define como un tipo de dato que almacena informacion en pares clave valor, donde las claves deben ser strings, numeros o tuplas
user = {
  'name': 'Isaac',
  26: 'age',
  'email': 'isaacmar24@gmail.com',
  5.11: 'birthday',
  'active': True,
  (19.2, -98.36): "Cancun Mexico"
}

print(user)
# Actualizar un valor mediante la clave
user['name'] = 'Chaco'
# Acceder a un valor mediante su llave
print(user['name'])
# Agregar nuevo par clave valor
user['country'] = 'Mexico'
print(user)

# Acceder a los valores de un diccionario dados por una lista de los valores del diccionario [valor1, valor2, ...]
values = user.values()
# Acceder a los elementos de un diccionario dados por una lista de tuplas [(clave1, valor1), (clave2, valor2)...]
items = user.items()
# Acceder a las llaves de un diccionario dados por una lista de las llaves del diccionario [llave1, llave2, ...]
keys = user.keys()

print(values)
print(items)
print(keys)

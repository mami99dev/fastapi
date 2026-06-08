name = 'Isaac' # Se usa por convencion snake case en python
full_name = 'Isaac Martinez' # Los strings con comillas simples

_private_name = 'mami99' # Por convencion asi son las variables privadas
PI = 3.1416 # Por convencion las constantes son en mayusculas
GREET = 'Hola'

print(id(name)) # Se imprime el espacio (direccion) en memoria de la variable name 
print(hex(id(full_name))) # Espacio en memoria en hexadecimal
print(_private_name)
print(PI)
print(GREET + ' ' + full_name)
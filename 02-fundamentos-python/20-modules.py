import math_utils #$ Modulo math_utils
from my_package import messages #$ Paquete my_package con modulo messages

#! Al ejecutar el archivo 20-modules.py se genera una carpeta llamada __pycache__ que contiene archivos compilados de los modulos y paquetes que se importan. Esto es para optimizar la ejecución del código, guardandolas en cache.

#! Un modulo es un archivo .py que contiene código Python, mientras que un paquete es una carpeta que contiene un archivo __init__.py y otros módulos o subpaquetes.

result = math_utils.addition(3, 4)

print(result)
print(messages.greet('Isaac'))
print(messages.bye('Isaac'))
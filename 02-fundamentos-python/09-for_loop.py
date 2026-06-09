my_list = [1, 2, 3, 4, 5]
addition = 0

# El bucle for se usa para iterar sobre una secuencia de elementos que tienen fin
for number in my_list:
  print(number)
  addition += number
  
print(addition)

# El bucle for se puede usar con la funcion enumerate() para obtener el indice y el valor de cada elemento de una lista, tupla o set
for index, number in enumerate(list(range(100))):
  print(index, number*2)
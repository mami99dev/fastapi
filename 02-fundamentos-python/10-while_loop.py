# Es recomendable usar el ciclo while para cuando no sabes si tiene fin el ciclo

counter = 1

while counter <= 5:
  print(f'Number: {counter}')
  counter += 1
else:
  print('Terminamos')
  

response = ''
while response.lower() != 'bye':
  response = input('Escribe bye para salir: ')
else:
  print('Bueno bye')
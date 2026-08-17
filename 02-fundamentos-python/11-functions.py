# Parameters
def hello(greet='Hello', name='User'):
  print(f'{greet}, {name}')
  
# Arguments  
hello('Hola', 'Isaac')
hello('Ciao', 'Isaac')
hello()

# Keyword arguments
hello(name='Juan', greet='Hi')
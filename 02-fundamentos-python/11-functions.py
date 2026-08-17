# Parameters
def hello(greet='Hello', name='User'):
  print(f'{greet}, {name}')
  
# Arguments  
hello('Hola', 'Isaac')
hello('Ciao', 'Isaac')
hello()

# Keyword arguments
hello(name='Juan', greet='Hi')

# Args and Kwargs
def add(*args, **kwargs):
  print(args)
  print(kwargs)
  print(type(args))
  print(type(kwargs))
  result = 0
  element = 0
  while element < len(args):
    result = result + args[element]
    element = element + 1
    
  element = 0
  
  for element in kwargs:
    result = result + kwargs[element]
  return result
  
result = add(1, 2, 3, 4, 5, 6, 7, arg1=8, arg2=9, arg3=10)
print(result)
class Person:
  # Atributo publico global o de clase
  species = 'Humano'
  # Constructor
  def __init__(self, name, age):
    # Atributos publicos de instancia
    self.name = name
    self.age = age
    # Atributo protegido de instancia
    self._energy = 100
    # Atributo privado de instancia
    self.__password = '1234'
    
  # Metodo publico
  def work(self):
    return f'{self.name} esta trabajando duro'
  
  # Metodo protegido
  def _waste_energy(self, quantity):
    self._energy -= quantity
    return self._energy
  
  # Metodo privado
  def __generate_password(self):
    return f'$${self.name}_{self.age}$$'
  
  # Metodo publico que sirve para acceder a un atributo privado
  def get_password(self):
    return self.__password

  
# Instanciando la clase Person en el objeto person1
person1 = Person('Isaac', 26)

print(person1._energy) # Se puede acceder a un atributo protegido desde fuera de la clase, pero no es recomendable

print(person1._waste_energy(20)) # Se puede acceder a un metodo protegido desde fuera de la clase, pero no es recomendable, inclusive waste_energy puede ser un metodo publico

# No se puede acceder a un atributo privado, ni a un metodo privado desde fuera de la clase
# print(person1.__password) # Esto genera un error
# print(person1.__generate_password()) # Esto genera un error

# Una forma de acceder a un atributo privado y a un metodo privado desde fuera de la clase
print(person1._Person__password)
print(person1._Person__generate_password())

# Otra forma de acceder a los atributos privados es a traves de un metodo publico para acceder a ellos
print(person1.get_password())
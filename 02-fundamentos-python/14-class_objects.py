# Clase
class Person:
  # Constructor
  def __init__(self, name, age):
    # Atributos publicos
    self.name = name
    self.age = age
    
  # Metodo publico
  def work(self):
    return f'{self.name} esta trabajando duro'
  
# Instanciando la clase Person en el objeto person1
person1 = Person('Isaac', 26)
# Instanciando la clase Person en el objeto person2
person2 = Person('Juan', 63)

print(person1.name, person1.age, person1.work())
print(person2.name, person2.age, person2.work())
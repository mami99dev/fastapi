class Person:
  # Atributos de clase
  species = 'Humano'
  gender = 'Masculino'
  
  def __init__(self, name, age):
    # Atributos de instancia
    self.name = name
    self.age = age
  
  # Metodo de instancia
  def change_gender(self, new_gender):
    self.gender = new_gender
  
  # Metodo de clase
  @classmethod
  def change_species(cls, new_species):
    cls.species = new_species
    
  # Metodo estatico
  @staticmethod
  def is_adult(age):
    return age >= 18
  

person1 = Person('Isaac', 26)
person2 = Person('Juan', 63)

# ? ######################################################################################################################\
#! Atributos de instancia
# Una instancia puede acceder a un atributo de instancia, y si se cambia el valor del atributo de instancia, solo se cambia para esa instancia.
print(person1.age)

# Una clase no puede acceder a un atributo de instancia, porque no hay una instancia para acceder al atributo.
# print(Person.age) # Esto lanzará un error porque age es un atributo de instancia, no de clase (Person.__dict__ no tiene age)


# ? ######################################################################################################################
#! Atributos de clase
# Una instancia puede acceder a un atributo de clase, pero si se cambia el valor del atributo de clase a través de una instancia, se crea un nuevo atributo de instancia con el mismo nombre, y el atributo de clase original no se ve afectado. 
print(person1.species)
print(person1.__dict__)
person1.species = 'Androide Metahumano'
print(person1.species)
print(person1.__dict__)

# Una clase puede acceder a un atributo de clase, y si se cambia el valor del atributo de clase a través de la clase, se cambia para todas las instancias que no tengan un atributo de instancia con el mismo nombre.
print(Person.species)
Person.species = 'Androide Bot'
print(person2.species)


# ? ######################################################################################################################
#! Metodo de instancia
# Una instancia puede acceder a un método de instancia, y si se llama al método de instancia a través de una instancia, se pasa la instancia como primer argumento.
person1.change_gender('Femenino')
print(person1.gender)

# Una clase puede acceder a un método de instancia, pero si se llama al método de instancia a través de la clase, se debe pasar la instancia como primer argumento
Person.change_gender(person2, 'Masculino')
print(person2.gender)


# ? ######################################################################################################################
#! Metodo de clase
# Una instancia puede acceder a un método de clase, pero con un proceso interno por detras:
# Python permite acceder a metodos de clase a través de una instancia. La instancia se usa como puente para encontrar el método de clase, pero no se pasa como argumento. El primer argumento de un método de clase es la clase, no la instancia.
# 1.- Busca change_species en person1, no lo encuentra ahí
# 2.- Lo busca en la clase Person, lo encuentra
# 3.- Ve que es un classmethod, así que igual pasa cls=Person (la clase de person1), no person1
person1.change_species('Bot')
print(person1.species)

# Una clase puede acceder a un método de clase, y si se llama al método de clase a través de la clase, se pasa la clase como primer argumento por detras, esto modifica el atributo de clase en todas las instancias.
Person.change_species('Reptiliano')
print(person1.species)
print(person2.species)


# ? ######################################################################################################################
#! Metodo estatico
# Los métodos estáticos no reciben ni la instancia ni la clase como primer argumento (self, cls). Son métodos que se pueden llamar tanto desde la clase como desde la instancia.
# Una instancia puede acceder a un método estático, y si se llama al método estático a través de una instancia, no se pasa la instancia como primer argumento.
print(person1.is_adult(person1.age))

# Una clase puede acceder a un método estático, y si se llama al método estático a través de la clase, no se pasa la clase como primer argumento.
print(Person.is_adult(17))


# ? ######################################################################################################################
#! Como encontrar los atributos de clase, metodos de clase, atributos de instancia, métodos de instancia y metodos estaticos
print('###########        Como encontrar los atributos y métodos de instancia, clase y estáticos          ###########')
# los métodos (clase, instancia y estaticos) nunca existen en las instancias, solo los atributos (de clase y de instancia). Los métodos existen en la clase y si puedes acceder a ellos a traves de la instancia (person1.change_species() o person1.change_gender()), pero python lo hace por un proceso interno.
attributes_in_instance = []
for attribute in person1.__dict__:
  if attribute.startswith('__'):
    continue
  attributes_in_instance.append(attribute)
print(f'attributes_in_instance: {attributes_in_instance}')

# Los métodos de clase, atributos de clase, metodos de instancia y metodos estaticos existen en la clase, pero los atributos de instancia no existen en la clase
methods_and_attributes_in_class = []
for method_or_attribute in Person.__dict__:
  if method_or_attribute.startswith('__'):
    continue
  methods_and_attributes_in_class.append(method_or_attribute)
print(f'methods_and_attributes_in_class: {methods_and_attributes_in_class}')

# Si quieres aceder a los atributos de clase, metodos de clase, atributos de instancia, métodos de instancia y metodos estaticos a través de una instancia, puedes usar dir() para obtener todos los métodos y atributos disponibles.
all_methods_and_attributes = []
for method_or_attribute in dir(person1):
  if method_or_attribute.startswith('__'):
    continue
  all_methods_and_attributes.append(method_or_attribute)
print(f'all_methods_and_attributes: {all_methods_and_attributes}')
##! Todo en python es un objeto

list_numbers = [1, 2, 3, 4, 5, 2, 2, 2]
list_letters = ['a', 'b', 'c', 'd']
list_mix = [2, 'z', True, [1, 2, 3], 5.5]
shopping_cart = ['Laptop', 'Silla gamer', 'Cafe']

print(type(list_mix))

# APPEND
print(list_numbers)
list_numbers.append(100)
list_numbers.append(200)
print(list_numbers)

# REMOVE (value)
list_numbers.remove(4)
print(list_numbers)

# COUNT (value)
a = list_numbers.count(2)
print(a)

# COPY
new_list = list_numbers.copy()
print(new_list)

# SORT
list_numbers.sort()
print(list_numbers)
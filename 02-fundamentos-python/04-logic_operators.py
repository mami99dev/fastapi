# AND
age = 26
licensed = True

if age >= 18 and licensed:
  print('Puedes manejar')
  
# OR
is_student = False
membership = True

if is_student or membership:
  print('Obtiene precio especial')
  
# NOT
is_admin = False
if not is_admin:
  print('Acceso denegado')

# SHORT CIRCUITING
name = 'Isaac'
print(name and name.upper())

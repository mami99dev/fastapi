# Un decorador es una forma elegante de modificar el comportamiento de una funcion sin cambiar su codigo
def require_auth(greet_function):
  def wrapper(user):
    if user.lower() == 'admin':
      return greet_function(user)
    else:
      return 'Acceso denegado'

  print('Cargando...')
  return wrapper

@require_auth
# Este decorador va a encapsular la funcion admin_dashboard y lo manda como argumento a require_auth
def admin_dashboard(user):
  return f'Bienvenido al panel, {user}'

# Por detras python hace lo siguiente:
# admin_dashboard = require_auth(admin_dashboard)

print(admin_dashboard('Admin'))
print(admin_dashboard('User'))
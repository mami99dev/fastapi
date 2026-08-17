# High order function
# Las funciones de orden superior reciben como argumento una funcion y devuelven otra funcion
def require_auth(greet_function):
  def wrapper(user):
    if user.lower() == 'admin':
      return greet_function(user)
    else:
      return 'Acceso denegado'
  
  # El hilo de ejecucion se salta hasta este punto
  print('Cargando...')
  return wrapper

def admin_dashboard(user):
  return f'Bienvenido al panel, {user}'

# require_auth devuelve una funcion, por lo tanto auth_view_dashboard se convierte en la declaracion de la funcion wrapper que es la que se devuelve en este caso
auth_view_dashboard = require_auth(admin_dashboard)

print(auth_view_dashboard('Admin'))
print(auth_view_dashboard('User'))
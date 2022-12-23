import request

def run():
  nombre_completo = request.pedirNombre()
  fecha_nacimiento = request.pedirFecha()
  direccion = request.pedirEspecificaciones("Ingrese su direccion: ")
  metas = request.pedirEspecificaciones("Ingrese sus metas: ")

  #SALIDA DE DATOS
  print(f"Tu nombre completo es: {nombre_completo}")
  print(f"Tu fecha de nacimiento es: {fecha_nacimiento}")
  print(f"Tu direccion es: {direccion}")
  print(f"Tus metas son: {metas}")

while(True):
  run()
  salir = input("Si desea terminar el programa presione 'X' de lo contrario presione 'ENTER': ").lower()
  if salir=="x": break;

import request
import calculte

def run():
  #Ingrese su fecha de nacimiento
  fecha_nacimiento = request.pedirFecha()

  #obtener dias
  dias = calculte.obtenerDias(fecha_nacimiento)

  #salida
  if dias == 0 : print("Feliz Cumpleaños!")
  else: print(f"Faltan {dias} dias para tu cumpleaños") 

if __name__ == "__main__":
  run()
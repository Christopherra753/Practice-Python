from datetime import datetime

def pedirNombre():
  while True:
    nombre:str = input("Ingrese su nombre completo: ")
    nombre_validar = nombre.replace(" ","")
    if nombre_validar.isalpha(): return nombre
    else: print("Ingrese un nombre correcto!")

def pedirFecha():
  while True:
    fecha_cadena = input("Ingrese su fecha de nacimiento en el siguiente formato[dd-mm-yyyy]: ")
    try:
      fecha_nacimiento = datetime.strptime(fecha_cadena,"%d-%m-%Y")
      fecha_actual = datetime.now()
      if fecha_actual > fecha_nacimiento: return fecha_nacimiento.strftime("%b %d, %Y")
      else: raise Exception("La fecha de nacimiento no puede ser superior a la fecha actual!")
    except ValueError:
      print("El formato que ingreso es erroneo, intentelo nuevamente!")
    except Exception as e:
      print(e)

def pedirEspecificaciones(mensaje):
  especificacion = input(mensaje)
  return especificacion


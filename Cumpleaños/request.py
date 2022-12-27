import datetime

def pedirFecha():
  while True:
    fecha_cadena:str = input("Ingrese su fecha de nacimiento en el formato [yyyy-mm-dd]: ")
    try:
      fecha_nacimiento = datetime.date.fromisoformat(fecha_cadena)
      fecha_actual = datetime.date.today()
      
      if fecha_nacimiento >= fecha_actual: raise Exception("La fecha de nacimiento no puede ser igual o superior a la fecha actual!") 
      else: return fecha_nacimiento
    except ValueError:
      print("Formato erroeno!")
    except Exception as e:
      print(e)



#Importaciones para validar los numeros
import validaciones


def run():
  print("BIENVENIDOS AL JUEGO PAR O IMPAR")
  value = validaciones.requestValue()

  if value%2==0:
    print(f"El numero {value} es PAR")
  else:
    print(f"El numero {value} es IMPAR")


while(True):
  run()
  salir = input("Si desea terminar el programa presione 'X' de lo contrario presione 'ENTER': ").lower()
  if salir=="x": break;




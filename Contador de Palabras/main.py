import random
import escribir


def run():
  questions = ["¿Cómo estas el día de hoy?","¿Cuentame de tu día?","¿País al que quisieras viajar y por qué?","¿En qué estas pensando?"]
  description = input(f"{random.choice(questions)}: ")
  escribir.write_txt(description,"Contador de Palabras/texto.txt")
  length = len(description.split(" "))
  print(f"Excelente, Me expresaste tus pensamientos en {length} palabras!")


while(True):
  run()
  salir = input("Si desea terminar el programa presione 'X' de lo contrario presione 'ENTER': ").lower()
  if salir=="x": break;
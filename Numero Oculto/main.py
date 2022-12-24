import request
def run():
  numero_oculto = request.generatorNumber()
  intentos = 0
  while True:
    #aumentamos en 1 el numero de intentos
    intentos+=1

    #Pide que ingrese un numero entre el rango o la x para rendirce
    numero_ingresado = request.requestValue()

    #Verifica si se rindio o no el jugador
    if numero_ingresado == None:
      print(f"El numero oculto era {numero_oculto} pero se rindio en el intento numero {intentos}")
      break

    #Verifica si los numeros coinciden
    if numero_ingresado == numero_oculto:
      print(f"El numero oculto es {numero_oculto} y le tomo {intentos} intentos!")
      break

if __name__ == "__main__":
  run()
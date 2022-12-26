def pedirPalabra():
  while True:
    palabra:str = input("Ingrese una palabra: ")
    palabra_validar = palabra.replace(" ","")
    if palabra_validar.isalpha(): return palabra.lower()
    else: print("Ingrese un palabra correcta!")


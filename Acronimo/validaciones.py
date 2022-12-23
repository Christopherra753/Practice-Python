def requestInformation():
  while True:
    information = input("Ingrese el significado completo de una organizacion o concepto: ")
    information_validar = information.replace(" ","")
    if information_validar.isalpha(): return information
    else: print("Valor erroneo, intentelo nuevamente!")

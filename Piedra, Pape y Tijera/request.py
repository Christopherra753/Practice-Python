
options = ["piedra","papel","tijera"]
def requestOption():
  while True:
    opcion:str = input("Ingrese una opcion [piedra, papel o tijera]: ")
    if opcion in options: return opcion
    else: print("Opcion erronea, intentalo de nuevo!")

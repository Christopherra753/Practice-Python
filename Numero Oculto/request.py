import random
def requestValue():
  while True:
    try:
      value: str = input("Ingrese un numero del 1 al 50 o x para : ").lower()
      if (value == "x"):
        return None
      value_validation = int(value)
      if (value_validation<0 or value_validation>50): raise Exception("Fuera de rango!")
      return value_validation
    except ValueError:
      print("Ingrese un valor correcto!")
    except Exception as e:
      print(e)


def generatorNumber():
  numero = random.randint(1,50)
  return numero


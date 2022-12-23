def requestValue():
  while True:
    try:
      value: int = int(input("Ingrese un numero del 1 al 1000: "))
      if (value<0 or value>1000): raise Exception("Fuera de rango!")
      return value
    except ValueError:
      print("Ingrese un valor correcto!")
    except Exception as e:
      print(e)



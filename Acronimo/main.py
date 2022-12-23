import validaciones
import getAcronym
import escribir

def run():
  valor = validaciones.requestInformation()
  acronimo = getAcronym.get_result(valor)
  escribir.write_txt(valor,acronimo,"Acronimo/Acronimos.txt")
  print(f"El acronimo es: {acronimo}")

if __name__ == "__main__":
  run()


  





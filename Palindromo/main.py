import request
import calculate

def run():
  #TITULO
  print("INGRESE 4 PALABRAS PARA VER SI SON PALINDORMOS")

  #pedir palabras validas
  palabra1 = request.pedirPalabra()
  palabra2 = request.pedirPalabra()
  palabra3 = request.pedirPalabra()
  palabra4 = request.pedirPalabra()
  

  #calcular si son palindromos
  respuesta1 = calculate.esPalindromo(palabra1)
  respuesta2 = calculate.esPalindromo(palabra2)
  respuesta3 = calculate.esPalindromo(palabra3)
  respuesta4 = calculate.esPalindromo(palabra4)

  #salida
  print(f"La palabra '{palabra1}' ¿Es palindromo?: {respuesta1}")
  print(f"La palabra '{palabra2}' ¿Es palindromo?: {respuesta2}")
  print(f"La palabra '{palabra3}' ¿Es palindromo?: {respuesta3}")
  print(f"La palabra '{palabra4}' ¿Es palindromo?: {respuesta4}")




if __name__ == "__main__":
  run()
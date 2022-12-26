def esPalindromo(palabra):
  palabra_invertida = palabra[::-1]
  if palabra_invertida == palabra: return "Verdadero"
  else: return "Falso"
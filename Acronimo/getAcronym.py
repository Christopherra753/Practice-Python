def get_result(valor):
  acronimo = ""
  array_valor = valor.split(" ")
  for valor in array_valor:
    acronimo += valor[0]
  return acronimo.upper()
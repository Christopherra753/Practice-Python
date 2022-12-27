import datetime

def obtenerDias(fecha_nacimiento:datetime.date):
  fecha_actual = datetime.date.today()
  fecha_cumpleaños = fecha_nacimiento.replace(year=fecha_actual.year)

  if fecha_cumpleaños == fecha_actual:
    return 0
  if fecha_cumpleaños > fecha_actual:
    return (fecha_cumpleaños-fecha_actual).days
  if fecha_cumpleaños < fecha_actual:
    return 365 - (fecha_actual-fecha_cumpleaños).days  

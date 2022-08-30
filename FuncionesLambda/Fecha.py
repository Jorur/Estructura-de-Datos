#Mostrar Hora con lambda
from datetime import datetime

ahora = datetime.now()
print(ahora)

extraer= lambda f: (f.year, f.month, f.day)
resultado = extraer(ahora)

print(resultado)
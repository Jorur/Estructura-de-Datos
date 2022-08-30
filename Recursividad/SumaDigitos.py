#Crear un programa para sumar los digitos de un numero con recursividad.
def SumarDigitos(n):
    if n == 0:
        return 0

    else:
        return n%10 + SumarDigitos(n//10)

print(SumarDigitos(1234567))


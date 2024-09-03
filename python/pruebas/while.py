import math

numero = int(input("Ingrese un numero: "))

while numero<0:
    print("Ingrese un numero positivo")
    numero = int(input("Ingrese un numero: "))
    
print("El numero que ingreso fue ",numero)
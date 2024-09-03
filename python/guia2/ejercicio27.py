n1 = 1
n2 = 2
n3 = 3
n4 = 4
n5 = 5

suma = n1 + n2 + n3 + n4 + n5

prom = suma/5

print("el promedio es {}".format(prom))

suma1 = 0

# Solicitamos 5 números al usuario
for i in range(5):
    numero = int(input(f"Ingrese el número {i+1}: "))
    suma1 += numero  # Sumamos el número ingresado a la variable suma

# Calculamos el promedio dividiendo la suma por 5
promedio = suma1 / 5

# Mostramos el promedio en pantalla
print("El promedio de los 5 números ingresados es:", promedio)
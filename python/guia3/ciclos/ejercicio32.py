tabla = [0, 1, 2, 3, 4 ,5, 6, 7, 8 ,9 ,10]
numero = int(input("Ingrese un numero: "))

if numero > 0 and numero<=10:
    for i in tabla:
        print(numero*tabla[i])
else:
    print("ingrese un numero entre 1 y 10")
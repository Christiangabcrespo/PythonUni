num = int(input("Ingrese un numero: "))
limite = num+1

for i in range(1, limite):
    if i%2 == 0:
        print("Es par")
    else: 
        print("Es impar")
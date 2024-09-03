def imprimir_tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

def tablas_de_multiplicar():
    print("¡Hola! Esto es Tablas de Multiplicar")
    
    continuar = True
    while continuar:
        entrada = input('Ingrese un número o "X" para salir: ').strip()
        
        if entrada.upper() == "X":
            continuar = False
            print("¡Adios!")
        else:
            try:
                numero = int(entrada)
                if 1 <= numero <= 10:
                    imprimir_tabla_multiplicar(numero)
                else:
                    print("Error: El número debe ser positivo y estar entre 1 y 10")
            except ValueError:
                print("Error: Debe ingresar un número válido o 'X' para salir.")

# Ejemplo de uso
tablas_de_multiplicar()
def rendir_gastos():
    num_personas = int(input("Ingrese la cantidad de personas que van a rendir gastos: "))
    gastos_totales = []
    max_gasto = 0

    for i in range(1, num_personas + 1):
        print(f"\nIngrese los gastos de la persona {i}:")
        gasto = -1  # Inicializamos gasto con un valor que no sea 0
        gastos_persona = 0
        
        while gasto != 0:
            gasto = float(input("Ingrese el monto del gasto (o 0 para finalizar): "))
            if gasto != 0:
                gastos_persona += gasto
                if gasto > max_gasto:
                    max_gasto = gasto

        gastos_totales.append(gastos_persona)

    total_gastos = sum(gastos_totales)
    promedio_gastos = total_gastos / num_personas if num_personas > 0 else 0

    print("\nResumen de los gastos:")
    print(f"Gasto más alto: {max_gasto}")
    print(f"Promedio de gasto por persona: {promedio_gastos:.2f}")
    print(f"Total de gastos: {total_gastos:.2f}")

# Llamada a la función
rendir_gastos()
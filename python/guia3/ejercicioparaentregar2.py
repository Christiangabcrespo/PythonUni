def rendir_gastos():
    # 1. Se pide al usuario que ingrese cuántas personas serán
    num_personas = int(input("Ingrese cuántas personas van a rendir gastos: "))
    gastos_totales = []
    max_gasto = 0
    persona_max_gasto = ""

    for i in range(1, num_personas + 1):
        print(f"\nIngrese los gastos de la persona {i}:")
        gastos_persona = 0
        terminar = "no"  # Inicializamos con un valor distinto de "si"

        while terminar.lower() != "si":
            # 2. Validación de que no se ingresen montos negativos
            gasto = float(input("Ingrese el monto del gasto: "))
            if gasto < 0:
                print("Error: El monto no puede ser negativo. Intente nuevamente.")
                continue
            
            gastos_persona += gasto
            if gasto > max_gasto:
                max_gasto = gasto
                persona_max_gasto = f"Persona {i}"

            # 3. Preguntar si terminó de ingresar los gastos
            terminar = input("¿Terminó de ingresar los gastos? (Si/No): ")

        gastos_totales.append(gastos_persona)

    total_gastos = sum(gastos_totales)
    promedio_gastos = total_gastos / num_personas if num_personas > 0 else 0

    print("\nResumen de los gastos:")
    print(f"Gasto más alto: {max_gasto}")
    print(f"Promedio de gasto por persona: {promedio_gastos:.2f}")
    print(f"Total de gastos: {total_gastos:.2f}")
    # 4. Mostrar quién fue la persona que gastó más
    print(f"La persona que gastó más fue: {persona_max_gasto}")

# Llamada a la función
rendir_gastos()
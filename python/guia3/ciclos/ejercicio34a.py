def cobro_supermercado(totalAPagar):
    print("Su total a pagar es: ", totalAPagar)
    pendiente = totalAPagar
    
    while pendiente > 0:
        monto = int(input("Ingrese el monto a pagar: "))
        
        if monto <= pendiente:
            pendiente -= monto
            print("pendientes: ",pendiente)
        elif monto == pendiente:
            pendiente -= monto
            print("El monto ingresado es mayor al pendiente, Ingrese nuevamente")
        else:
            vuelto = monto - pendiente
            pendiente = 0
            print("pendientes: ",pendiente," su vuelto es: ",vuelto)
    
    print("Gracias por su compra")
    
total = 500

cobro_supermercado(total)
letra = input("Ingrese roca R, papel P o tijera T: ")

letraMayus = letra.upper()

def jugada():
    if letraMayus == 'R':
        print("Papel, gane")
    elif letraMayus == 'P':
        print("Tijera, gane")
    elif letraMayus == 'T':
        print("Roca, gane")
    else:
        print("ingrese un valor valido")
        
jugada()
letra = input("Ingrese una letra: ")
letra2 = input("Ingrese una letra: ")
letra = letra.lower()
def vocal():
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        print(True)
    else:
        print(False)

vocal() 

def vocal2():
    if 'a' not in letra and 'e' not in letra and 'i' not in letra and 'o' not in letra and 'u' not in letra:
        print(True)
    else:
        print(False)
        
vocal2()

def mayusominus():
    if letra2 == letra2.upper():
        print("Es mayuscula")
    elif letra2 == letra2.lower():
        print("es minuscula")
        
mayusominus()
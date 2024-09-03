celcius = int(input("ingrese temperatura en celcius: "))
farenheit = int(input("Ingrese temperatura en farenheit: "))

def cambiar():
    resultado = 9/5 * celcius + 32
    print(resultado)
    
cambiar()

def cambiar2():
    resultado2 = 5/9 * (farenheit - 32)
    print(resultado2) 

cambiar2()

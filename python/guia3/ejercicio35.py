year = int(input("Ingrese un año: "))

def bisiesto():
    if(year % 4 == 0 and year%100 != 0) or year %400 == 0:
        print("El año {} es bisiesto".format(year))
    else:
        print("El año no es bisiesto")
        
bisiesto()


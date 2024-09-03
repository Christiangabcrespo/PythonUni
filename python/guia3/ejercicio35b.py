dias = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
meses = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

mes = int(input("Ingrese un mes: "))
year = int(input("Ingrese un año: "))

# Verificar si el año es bisiesto y ajustar los días de febrero
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    dias[2] = 29

def dia():
    if mes in meses:
        print(f"El mes tiene {dias[mes]} días")
    else:
        print("Ingrese un mes correcto")

dia()
palabra = input("ingrese una palabra: ")

def corte():
    corte1 = palabra[0:5]
    print(corte1)

def invertida():
    invert = palabra[::-1]
    print(invert)

def corte2():
    for i in range(0, len(palabra), 2):
        print(palabra[i], end="")


corte()
corte2()
invertida()
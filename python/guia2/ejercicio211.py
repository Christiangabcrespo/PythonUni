num1 = int(input("ingrese un numero: "))
num2 = int(input("ingrese un numero: "))

def division():
    return num1/num2
 
def resto():
    return (num1/num2)%2 
 
print(division(), resto())
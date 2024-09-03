def dia_de_la_semana(dia_del_ano):
    # Lista de los días de la semana, considerando que el primer día es lunes
    dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
    
    # Calcular el índice del día de la semana
    indice_dia = (dia_del_ano - 1) % 7
    
    # Devolver el día correspondiente
    return dias_semana[indice_dia]

# Pedir al usuario que ingrese un número de día del año
dia_del_ano = int(input("Introduce un número de día del año (1-366): "))

# Obtener el día de la semana y mostrarlo
dia_semana = dia_de_la_semana(dia_del_ano)
print(f"El día {dia_del_ano} corresponde a {dia_semana}.")
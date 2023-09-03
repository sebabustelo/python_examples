def es_fecha_valida(dia, mes, anio):
    # Verificar si el año es bisiesto
    es_bisiesto = (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)
    
    # Definir la cantidad de días en cada mes
    dias_en_mes = [31, 28 if not es_bisiesto else 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Verificar que el mes esté en el rango válido (entre 1 y 12)
    if mes < 1 or mes > 12:
        return False
    
    # Verificar que el día esté en el rango válido para ese mes
    if dia < 1 or dia > dias_en_mes[mes - 1]:
        return False
    
    return True


dia = int(input("Ingresa el día: "))
mes = int(input("Ingresa el mes: "))
anio = int(input("Ingresa el año: "))

if es_fecha_valida(dia, mes, anio):
    print("La fecha es válida.")
else:
    print("La fecha es inválida.")

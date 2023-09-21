#Realizar un programa que pida al usuario que ingrese el día y mes de su cumpleaños y 
# el programa le debe decir a qué signo del zodíaco corresponde.
#• Aries: 21 de marzo al 20 de abril
#• Tauro: 21 de abril al 20 de mayo
#• Géminis: 21 de mayo al 21 de junio
#• Cáncer: 22 de junio al 23 de julio
#• Leo: 24 de julio al 23 de agosto
#• Virgo: 24 de agosto al 23 de septiembre
#• Libra: 24 de septiembre al 22 de octubre
#• Escorpio: 23 de octubre al 22 de noviembre
#• Sagitario: 23 de noviembre al 21 de diciembre
#• Capricornio: 22 de diciembre al 20 de enero
#• Acuario: 21 de enero al 19 de febrero
#• Piscis: 20 de febrero al 20 de marzo

def obtener_signo(dia, mes):
    if (mes == 3 and 21 <= dia <= 31) or (mes == 4 and 1 <= dia <= 20):
        return "Aries"
    elif (mes == 4 and 21 <= dia <= 30) or (mes == 5 and 1 <= dia <= 20):
        return "Tauro"
    elif (mes == 5 and 21 <= dia <= 31) or (mes == 6 and 1 <= dia <= 21):
        return "Géminis"
    elif (mes == 6 and 22 <= dia <= 30) or (mes == 7 and 1 <= dia <= 23):
        return "Cáncer"
    elif (mes == 7 and 24 <= dia <= 31) or (mes == 8 and 1 <= dia <= 23):
        return "Leo"
    elif (mes == 8 and 24 <= dia <= 31) or (mes == 9 and 1 <= dia <= 23):
        return "Virgo"
    elif (mes == 9 and 24 <= dia <= 30) or (mes == 10 and 1 <= dia <= 22):
        return "Libra"
    elif (mes == 10 and 23 <= dia <= 31) or (mes == 11 and 1 <= dia <= 22):
        return "Escorpio"
    elif (mes == 11 and 23 <= dia <= 30) or (mes == 12 and 1 <= dia <= 21):
        return "Sagitario"
    elif (mes == 12 and 22 <= dia <= 31) or (mes == 1 and 1 <= dia <= 20):
        return "Capricornio"
    elif (mes == 1 and 21 <= dia <= 31) or (mes == 2 and 1 <= dia <= 19):
        return "Acuario"
    else:
        return "Piscis"

def validar_fecha(dia, mes):
    if 1 <= mes <= 12 and 1 <= dia <= 31:
        if (mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia > 30:
            return False
        elif mes == 2:
            if (dia > 29) or (dia > 28 and not es_bisiesto()):
                return False
        return True
    return False

def es_bisiesto():
    # Función para verificar si un año es bisiesto
    # Un año es bisiesto si es divisible por 4, pero no por 100, a menos que también sea divisible por 400
    year = int(input("Ingresa el año de tu cumpleaños: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False




def main():
# Solicitar al usuario el día y mes de su cumpleaños
    while True:
        try:
            dia = int(input("Ingresa el día de tu cumpleaños (1-31): "))
            mes = int(input("Ingresa el mes de tu cumpleaños (1-12): "))
            if validar_fecha(dia, mes):
                break
            else:
                print("Fecha no válida. Ingresa una fecha válida.")
        except ValueError:
            print("Entrada inválida. Ingresa un número válido para el día y el mes.")

    signo = obtener_signo(dia, mes)
    print(f"Tu signo del zodíaco es {signo}.")

if __name__ == "__main__":
    main()

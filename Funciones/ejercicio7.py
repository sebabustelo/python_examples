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

import ejercicio1 as Validador
import ejercicio6 as Fecha

def determinar_signo(dia, mes):
    if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 20):
        return "Aries"
    elif (mes == 4 and dia >= 21) or (mes == 5 and dia <= 20):
        return "Tauro"
    elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 21):
        return "Géminis"
    elif (mes == 6 and dia >= 22) or (mes == 7 and dia <= 23):
        return "Cáncer"
    elif (mes == 7 and dia >= 24) or (mes == 8 and dia <= 23):
        return "Leo"
    elif (mes == 8 and dia >= 24) or (mes == 9 and dia <= 23):
        return "Virgo"
    elif (mes == 9 and dia >= 24) or (mes == 10 and dia <= 22):
        return "Libra"
    elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 22):
        return "Escorpio"
    elif (mes == 11 and dia >= 23) or (mes == 12 and dia <= 21):
        return "Sagitario"
    elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 20):
        return "Capricornio"
    elif (mes == 1 and dia >= 21) or (mes == 2 and dia <= 19):
        return "Acuario"
    else:
        return "Piscis"

def main():
    dia = Validador.ingresar_numero_entero("Ingrese el día de su cumpleaños: ")
    mes = Validador.ingresar_numero_entero("Ingrese el mes de su cumpleaños (como número): ")
    
    if(Fecha.es_fecha_valida(dia,mes,2024)):
        signo = determinar_signo(dia, mes)
        print("Su signo del zodíaco es:", signo)
    else:
        print("La fecha ingresada no es válida")
    

if __name__ == "__main__":
    main()
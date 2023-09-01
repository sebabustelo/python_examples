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

class Zodiaco:
    def __init__(self):
        
        self.signos = {
            "Aries": [(21, 3), (20, 4)],
            "Tauro": [(21, 4), (20, 5)],
            "Geminis": [(21, 5), (21, 6)],
            "Cancer": [(22, 6), (23, 7)],
            "Leo": [(24, 7), (23, 8)],
            "Virgo": [(24, 8), (23, 9)],
            "Libra": [(24, 9), (22, 10)],
            "Escorpio": [(23, 10), (22, 11)],
            "Sagitario": [(23, 11), (21, 12)],
            "Capricornio": [(22, 12), (20, 1)],
            "Acuario": [(21, 1), (19, 2)],
            "Piscis": [(20, 2), (20, 3)]
        }

    def obtener_signo(self, dia, mes):
        for signo, fechas in self.signos.items():
            inicio = fechas[0]
            fin = fechas[1]
            if (mes == inicio[1] and dia >= inicio[0]) or (mes == fin[1] and dia <= fin[0]):
                return signo
        return "Desconocido"

def main():
    zodiaco = Zodiaco()

    dia = int(input("Ingrese el día de su cumpleaños: "))
    mes = int(input("Ingrese el mes de su cumpleaños (en números): "))

    signo = zodiaco.obtener_signo(dia, mes)
    print("Su signo del zodiaco es:", signo)

if __name__ == "__main__":
    main()

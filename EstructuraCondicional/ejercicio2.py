#El encargado del planetario desea que se diseñe un programa que, al ingresar el número de día de la semana, indique el nombre de día y el astro que da origen a ese nombre.
#La siguiente tabla muestra la relación astro-día
# Dia         Nombre del Astro
# Domingo     Sol
# Lunes       Saturno
# Martes      Venus  
# Miercoles   Jupiter
# Jueves      Mercurio
# Viernes     Marte
# Sabados     Luna

def ingresar_dia_semana(mensaje):
    while True:
        try:
            dia = int(input(mensaje)) 
            if (dia > 0 and dia <= 7):
                return dia 
        except ValueError:
            print("Ingrese el número de día de la semana (1-7): ")

def obtener_nombre_astro(dia):
    
        match dia:
            case 1:
                astro = "Sol"
                nombre_dia = "Domingo"
            case 2:
                astro = "Saturno"
                nombre_dia = "Lunes"
            case 3:
                astro = "Venus"
                nombre_dia = "Martes"
            case 4:
                astro = "Jupiter"
                nombre_dia = "Miercoles"
            case 5:
                astro = "Mercurio"
                nombre_dia = "Jueves"
            case 6:
                astro = "Marte"
                nombre_dia = "Viernes"
            case 7:
                astro = "Luna"
                nombre_dia = "Sabado"
                    
        print("Nombre del día:", nombre_dia)
        print("Astro que da origen al nombre:", astro)    
        

def main():

    numero_dia = ingresar_dia_semana("Ingrese el número de día de la semana (1-7): ")
    
    obtener_nombre_astro(numero_dia)


if __name__ == "__main__":
    main()

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

class Planetario:
    def __init__(self):
        self.astro_dia = {
            "Domingo": "Sol",
            "Sábado": "Saturno",
            "Viernes": "Venus",
            "Jueves": "Júpiter",
            "Miércoles": "Mercurio",
            "Martes": "Marte",
            "Lunes": "Luna"
        }

    def obtener_nombre_astro(self, nombre_dia):
        return self.astro_dia.get(nombre_dia, "Astro desconocido")

def main():
    planetario = Planetario()

    numero_dia = int(input("Ingrese el número de día de la semana (1-7): "))

    while numero_dia < 1 or numero_dia > 7:
        print("Número de día inválido. Debe estar entre 1 y 7.")
        numero_dia = int(input("Ingrese el número de día de la semana (1-7): "))
    
    dias_semana = list(planetario.astro_dia.keys())
    nombre_dia = dias_semana[numero_dia - 1]
    astro = planetario.obtener_nombre_astro(nombre_dia)

    print("Nombre del día:", nombre_dia)
    print("Astro que da origen al nombre:", astro)

if __name__ == "__main__":
    main()

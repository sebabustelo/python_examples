#Charly va a hacer una fiesta, pero como es super popular un monton de gente pretende asistir. 
#El problema es que no entra mucha gente en su casa, solo hay capacidad para 50 personas. 
#Entonces se le ocurrio una idea buenisima para definir quienes entran y quienes no. 
#Decidio que a cada uno que quiera ingresar le iba a pedir un numero,
#si este numero esta entre N y M, lo deja entrar, si no, no lo deja. 
#Indique cuantas personas intentaron ingresar a la fiesta. 


def ingresar_numero_entero_positivo(mensaje):
    while True:
        try:
            numero = int(input(mensaje)) 
            if (numero > 0):
                return numero
            else:
               print("Debes ingresar un número entero positivo.") 
            
        except ValueError:
            print("Debes ingresar un número entero positivo.")
    
def calcular_incremento(importe):
        if importe >= 900:
            return importe * 2
        elif importe >= 700:
            return importe * 1.5
        elif importe >= 500:
            return importe * 1.2
        else:
            return importe

def main():
    numero_celular = input("Ingrese el número de celular: ")
    importe_recarga = ingresar_numero_entero_positivo("Ingrese el importe de la recarga: ")
    importe_acreditado =  calcular_incremento(importe_recarga)

    print("Numero de celular:", numero_celular)
    print("Importe acreditado de la recarga:", importe_acreditado)

if __name__ == "__main__":
    main()
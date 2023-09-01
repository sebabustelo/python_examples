#Charly va a hacer una fiesta, pero como es super popular un monton de gente pretende asistir. 
#El problema es que no entra mucha gente en su casa, solo hay capacidad para 50 personas. 
#Entonces se le ocurrio una idea buenisima para definir quienes entran y quienes no. 
#Decidio que a cada uno que quiera ingresar le iba a pedir un numero,
#si este numero esta entre N y M, lo deja entrar, si no, no lo deja. 
#Indique cuantas personas intentaron ingresar a la fiesta. 
class Empresa:
    def __init__(self) -> None:
        pass
    
    def calcular_incremento(self,importe):
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
    importe_recarga = float(input("Ingrese el importe de la recarga: "))
    
    emp =  Empresa()
   
    importe_acreditado =  emp.calcular_incremento(importe_recarga)

    print("Numero de celular:", numero_celular)
    print("Importe acreditado de la recarga:", importe_acreditado)

if __name__ == "__main__":
    main()
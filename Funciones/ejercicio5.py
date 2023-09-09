#Hacer un programa que solicite un año. Luego mostrar un mensaje indicando si el año ingresado es un año
#bisiesto. Resumiendo: un año es bisiesto si es divisible por 4, pero no es divisible por 100, o en el caso que sea
#divisible por 400.

def ingresar_anio():
    while True:
        try:
            numero = int(input(f"Ingresa un  año para validar si es bisiesto : ")) 
            if(numero > 0):
               return numero
            else:
               print("Debes ingresar un año, el valor ingresado no es válido.")      
        except ValueError:
            print("Debes ingresar un año, el valor ingresado no es válido.")  


def validar_anio_bisiesto(anio):
     
    if((anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0) ):
        return True
    else:
        return False
 
          
def main():
    anio =ingresar_anio()
    if(validar_anio_bisiesto(anio)):
       print("El año ingresado es bisiesto")
    else:   
       print("El año ingresado no es bisiesto")
    

if __name__ == "__main__":
    main()           
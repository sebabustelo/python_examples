#Escribir una función que tenga un argumento de tipo entero y que devuelva la letra P si el número es positivo,
#la letra N si el número es negativo, y la letra C si es cero.


# Permite ingresar un número por consola y válida que sea un entero, si no lo
# es, vuelve a solicitar que ingrese un número hasta que sea correcto.
# Retorna el número ingresado convertido a entero
def ingresar_numero():
    
    numero = input(f"Ingrese un numero entero: ")
    while (not(numero.isdigit())):
        numero = input(f"No corresponde, ingrese un numero entero: ")
    return int(numero)  

def obtener_signo(numero):
    if numero > 0:
        return 'P'
    elif numero < 0:
        return 'N'
    else:
        return 'C'


def main():
   
    numero = ingresar_numero()
    resultado = obtener_signo(numero)
    print(f"El número {numero} es {resultado}")
    
if __name__ == "__main__":
    main()   
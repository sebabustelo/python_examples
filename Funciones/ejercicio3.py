#Escribir una función que tenga un argumento de tipo entero y que devuelva la letra P si el número es positivo,
#la letra N si el número es negativo, y la letra C si es cero.

# Permite ingresar un número por consola y válida que sea un entero, si no lo
# es, vuelve a solicitar que ingrese un número hasta que sea correcto.
# Retorna el número ingresado convertido a int
def ingresar_numero():
    while True:
        try:
            numero = int(input(f"Ingresa un número entero : "))  # Utilizamos int para admitir números enteros solamente
            return numero
        except ValueError:
            print("Debes ingresar un número válido.") 

def obtener_signo(numero):
    if numero > 0:
        return 'Positivo'
    elif numero < 0:
        return 'Negativo'
    else:
        return 'Cero'


def main():
   
    numero = ingresar_numero()
    resultado = obtener_signo(numero)
    print(f"El número es {resultado}")
    
if __name__ == "__main__":
    main()   
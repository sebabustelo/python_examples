#Escribir una función que permita la suma 1+2+3+….+n, donde n es la variable que pasa a la función como parámetro.

import ejercicio1 as Validador

# Permite ingresar un número por consola y válida que sea un entero, si no lo
# es, vuelve a solicitar que ingrese un número hasta que sea correcto.
# Recibe por parametro el mensaje que se quiere mostrar por consola en la solicitud.
# Retorna el número ingresado convertido a entero
def ingresar_numero_entero(mensaje):
    while True:
        try:
            numero = int(input(mensaje)) 
            return numero
        except ValueError:
            print("Debes ingresar un número válido.")
    
def suma_hasta_n(n):
    
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma


def main():  
     
    n = Validador.ingresar_numero_entero("Ingrese el valor para n: ")
    suma = suma_hasta_n(n)
    print(f"La suma de los números del 1 al {n} es {suma}")
    
    
if __name__ == "__main__":
    main()    
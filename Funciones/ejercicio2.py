#Escribir una función que permita la suma 1+2+3+….+n, donde n es la variable que pasa a la función como parámetro.


# Permite ingresar un número por consola y válida que sea un entero, si no lo
# es, vuelve a solicitar que ingrese un número hasta que sea correcto.
# Recibe por parametro el nombre de que se quiere mostrar por consola en la solicitud.
# Retorna el número ingresado convertido a entero
def ingresar_numero(nombre):
    
    numero = input(f"Ingrese un numero entero para {nombre}: ")
    while (not(numero.isdigit())):
        numero = input(f"Ingrese un numero entero para {nombre}: ")
    return int(numero)   
    
def suma_hasta_n(n):
    
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma


def main():  
     
    n = ingresar_numero("n")
    suma = suma_hasta_n(n)
    print(f"La suma de los números del 1 al {n} es {suma}")
    
    
if __name__ == "__main__":
    main()    
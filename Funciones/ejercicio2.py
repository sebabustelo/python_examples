#Escribir una función que permita la suma 1+2+3+….+n, donde n es la variable que pasa a la función como parámetro.

import ejercicio1 as Validador

    
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
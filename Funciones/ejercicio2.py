
#Escribir una función que tenga un argumento de tipo entero y que devuelva la letra P si el número es positivo,
#la letra N si el número es negativo, y la letra C si es cero.

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
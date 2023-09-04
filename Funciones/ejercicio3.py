#Escribir una función que tenga un argumento de tipo entero y que devuelva la letra P si el número es positivo,
#la letra N si el número es negativo, y la letra C si es cero.

import ejercicio1 as Validador

def obtener_signo(numero):
    if numero > 0:
        return 'Positivo'
    elif numero < 0:
        return 'Negativo'
    else:
        return 'Cero'

def main():
   
    numero = Validador.ingresar_numero_entero("Ingrese un valor entero: ")
    resultado = obtener_signo(numero)
    print(f"El número es {resultado}")
    
if __name__ == "__main__":
    main()   
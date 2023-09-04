# Definir una función que tome como argumento tres números enteros y devuelva el mayor de los tres.

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
            print("Debes ingresar un número entero.")

def buscar_mayor_numero(a, b, c):
    
    if(a > b):
        mayor  = a
    else:
        mayor = b  
          
    if(c > mayor):
        mayor = c   
    return mayor        
       
       
def main():
   
   numero1 = ingresar_numero_entero("Ingresa un valor  para el numero 1: ")
   numero2 = ingresar_numero_entero("Ingresa un valor  para el numero 2: ")
   numero3 = ingresar_numero_entero("Ingresa un valor  para el numero 3: ")
   
   resultado = buscar_mayor_numero(numero1, numero2, numero3)
   print(f"El número máximo entre {numero1}, {numero2} y {numero3} es {resultado}")
    
 
if __name__ == "__main__":
    main()    
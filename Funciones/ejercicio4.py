#Escribir una función que reciba un número y valide el ingreso del mismo de modo que vuelva a solicitar el
#número hasta que este sea positivo.

def ingresar_numero():
    
    numero = input(f"Ingrese un numero entero positivo: ")
    while (not(numero.isdigit())):
        numero = input(f"No corresponde, por favor ingrese un número positivo: ")
    return int(numero)  

         
def main():
   
   ingresar_numero()
   print(f"Gracias")
    
    
if __name__ == "__main__":
    main()    
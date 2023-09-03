#Escribir una función que reciba un número y valide el ingreso del mismo de modo que vuelva a solicitar el
#número hasta que este sea positivo.

# Permite ingresar un número por consola y válida que sea un entero, si no lo
# es, vuelve a solicitar que ingrese un número hasta que sea correcto.
# Retorna el número ingresado convertido a int
def ingresar_numero_positivo():
    while True:
        try:
            numero = float(input(f"Ingresa un número positivo : "))  # Utilizamos float para admitir números deciemales
            if(numero > 0):
               return numero
            else:
               print("Debes ingresar un número positivo, el valor ingresado no es válido.")    
        except ValueError:
            print("Debes ingresar un número positivo, el valor ingresado no es válido.")  

         
def main():
   
   ingresar_numero_positivo()
   print(f"Gracias, el número es positivo")
    
    
if __name__ == "__main__":
    main()    
#Escribir un programa que permita ingresar dos numeros enteros a y b. El programa debe mostrar: 
#a) La suma de los numeros entre a y b 
#b) La suma de los numeros pares entre a y b. 
#c) El producto de los numeros impares entre a y b. 

class Operaciones:
    
    def sumar_pares(self,numero):
       suma_pares = 0
       for i in range(1,numero+1):
            if((i%2) == 0):
               suma_pares = suma_pares + i          
       return suma_pares   
   
    def producto_impares(self,numero):
        producto_impares = 1
        for i in range(1,numero+1):
            if((i%2) == 1):
                producto_impares = producto_impares * i
        return producto_impares    
        
    def ingresar_numero(self,nombre):
        numero = input(f"Ingrese un numero entero para {nombre}: ")
        while (not(numero.isdigit())):
          numero = input(f"Ingrese un numero entero para {nombre}: ")
        return int(numero)  
                                         
def main():
  
   op = Operaciones()  
   a = op.ingresar_numero("a")
   b = op.ingresar_numero("b")     
  
   suma_pares_a = op.sumar_pares(a)
   suma_pares_b = op.sumar_pares(b)
   producto_impares_a = op.producto_impares(a)
   producto_impares_b = op.producto_impares(b)
    
   print("La suma de a y b es: ",a+b)
   print("La suma de los numeros pares entre a y b es: ", suma_pares_a+suma_pares_b)
   print("El producto de los numeros impares entre a y b es: ", producto_impares_a*producto_impares_b)

if __name__ == "__main__":
    main()
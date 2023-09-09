#Charly va a hacer una fiesta, pero como es super popular un monton de gente pretende asistir. 
#El problema es que no entra mucha gente en su casa, solo hay capacidad para 50 personas. 
#Entonces se le ocurrio una idea buenisima para definir quienes entran y quienes no. 
#Decidio que a cada uno que quiera ingresar le iba a pedir un numero, si este numero esta entre N y M, lo deja entrar, si no, no lo deja. 
#Indique cuantas personas intentaron ingresar a la fiesta. 

def verificar_numero(numero,n,m):
        if(numero >= n and numero <= m):
            return True
        else:  
            return False
                    
def ingresar_numero_entero_positivo(mensaje):
    while True:
        try:
            numero = int(input(mensaje)) 
            if (numero > 0):
                return numero
            else:
               print("Debes ingresar un número entero positivo.") 
            
        except ValueError:
            print("Debes ingresar un número entero positivo.")   
                          
def main():
   
   n = ingresar_numero_entero_positivo("Ingrese un numero entero para n:")
   m = ingresar_numero_entero_positivo("Ingrese un numero entero para m:")
         
   numero_ingreso = "" 
   contador_ingresos = 0
   contador_rechazados = 0
   
   while (numero_ingreso != "No"):
       
        numero_ingreso = input("Ingrese un numero para validar el ingreso, 'No' para terminar: ")
        
        while (not(numero_ingreso.isdigit()) and numero_ingreso!='No'):
           print(not(numero_ingreso.isdigit()))
           print(numero_ingreso!='No')
           print(not(numero_ingreso.isdigit()) or numero_ingreso!='No') 
           numero_ingreso = input("Ingrese un numero para validar el ingreso, 'No' para terminar: ")
       
        if(numero_ingreso.isdigit()):
            numero_valido = verificar_numero(int(numero_ingreso),n,m)
            if(numero_valido):
                contador_ingresos = contador_ingresos +1
            else:
                contador_rechazados = contador_rechazados + 1
         
   print("La cantidad de personas que ingresaron son: " , contador_ingresos)
   print("La cantidad de personas que se rechazaron son: " , contador_rechazados)     

if __name__ == "__main__":
    main()
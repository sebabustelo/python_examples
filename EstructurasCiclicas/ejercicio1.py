#Charly va a hacer una fiesta, pero como es super popular un monton de gente pretende asistir. 
#El problema es que no entra mucha gente en su casa, solo hay capacidad para 50 personas. 
#Entonces se le ocurrio una idea buenisima para definir quienes entran y quienes no. 
#Decidio que a cada uno que quiera ingresar le iba a pedir un numero, si este numero esta entre N y M, lo deja entrar, si no, no lo deja. 
#Indique cuantas personas intentaron ingresar a la fiesta. 

class Fiesta():

    def verificar_numero(self,numero,n,m):
        if(numero >= n and numero <= m):
            return True
        else:  
            return False
         
    def ingresar_numero(self,nombre):
        numero = input(f"Ingrese un numero entero para {nombre}: ")
        while (not(numero.isdigit())):
          numero = input(f"Ingrese un numero entero para {nombre}: ")
        return int(numero)  
                          
def main():
    
   fiesta = Fiesta()
   
   n = fiesta.ingresar_numero("n")
   m = fiesta.ingresar_numero("m")
         
   numero_ingreso = "" 
   contador_ingresos = 0
   contador_rechazados = 0
   
   while (numero_ingreso != "No"):
       
        numero_ingreso = input("Ingrese un numero para validar el ingreso, 'No' para terminar: ")
        while (not(numero_ingreso.isdigit()) and numero_ingreso!='No'):
           numero_ingreso = input("Ingrese un numero para validar el ingreso, 'No' para terminar: ")
       
        if(numero_ingreso.isdigit()):
            numero_valido = fiesta.verificar_numero(int(numero_ingreso),n,m)
            if(numero_valido):
                contador_ingresos = contador_ingresos +1
            else:
                contador_rechazados = contador_rechazados + 1
         
   print("La cantidad de personas que ingresaron son: " , contador_ingresos)
   print("La cantidad de personas que se rechazaron son: " , contador_rechazados)     

if __name__ == "__main__":
    main()
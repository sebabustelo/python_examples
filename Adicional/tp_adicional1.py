#Se quiere diseñar el menú de un expendedor de snack
#  1. Al comenzar el programa, solicitara que se ingresen los precios de los 4 productos
#  2. A continuación, se debe mostrar el siguiente menú:
#           1) Papas fritas
#           2) Palitos salados
#           3) Mani salado
#           4) Frutos secos
#           5) Salir
#
# Al seleccionar el Snack, se le preguntará cuantas unidades quiere. Se le mostrará el importe a pagar posteriormente
# se le solicitará que ingrese el monto con el que va a abonar. El sistema debe evaluar si el monto ingresado alcanza para
# abonar el snack. En caso de que no alcance, no se realizará la venta y el sistema le notificara "Dinero insuficiente,
# retire el dinero ingresado ".
# Si el dinero ingresado alcanza para abonar el snack, se le informara que puede retirar el producto y en el caso
# de que no haya abonado en forma exacta, también mostrará cuál es el vuelto.
# Tener en cuenta que si se elije el producto que esta de promocion, la transaccion tendra un descuento del 15%.
# Solo se sale del sistema cuando se selecciona 5.
# Cuando se sale del sistema se deberá mostrar:
#    * El total recaudado por cada snack  
#    * La recaudación total.
# Considerar que, por cada transacción, la máquina solo expende un solo tipo de snack

def seleccionar_menu(mensaje):
    while True:
        try:
            numero = int(input(mensaje)) 
            if (numero > 0 and numero < 6):
                return numero
            else:
               print("Debes ingresar un número válido del menú [1,2,3,4,5].") 
            
        except ValueError:
            print("Debes ingresar un número válido del menú [1,2,3,4,5].") 
            
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
             

def mostrar_menu(precios):
   # Mostramos el menú
    print("Menú de Snacks:")
    print(f"1) Papas fritas - ${precios[0]:.2f}")
    print(f"2) Palitos salados - ${precios[1]:.2f}")
    print(f"3) Maní salado - ${precios[2]:.2f}")
    print(f"4) Frutos secos - ${precios[3]:.2f}")
    print("5) Salir")
    
def calcular_importe(opcion_snack, cantidad,precios):
    match opcion_snack:
        case 1:
            importe =  cantidad * precios[0]
        case 2:
            importe =  cantidad * precios[1]    
        case 3:
            importe =  cantidad * precios[2]
        case 4:
            importe =  cantidad * precios[3]
        case _:
            importe = 0
         
    return importe    
     

def main():
    # Inicializamos los precios de los productos
    precios = [700, 300, 600, 900]
    productos = []
    # Inicializamos el total recaudado por cada snack
    total_recaudado = [0,0,0,0] 
    
    mostrar_menu(precios)
    opcion_seleccionada = seleccionar_menu("Ingrese la operación que desea realizar del menú: ")
    while (opcion_seleccionada != 5):
        cantidad_snack = ingresar_numero_entero_positivo("Ingrese cuantas unidades quiere: ")
        importe_snack = calcular_importe(opcion_seleccionada,cantidad_snack,precios)
        print("El importe a pagar es ",importe_snack )
        importe_abonado = ingresar_numero_entero_positivo("Ingrese el monto con el que va a abonar: ")
        if(importe_abonado < importe_snack):
            print("Dinero insuficiente, retire el dinero ingresado.")
        elif(importe_abonado > importe_snack):
            print("Retire su producto, su vuelto es: ",(importe_abonado - importe_snack) ," ,muchas gracias")
        else:
            print("Retire su producto,muchas gracias " )
            
        total_recaudado[opcion_seleccionada-1] = total_recaudado[opcion_seleccionada-1] + importe_snack
        mostrar_menu(precios)
        opcion_seleccionada =  seleccionar_menu("Ingrese la operación que desea realizar del menú: ")   
                
    for i in range(0,4):
        print(f"El total recaudado para el snack es {i} es ${total_recaudado[i]}")        
             
if __name__ == "__main__":
     main()       
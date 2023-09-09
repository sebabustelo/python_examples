#En una playa de estacionamiento “Tow Mater”, se cobra de la siguiente manera: los 10 minutos son gratis,
# los siguientes 30 minutos tiene un va lor de $ 500 .00 y la hora $ 1000 .00. Se desea escribir un programa que,
# para 10 vehiculos, reciba tanto minutos como horas y muestre lo que debe cancelar cada cliente. 
# Tomando en cuenta que si es Martes o Sabado se hace un descuento del 20% sobre el monto tota l.
# Al finalizar el ingreso de los n vehiculos, el programa debe mostrar cuantos vehiculos permanecieron menos de media hora. 

#El enunciado no aclara si al pasar a otro rango de tarifa se cobra por media hora mas o no, 
#ejemplo si esta 1 hora y 10 minutos, le fracciona esos 10 minutos como otra media hora y seria 1500 pesos (siempre
# y cuando no sea un dia con descuento), o solo le cobro 1 hora.


import math
import ejercicio1 as Validador
        
def ingresar_dia_semana(mensaje):
    while True:
        try:
            dia = int(input(mensaje)) 
            if (dia > 0 and dia <= 7):
                return dia 
        except ValueError:
            print("Ingrese el número de día de la semana (1-7): ")  
            
def ingresar_numero_entero_positivo(mensaje):
    while True:
        try:
            numero = int(input(mensaje)) 
            if (numero >= 0):
                return numero
            else:
               print("Debes ingresar un número entero positivo.") 
            
        except ValueError:
            print("Debes ingresar un número entero positivo.")                          
        
def calcular_costo(horas,minutos,dia):
        costo_total = 0
        minutos_totales = horas * 60 + minutos
        minutos_totales = minutos_totales
      
        if (minutos_totales > 10 and minutos_totales < 30):
             costo_total +=  500
        elif(minutos_totales <= 10):
            #primero 10 minutos son gratis
             costo_total +=  0
        else:
             #costo_total += ((minutos_totales) / 30) * 500
             costo_total += (math.ceil((minutos_totales) / 30)) * 500
        
        # Aplica el descuento si es Martes (2) o Sábado (6)
        if dia == 2 or dia == 6:
            costo_total *= 0.8

        return costo_total


def main():
   
    vehiculos_menos_de_media_hora =0
    for i in range(10):
        print(f"Cliente {i + 1}")
        minutos = ingresar_numero_entero_positivo("Ingrese la cantidad de minutos: ")
        horas = ingresar_numero_entero_positivo("Ingrese la cantidad de horas: ")
        dia = ingresar_dia_semana("Ingrese el día de la semana (1 para Lunes, 2 para Martes, ..., 7 para Domingo):")

        #playa_estacionamiento = Estacionamiento(minutos, horas, dia)
        costo = calcular_costo(horas,minutos,dia)
        print(f"El cliente debe pagar ${costo:.2f}")
        
        if((minutos + horas * 60)< 30):
            vehiculos_menos_de_media_hora = vehiculos_menos_de_media_hora + 1
        
    print(f"Total de vehículos que permanecieron menos de media hora: {vehiculos_menos_de_media_hora}")

if __name__ == "__main__":
    main()

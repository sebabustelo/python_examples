#En una playa de estacionamiento “Tow Mater”, se cobra de la siguiente manera: los 10 minutos son gratis,
# los siguientes 30 minutos tiene un va lor de $ 500 .00 y la hora $ 1000 .00. Se desea escribir un programa que,
# para 10 vehiculos, reciba tanto minutos como horas y muestre lo que debe cancelar cada cliente. 
# Tomando en cuenta que si es Martes o Sabado se hace un descuento del 20% sobre el monto tota l.
# Al finalizar el ingreso de los n vehiculos, el programa debe mostrar cuantos vehiculos permanecieron menos de media hora. 

#El enunciado no aclara si al pasar a otro rango de tarifa se cobra por media hora mas o no, 
#ejemplo si esta 1 hora y 10 minutos, le fracciona esos 10 minutos como otra media hora y seria 1500 pesos (siempre
# y cuando no sea un dia con descuento), o solo le cobro 1 hora.
# En el ejercicio dejamos comentado (#import math, #costo_total += (math.ceil((minutos_totales) / 30)) * 500 ),
# el código que es necesario si se quiere fraccionar para arriba, por defecto los hacemos para abajo.

#import math

class Estacionamiento:
    def __init__(self, minutos, horas, dia):
        self.minutos = minutos
        self.horas = horas
        self.dia = dia

    def calcular_costo(self):
        costo_total = 0

        minutos_totales = self.horas * 60 + self.minutos
        #primero 10 minutos son gratis
        minutos_totales = minutos_totales
      
        if (minutos_totales > 10 and minutos_totales < 30):
             costo_total +=  500
        else:
             costo_total += ((minutos_totales) / 30) * 500
             #costo_total += (math.ceil((minutos_totales) / 30)) * 500
        
        # Aplica el descuento si es Martes (2) o Sábado (6)
        if self.dia == 2 or self.dia == 6:
            costo_total *= 0.8

        return costo_total


def main():
   
    vehiculos_menos_de_media_hora =0
    for i in range(10):
        print(f"Cliente {i + 1}")
        minutos = int(input("Ingrese la cantidad de minutos: "))
        horas = int(input("Ingrese la cantidad de horas: "))
        dia = int(input("Ingrese el día de la semana (1 para Lunes, 2 para Martes, ..., 7 para Domingo): "))

        # Validar que el día ingresado sea válido (entre 1 y 7)
        if dia < 1 or dia > 7:
            print("Día no válido. Ingrese un número entre 1 y 7 .")
            continue

        playa_estacionamiento = Estacionamiento(minutos, horas, dia)
        costo = playa_estacionamiento.calcular_costo()
        print(f"El cliente debe pagar ${costo:.2f}")
        
        if((minutos + horas * 60)< 30):
            vehiculos_menos_de_media_hora = vehiculos_menos_de_media_hora + 1
        
    print(f"Total de vehículos que permanecieron menos de media hora: {vehiculos_menos_de_media_hora}")

if __name__ == "__main__":
    main()

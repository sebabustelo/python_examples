#Hacer una función que nos indique con verdadero o falso si una fecha ingresada en el formato día, mes, año
#es válida o inválida. Considerar los años bisiestos. Desarrollar el código para probarla

import ejercicio1 as Validador
import ejercicio5 as Fecha

def es_fecha_valida(dia, mes, anio):
    # Verificar si el año es bisiesto
    es_bisiesto = Fecha.validar_anio_bisiesto(anio)
    
    # Definir la cantidad de días en cada mes
    dias_en_mes = [31, 28 if not es_bisiesto else 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Verificar que el mes esté en el rango válido (entre 1 y 12)
    if mes < 1 or mes > 12:
        return False
    
    # Verificar que el día esté en el rango válido para ese mes
    if dia < 1 or dia > dias_en_mes[mes - 1]:
        return False
    
    return True


def main():
    dia = Validador.ingresar_numero_entero("Ingrese el valor día en número: ")  
    mes = Validador.ingresar_numero_entero("Ingrese el valor para el mes en número: ")
    anio = Validador.ingresar_numero_entero("Ingrese el valor para el año en número: ")

    if es_fecha_valida(dia, mes, anio):
        print("La fecha es válida.")
    else:
        print("La fecha es inválida.")

if __name__ == "__main__":
    main()           
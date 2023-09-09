#Ejercicio 4
#Realizar un algoritmo que pida al usuario su Peso y su Altura de 150 personas. Calcule el IMC (indice de masa corporal), 
# muestre por cada persona que se ingresa, el mensaje correspondiente (ver tabla). Ademas, debe mostrar la cantidad de 
# personas que esta en cada categoria   
#IMC = masa [kg] / (estatura [m])2 
#Si este da menor que 18.5 es INFRAPESO. 
#Si da entre 18.5 y 25 da NORMAL.  
#Si da entre 25 y 30 es SOBREPESO.  
#Si da mayor a 30 es OBESO. 

import ejercicio1 as Validador


def calcular_imc(peso,altura):
    return peso / (altura ** 2)

def determinar_categoria(peso,altura):
    
    imc = calcular_imc(peso,altura)
    if imc < 18.5:
        return "INFRAPESO"
    elif 18.5 <= imc < 25:
        return "NORMAL"
    elif 25 <= imc < 30:
        return "SOBREPESO"
    else:
        return "OBESO"

def main():
    for i in range(5):
        print(f"Persona {i + 1}")
        nombre = input("Ingrese el nombre de la persona: ")
        peso = float(input("Ingrese su peso en kg: "))
        altura = Validador.ingresar_numero_entero_positivo("Ingrese su altura en centimeros : ")

        categoria = determinar_categoria(peso,altura)
        cantidad_infrapeso = 0
        cantidad_normal = 0
        cantidad_sobrepeso = 0
        cantidad_obeso = 0
        
        match categoria:
            case "INFRAPESO":
                cantidad_infrapeso = cantidad_infrapeso + 1
            case "NORMAL":
                cantidad_normal = cantidad_normal + 1
            case "SOBREPESO":
                cantidad_sobrepeso = cantidad_sobrepeso + 1
            case "OBESO":
                cantidad_obeso = cantidad_obeso + 1            
        

        print(f"El IMC de {nombre} es {calcular_imc(peso,altura):.2f}, categoría: {categoria}\n")
        
        

    print("Resumen:")
    print(f"INFRAPESO: {cantidad_infrapeso} personas")
    print(f"NORMAL: {cantidad_normal} personas")
    print(f"SOBREPESO: {cantidad_sobrepeso} personas")
    print(f"OBSEO: {cantidad_obeso} personas")
    
if __name__ == "__main__":
    main()

#Una empresa cuenta con 50 empleados, divididos en tres categorias A, B Y C. 
#Por cada empleado se lee su legajo, categoria y salario. Se solicita elaborar un inform e que contenga: 
# a. Importe total de salarios pagados por la empresa 
# b. Cantidad de empleados que ganan mas de $300 .000, 00 
# c. Cantidad de empleados que ganan menos de $250.000,00 , cuya categoria sea “C” 
# d. I mporte de sueldos por categoria 
# e. Salario promedio. 

class Empleado:
    def __init__(self, legajo, categoria, salario):
        self.legajo = legajo
        self.categoria = categoria
        self.salario = salario

class Empresa:
    def __init__(self):
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def calcular_informe(self):
        total_salarios = sum(empleado.salario for empleado in self.empleados)
        empleados_mas_de_300000 = 0
        empleados_menos_de_250000_categoria_C = 0
        salarios_por_categoria = {"A": 0, "B": 0, "C": 0}
        
        for empleado in self.empleados:
            
            if (empleado.salario > 300000):
                empleados_mas_de_300000 = empleados_mas_de_300000 + 1
            elif(empleado.salario < 250000 and empleado.categoria == "C"):    
                empleados_menos_de_250000_categoria_C = empleados_menos_de_250000_categoria_C + 1
            
            salarios_por_categoria[empleado.categoria] += empleado.salario    

        salario_promedio = total_salarios / len(self.empleados)

        informe = {
            "a. Importe total de salarios pagados por la empresa": total_salarios,
            "b. Cantidad de empleados que ganan más de $300,000.00": empleados_mas_de_300000,
            "c. Cantidad de empleados que ganan menos de $250,000.00, cuya categoría sea 'C'": empleados_menos_de_250000_categoria_C,
            "d. Importe de sueldos por categoría": salarios_por_categoria,
            "e. Salario promedio de la empresa": salario_promedio
        }

        return informe
    
def main():
        
    empresa = Empresa()

    # Leer datos de los empleados
    for i in range(2):
        print(f"Empleado {i + 1}")
        legajo = int(input("Ingrese el legajo del empleado: "))
        categoria = input("Ingrese la categoría del empleado (A, B o C): ")
        salario = float(input("Ingrese el salario del empleado: "))

        empleado = Empleado(legajo, categoria, salario)
        empresa.agregar_empleado(empleado)

    informe = empresa.calcular_informe()

    # Mostrar el informe
    print("\nInforme de la empresa:")
    for clave, valor in informe.items():
    
        if isinstance(valor, dict):
            print(valor.items())
            print(f"{clave}:")
            for categoria, salario_total in valor.items():
                print(f"   - Categoría {categoria}: ${salario_total:.2f}")
        else:
            print(f"{clave}: {valor}")

        
     
 if __name__ == "__main__":
     main()       

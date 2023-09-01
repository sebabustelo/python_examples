#Ejercicio 4
#Realizar un algoritmo que pida al usuario su Peso y su Altura de 150 personas. Calcule el IMC (indice de masa corporal), 
# muestre por cada persona que se ingresa, el mensaje correspondiente (ver tabla). Ademas, debe mostrar la cantidad de 
# personas que esta en cada categoria   
#IMC = masa [kg] / (estatura [m])2 
#Si este da menor que 18.5 es INFRAPESO. 
#Si da entre 18.5 y 25 da NORMAL.  
#Si da entre 25 y 30 es SOBREPESO.  
#Si da mayor a 30 es OBESO. 

class Persona:
    def __init__(self, nombre, peso, altura):
        self.nombre = nombre
        self.peso = peso
        self.altura = altura

    def calcular_imc(self):
        return self.peso / (self.altura ** 2)

    def determinar_categoria(self):
        imc = self.calcular_imc()
        if imc < 18.5:
            return "INFRAPESO"
        elif 18.5 <= imc < 25:
            return "NORMAL"
        elif 25 <= imc < 30:
            return "SOBREPESO"
        else:
            return "OBESO"

categorias = {
    "INFRAPESO": 0,
    "NORMAL": 0,
    "SOBREPESO": 0,
    "OBESO": 0
}

personas = []

for i in range(150):
    print(f"Persona {i + 1}")
    nombre = input("Ingrese el nombre de la persona: ")
    peso = float(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en metros: "))

    persona = Persona(nombre, peso, altura)
    categoria = persona.determinar_categoria()

    print(f"El IMC de {persona.nombre} es {persona.calcular_imc():.2f}, categoría: {categoria}\n")
    categorias[categoria] += 1
    personas.append(persona)

print("Resumen:")
for categoria, cantidad in categorias.items():
    print(f"{categoria}: {cantidad} personas")

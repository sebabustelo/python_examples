#La fábrica “Firulais” produce artículos con códigos (1,2,3,4,5 y 6). Se requiere un algoritmo para calcular los precios de venta, 
# para esto hay que considerar los siguiente:
#  • Costo de producción es igual a materia prima más mano de obra más gastos de fabricación.
#  • Precio de venta es igual al costo de producción más 45% del costo de producción.
#El costo de mano de obra se obtiene de la siguiente forma: para los productos que tienen código 3 ó 4: se carga 75% del costo de la materia prima;
# para los que tienen código 1 ó 5 se carga 85% y para los que tienen código 2 ó 6, el 90%
#Para calcular el gasto de fabricación se considera que si el artículo que se va a producir tiene código 2 o 5, 
# este gasto representa 30% sobre el costo de la materia prima, si las claves son 3 ó 6, representa el 35%, si los códigos son 1 ó 4 representan el 28%.
#La materia prima tiene el mismo costo para cualquier clave


def calcular_costo_mano_obra(codigo,materia_prima):
        if codigo in [3, 4]:
            return materia_prima * 0.75
        elif codigo in [1, 5]:
            return materia_prima * 0.85
        elif codigo in [2, 6]:
            return materia_prima * 0.90
        else:
            return 0

def calcular_gasto_fabricacion(codigo,materia_prima):
        if codigo in [2, 5]:
            return materia_prima * 0.30
        elif codigo in [3, 6]:
            return materia_prima * 0.35
        elif codigo in [1, 4]:
            return materia_prima * 0.28
        else:
            return 0

def calcular_precio_venta(codigo,materia_prima):
        costo_mano_obra = calcular_costo_mano_obra(codigo,materia_prima)
        gasto_fabricacion = calcular_gasto_fabricacion(codigo,materia_prima)
        costo_produccion = materia_prima + costo_mano_obra + gasto_fabricacion
        precio_venta = costo_produccion + (0.45 * costo_produccion)
        return precio_venta

def main():
    
    materia_prima = 100  # Costo de la materia prima (valor ficticio para ejemplo)
    codigo_articulo = int(input("Ingrese el código del artículo (1-6): "))
    if codigo_articulo < 1 or codigo_articulo > 6:
        print("Código inválido.")
    else:
        precio_venta = calcular_precio_venta(codigo_articulo,materia_prima)
        print("El precio de venta del artículo es:", precio_venta)

if __name__ == "__main__":
    main()

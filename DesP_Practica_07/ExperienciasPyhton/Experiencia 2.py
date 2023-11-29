# Definición de un diccionario de ejemplo
datos_personales = {
    "nombre": "Juan",
    "apellido": "Pérez",
    "edad": 30,
    "ciudad": "Ciudad de Ejemplo",
}

# 1. Funciones que reciben diccionarios como parámetros para procesar datos
def imprimir_datos_persona(persona):
    for clave, valor in persona.items():
        print(f"{clave}: {valor}")

def obtener_edad_persona(persona):
    return persona.get("edad", None)  # Obtiene la edad o devuelve None si no existe

# Llamada a las funciones
print("Datos personales:")
imprimir_datos_persona(datos_personales)

edad = obtener_edad_persona(datos_personales)
if edad is not None:
    print(f"Edad: {edad}")
else:
    print("Edad no especificada")

# 2. Funciones con parámetros por defecto
def calcular_impuesto(datos_fiscales, tasa=0.1):
    ingresos = datos_fiscales.get("ingresos", 0)
    return ingresos * tasa

datos_fiscales = {
    "ingresos": 50000,
    "deducciones": 10000,
}

impuesto = calcular_impuesto(datos_fiscales)
print(f"Impuesto calculado: {impuesto}")

# 3. Funciones que devuelven más de un valor de retorno
def dividir_numero(dividendo, divisor):
    cociente = dividendo // divisor
    residuo = dividendo % divisor
    return cociente, residuo

resultado_cociente, resultado_residuo = dividir_numero(20, 7)
print(f"Cociente: {resultado_cociente}")
print(f"Residuo: {resultado_residuo}")
# Instrucciones condicionales
# 1. Ingresar 6 números diferentes
numbers = []
for i in range(6):
    num = float(input(f"Ingrese el número {i + 1}: "))
    numbers.append(num)

# 2. Hallar el mayor, el menor y el número más próximo al punto medio
max_num = max(numbers)
min_num = min(numbers)
mid_point = sum(numbers) / 6
closest_to_mid = min(numbers, key=lambda x: abs(x - mid_point))

print(f"El número mayor es {max_num}")
print(f"El número menor es {min_num}")
print(f"El número más cercano al punto medio ({mid_point}) es {closest_to_mid}")

# Funciones para instrucciones iterativas
# Función para verificar si un número es primo
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Función para ingresar números y verificar si son primos
def verificar_numeros_primos():
    while True:
        num = int(input("Ingrese un número (o ingrese 0 para salir): "))
        if num == 0:
            break
        if es_primo(num):
            print(f"{num} es primo.")
        else:
            print(f"{num} no es primo.")
    else:
        print("Saliendo de la verificación de números primos.")

# Menú de opciones
def menu():
    print("1. Verificar números primos")
    print("2. Salir")
    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        verificar_numeros_primos()
    elif opcion == 2:
        print("Saliendo del programa.")
    else:
        print("Opción no válida")

# Instrucciones iterativas
while True:
    menu()
    if opcion == 2:
        break

# Funciones para el manejo de colecciones
# Función que recibe una lista como parámetro y suma todos los elementos
def suma_lista(lista):
    return sum(lista)

# Función que recibe una tupla como parámetro y encuentra el máximo valor
def maximo_tupla(tupla):
    return max(tupla)

# Función que recibe una lista como parámetro y un valor por defecto, y suma todos los elementos
def suma_lista_con_defecto(lista, valor_defecto=0):
    return sum(lista) + valor_defecto

# Función que recibe una lista como parámetro y devuelve la suma y el promedio de los elementos
def suma_promedio_lista(lista):
    suma = sum(lista)
    promedio = suma / len(lista)
    return suma, promedio


from estudiante import Estudiante

def ingresar_datos_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")
    edad = input("Ingrese la edad del estudiante: ")
    matricula = input("Ingrese el número de matrícula del estudiante: ")
    
    return Estudiante(nombre, edad, matricula)

def mostrar_menu():
    print("1. Ingresar datos del estudiante")
    print("2. Imprimir datos del estudiante")
    print("3. Matricular al estudiante")
    print("4. Pagar pensión del estudiante")
    print("5. Salir")

def ejecutar_menu(estudiante):
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            estudiante = ingresar_datos_estudiante()
        elif opcion == "2":
            estudiante.imprimirDatos()
        elif opcion == "3":
            estudiante.matricular()
        elif opcion == "4":
            estudiante.pagarPension()
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Inténtelo de nuevo.")

if __name__ == "__main__":
    estudiante = ingresar_datos_estudiante()
    ejecutar_menu(estudiante)

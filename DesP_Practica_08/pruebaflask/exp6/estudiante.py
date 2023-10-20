class Estudiante:
    def __init__(self, nombre, edad, matricula):
        self.nombre = nombre
        self.edad = edad
        self.matricula = matricula
        self.matriculado = False
        self.pension_pagada = False


    def __new__(cls, *args, **kwargs):
        # 8A
        instance = super(Estudiante, cls).__new__(cls)
        return instance

    def __del__(self):
        # 8B
        print(f"Estudiante {self.nombre} eliminado.")
        
     # 7A) CREAR PROPIEDADES
    @property
    def nombre_completo(self):
        return f"{self.nombre} ({self.matricula})"      

    def ingresarDatos(self):
        self.nombre = input("Ingrese el nombre del estudiante: ")
        self.edad = input("Ingrese la edad del estudiante: ")
        self.matricula = input("Ingrese el número de matrícula del estudiante: ")

    def imprimirDatos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Matrícula: {self.matricula}")
        print(f"Matriculado: {self.matriculado}")
        print(f"Pensión Pagada: {self.pension_pagada}")

    def matricular(self):
        self.matriculado = True

    def pagarPension(self):
        self.pension_pagada = True

    @classmethod
    def contar_estudiantes(cls, lista_estudiantes):
        """Método de clase que cuenta la cantidad total de estudiantes."""
        return len(lista_estudiantes)

    @classmethod
    def obtener_edad_promedio(cls, lista_estudiantes):
        """Método de clase que calcula la edad promedio de los estudiantes."""
        if not lista_estudiantes:
            return 0  # Evitar la división por cero si no hay estudiantes

        total_edades = sum(int(estudiante.edad) for estudiante in lista_estudiantes)
        return total_edades / len(lista_estudiantes)

    #7C    
    @staticmethod
    def validar_matricula(matricula):
        """Método estático que valida una matrícula."""
        # Lógica para validar la matrícula (por ejemplo, longitud o formato específico)
        # En este ejemplo, se verifica que la matrícula tenga exactamente 6 caracteres
        return len(matricula) == 6

    @staticmethod
    def imprimir_instrucciones():
        """Método estático que imprime instrucciones para estudiantes."""
        print("Instrucciones para estudiantes:")
        print("- Realice sus tareas a tiempo.")
        print("- Asista a todas las clases.")
        print("- Pague su pensión antes de la fecha límite.")

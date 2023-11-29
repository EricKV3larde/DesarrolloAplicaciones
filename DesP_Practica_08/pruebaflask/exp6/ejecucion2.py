from estudiante import Estudiante

# Crear objetos de instancia
estudiante1 = Estudiante("Juan", "20", "M123")
estudiante2 = Estudiante("María", "22", "M456")
estudiante3 = Estudiante("Carlos", "21", "M789")

# Almacenar objetos en una lista
lista_estudiantes = [estudiante1, estudiante2, estudiante3]

# Ejecutar métodos para cada objeto
for estudiante in lista_estudiantes:
    estudiante.imprimirDatos()
    estudiante.matricular()
    estudiante.pagarPension()
    estudiante.imprimirDatos()

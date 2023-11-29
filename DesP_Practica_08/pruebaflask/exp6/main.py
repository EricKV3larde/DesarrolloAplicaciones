from estudiante import Estudiante
from profesor import Profesor

# estudiante = Estudiante()
# estudiante.ingresarDatos()
# estudiante.imprimirDatos()
# estudiante.matricular()
# estudiante.pagarPension()
# estudiante.imprimirDatos()

# estudiante1 = Estudiante("Juan", "20", "M123")
# estudiante2 = Estudiante("María", "22", "M456")

# print(f"Total de estudiantes: {Estudiante.contar_estudiantes()}")
# print(f"Edad promedio: {Estudiante.obtener_edad_promedio()}")


# from estudiante import Estudiante

# estudiante = Estudiante("Juan", "20", "M123")
# print(estudiante.nombre_completo)
#7B
# from estudiante import Estudiante

# estudiante1 = Estudiante("Juan", "20", "M123")
# estudiante2 = Estudiante("María", "22", "M456")
# estudiante3 = Estudiante("Juana", "21", "M45sd6")

# # Uso de los métodos de clase
# total_estudiantes = Estudiante.contar_estudiantes([estudiante1, estudiante2, estudiante3])
# edad_promedio = Estudiante.obtener_edad_promedio([estudiante1, estudiante2, estudiante3])

# print(f"Total de estudiantes: {total_estudiantes}")
# print(f"Edad promedio: {edad_promedio}")


#7C
# Crear un estudiante
# estudiante = Estudiante("Juan", "20", "M123")

# # Llamar a los métodos estáticos
# matricula_valida = Estudiante.validar_matricula(estudiante.matricula)
# Estudiante.imprimir_instrucciones()

# print(f"¿Matrícula válida? {matricula_valida}")

# Pruebas
estudiante = Estudiante("Juan", "20", "M123")
profesor = Profesor("Dr. Smith", "45", "Física")

# Eliminar objetos (esto activará los métodos __del__)
del estudiante
del profesor


 


















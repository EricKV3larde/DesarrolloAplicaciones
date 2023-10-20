# 1. Crear un archivo de texto o binario
nombre_archivo = 'archivo_texto.txt'  # Cambiar el nombre según sea necesario
modo_apertura = 'w'  # 'w' para texto, 'wb' para binario

try:
    with open(nombre_archivo, modo_apertura) as archivo:
        while True:
            linea = input("Escriba una línea (o escriba 'exit' para terminar): ")
            if linea.lower() == 'exit':
                break
            archivo.write(linea + '\n')
        print("Contenido escrito en el archivo.")
except Exception as e:
    print(f"Error al escribir en el archivo: {str(e)}")

# 6. Cerrar el archivo
archivo.close()

# Definición de la función que escribe contenido adicional en un archivo y lo muestra
def file_read(fname, contenido_adicional):
    # Abrir el archivo en modo de anexar ("a") para agregar contenido adicional
    with open(fname, "a") as myfile:
        myfile.write(contenido_adicional)

    # Abrir el archivo en modo de lectura ("r") para leer el contenido completo
    with open(fname, "r") as txt:
        contenido_completo = txt.read()
        print(contenido_completo)  # Mostrar el contenido completo

# Contenido adicional que deseamos agregar al archivo
contenido_adicional = "Más ejercicios Python\nMás ejercicios Java"

# Llamar a la función con el nombre del archivo y el contenido adicional
file_read('abc.txt', contenido_adicional)
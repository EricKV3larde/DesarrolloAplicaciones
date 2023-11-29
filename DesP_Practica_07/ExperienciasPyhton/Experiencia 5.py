# 1. Leer y mostrar el contenido completo de un archivo
def file_read(fname):
    # Abrir el archivo en modo lectura
    txt = open(fname)
    # Leer y mostrar el contenido
    print(txt.read())

# 4. Leer y mostrar las primeras n líneas de un archivo
def file_read_from_head(fname, nlines):
    from itertools import islice
    # Abrir el archivo en modo lectura
    with open(fname) as f:
        # Utilizar 'islice' para leer las primeras n líneas
        for line in islice(f, nlines):
            print(line)

# 6. Leer y mostrar todas las líneas de un archivo en una lista
def file_read_lines(fname):
    with open(fname, "r") as myfile:
        # Leer todas las líneas del archivo y almacenarlas en 'data'
        data = myfile.readlines()
        # Mostrar 'data'
        print(data)

# 8. Leer y mostrar el contenido de varios archivos con extensión '.txt' en una lista
import glob
char_list = []

# Buscar todos los archivos con extensión '.txt' en el directorio actual
files_list = glob.glob("*.txt")

# Leer y almacenar el contenido de los archivos
for file_elem in files_list:
    with open(file_elem, "r") as f:
        contenido = f.read()
        char_list.append((file_elem, contenido))  # Almacenar el nombre del archivo y su contenido

# Mostrar el contenido de los archivos de manera más legible
for nombre, contenido in char_list:
    print(f"Archivo: {nombre}")
    print(contenido)
    print("-" * 40)  # Línea divisoria entre archivos

# Llamar a las funciones para probarlas
file_read('C:/Users/user/OneDrive/Escritorio/test.txt')
file_read_from_head('C:/Users/user/OneDrive/Escritorio/test.txt', 2)
file_read_lines('C:/Users/user/OneDrive/Escritorio/test.txt')
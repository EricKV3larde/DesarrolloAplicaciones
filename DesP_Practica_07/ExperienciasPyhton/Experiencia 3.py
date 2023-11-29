# a) Crear un archivo de texto
nombre_archivo_texto = "archivo_texto.txt"

# Modo "w" para escritura, creará un archivo si no existe o sobrescribirá si existe
with open(nombre_archivo_texto, "w") as archivo_texto:
    archivo_texto.write("Este es un archivo de texto.\n")
    archivo_texto.write("Puedes escribir texto en él.\n")

# b) Crear un archivo de binario
nombre_archivo_binario = "archivo_binario.bin"

# Modo "wb" para escritura binaria, creará un archivo si no existe o sobrescribirá si existe
with open(nombre_archivo_binario, "wb") as archivo_binario:
    archivo_binario.write(b"Este es un archivo binario.\n")
    archivo_binario.write(b"Puedes escribir datos binarios en el.\n")

# c) Abrir un archivo existente para escritura
nombre_archivo_existente = "archivo_existente.txt"

# Modo "a" para escritura (append), creará el archivo si no existe
with open(nombre_archivo_existente, "a") as archivo_existente:
    archivo_existente.write("Añadiendo texto a un archivo existente.\n")
    archivo_existente.write("Este texto se agregará al final del archivo.\n")

nombre_archivo_texto = "archivo_texto.txt"

with open(nombre_archivo_texto, "r") as archivo_texto:
    contenido = archivo_texto.read()
    print("Contenido del archivo de texto:")
    print(contenido)

# Abrir y leer un archivo de binario
nombre_archivo_binario = "archivo_binario.bin"

with open(nombre_archivo_binario, "rb") as archivo_binario:
    contenido_binario = archivo_binario.read()
    print("\nContenido del archivo binario:")
    print(contenido_binario.decode("utf-8"))

# Abrir y leer un archivo existente
nombre_archivo_existente = "archivo_existente.txt"

with open(nombre_archivo_existente, "r") as archivo_existente:
    contenido_existente = archivo_existente.read()
    print("\nContenido del archivo existente:")
    print(contenido_existente)
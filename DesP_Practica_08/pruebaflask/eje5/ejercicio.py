def buscar_palabra(archivo, palabra):
    try:
        # Abrir el archivo en modo lectura
        with open(archivo, 'r') as f:
            contenido = f.read()

            # Verificar si la palabra existe en el contenido
            if palabra in contenido:
                print(f'La palabra "{palabra}" existe en el archivo.')
            else:
                print(f'La palabra "{palabra}" no existe en el archivo.')
    except FileNotFoundError:
        print(f'Error: No se encontró el archivo {archivo}.')
    except Exception as e:
        print(f'Ocurrió un error: {e}')

# Prueba del programa
archivo_a_verificar = 'texto.txt'  # Reemplaza esto con el nombre de tu archivo
palabra_a_buscar = 'Python'

buscar_palabra(archivo_a_verificar, palabra_a_buscar)

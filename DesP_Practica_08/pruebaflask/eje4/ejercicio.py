def buscar_y_reemplazar(archivo, buscar, reemplazar):
    try:
        # Abrir el archivo en modo lectura y escritura
        with open(archivo, 'r') as f:
            contenido = f.read()

            # Realizar la búsqueda y reemplazo
            nuevo_contenido = contenido.replace(buscar, reemplazar)

        # Escribir el contenido actualizado en el archivo
        with open(archivo, 'w') as f:
            f.write(nuevo_contenido)

        print(f'Se ha realizado la búsqueda y reemplazo en {archivo}.')
    except FileNotFoundError:
        print(f'Error: No se encontró el archivo {archivo}.')
    except Exception as e:
        print(f'Ocurrió un error: {e}')

# Prueba del programa
archivo_a_editar = 'ejemplo.txt'  # Reemplaza esto con el nombre de tu archivo
texto_a_buscar = 'viejo'
texto_a_reemplazar = 'nuevo'

buscar_y_reemplazar(archivo_a_editar, texto_a_buscar, texto_a_reemplazar)

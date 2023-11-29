import os

def verificar_existencia_archivo(ruta):
    try:
        if os.path.isfile(ruta):
            return True
        else:
            return False
    except (PermissionError, FileNotFoundError) as e:
        print(f"Error al verificar la existencia del archivo: {str(e)}")
        return False

def main():
    while True:
        ruta_archivo = input("Ingrese la ruta al archivo que desea verificar: ")

        if verificar_existencia_archivo(ruta_archivo):
            print(f"El archivo en la ruta '{ruta_archivo}' existe.")
        else:
            print(f"El archivo en la ruta '{ruta_archivo}' no existe o no se puede acceder.")

        continuar = input("¿Desea verificar otro archivo? (Sí/No): ").strip().lower()
        if continuar != 'si' and continuar != 'sí':
            break

if __name__ == "__main__":
    main()
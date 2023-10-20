class Profesor:
    # 8A
    def __init__(self, nombre, edad, especialidad):
        self.nombre = nombre
        self.edad = edad
        self.especialidad = especialidad

    def __new__(cls, *args, **kwargs):
        # 8A
        instance = super(Profesor, cls).__new__(cls)
        return instance

    def __del__(self):
        # 8B
        print(f"Profesor {self.nombre} eliminado.")

    @property
    def info_profesor(self):
        return f"{self.nombre} ({self.especialidad})"


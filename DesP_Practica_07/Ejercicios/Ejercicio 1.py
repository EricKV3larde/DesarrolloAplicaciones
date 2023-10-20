class Producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo  # Código único del producto
        self.nombre = nombre  # Nombre del producto
        self.precio = precio  # Precio del producto

    def __str__(self):
        return f"Código: {self.codigo}, Nombre: {self.nombre}, Precio: ${self.precio:.2f}"


class Cliente:
    def __init__(self, id, nombre, direccion):
        self.id = id          # Identificador único del cliente
        self.nombre = nombre  # Nombre del cliente
        self.direccion = direccion  # Dirección del cliente

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Dirección: {self.direccion}"


class Venta:
    def __init__(self, cliente, productos):
        self.cliente = cliente   # Cliente que realiza la compra
        self.productos = productos  # Lista de productos en la venta

    def calcular_total(self):
        total = sum(producto.precio for producto in self.productos)
        return total

    def __str__(self):
        return f"Cliente: {self.cliente.nombre}\nProductos:\n{', '.join(producto.nombre for producto in self.productos)}\nTotal: ${self.calcular_total():.2f}"


# Ejemplo de uso:
# Crear productos
producto1 = Producto("P001", "Producto 1", 10.99)
producto2 = Producto("P002", "Producto 2", 5.49)

# Crear un cliente
cliente1 = Cliente(1, "Cliente A", "Calle Principal 123")

# Crear una venta con los productos y el cliente
venta1 = Venta(cliente1, [producto1, producto2])

# Mostrar la información de la venta
print(venta1)
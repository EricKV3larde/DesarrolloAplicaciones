class Producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"Código: {self.codigo}, Nombre: {self.nombre}, Precio: ${self.precio:.2f}"

class Cliente:
    def __init__(self, id, nombre, direccion):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Dirección: {self.direccion}"

class Venta:
    def __init__(self, cliente, productos):
        self.cliente = cliente
        self.productos = productos

    def calcular_total(self):
        total = sum(producto.precio for producto in self.productos)
        return total

    def __str__(self):
        return f"Cliente: {self.cliente.nombre}\nProductos:\n{', '.join(producto.nombre for producto in self.productos)}\nTotal: ${self.calcular_total():.2f}"

# Almacenar objetos en listas
productos_registrados = []
clientes_registrados = []
ventas_registradas = []

# Crear y registrar productos
producto1 = Producto("P001", "Producto 1", 10.99)
productos_registrados.append(producto1)

producto2 = Producto("P002", "Producto 2", 5.49)
productos_registrados.append(producto2)

producto3 = Producto("P003", "Producto 3", 7.99)
productos_registrados.append(producto3)

producto4 = Producto("P004", "Producto 4", 12.99)
productos_registrados.append(producto4)

producto5 = Producto("P005", "Producto 5", 8.49)
productos_registrados.append(producto5)

# Crear y registrar clientes
cliente1 = Cliente(1, "Cliente A", "Calle Principal 123")
clientes_registrados.append(cliente1)

cliente2 = Cliente(2, "Cliente B", "Avenida Secundaria 456")
clientes_registrados.append(cliente2)

cliente3 = Cliente(3, "Cliente C", "Plaza Central 789")
clientes_registrados.append(cliente3)

cliente4 = Cliente(4, "Cliente D", "Ruta 66")
clientes_registrados.append(cliente4)

cliente5 = Cliente(5, "Cliente E", "Avenida Principal 567")
clientes_registrados.append(cliente5)

# Crear ventas y registrarlas
venta1 = Venta(cliente1, [producto1, producto2])
ventas_registradas.append(venta1)

venta2 = Venta(cliente2, [producto2, producto3, producto4])
ventas_registradas.append(venta2)

venta3 = Venta(cliente3, [producto1, producto5])
ventas_registradas.append(venta3)

venta4 = Venta(cliente4, [producto4, producto5])
ventas_registradas.append(venta4)

venta5 = Venta(cliente5, [producto1, producto2, producto3])
ventas_registradas.append(venta5)

# Mostrar información de los objetos registrados
print("Productos registrados:")
for producto in productos_registrados:
    print(producto)

print("\nClientes registrados:")
for cliente in clientes_registrados:
    print(cliente)

print("\nVentas registradas:")
for venta in ventas_registradas:
    print(venta)
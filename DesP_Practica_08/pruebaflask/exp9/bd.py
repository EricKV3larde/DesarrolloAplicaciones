import sqlite3

# a) CREANDO UNA BASE DE DATOS SQLITE EN PYTHON
# 4, 5, 6
conn = sqlite3.connect('ORDERS.db')  # Utiliza el mismo nombre de la base de datos en ambos lugares
# 7
# Puedes usar la siguiente línea para crear una base de datos en memoria
# conn = sqlite3.connect(':memory:')

# 8A
# Crear un objeto de cursor
cur = conn.cursor()

# 9

# b) CONECTARSE A LA BASE DE DATOS
# Comentamos la conexión a la base de datos 'ORDERS.db'
# Ya que ya estamos conectados a la misma base de datos en 'conn'
# conn_existing = sqlite3.connect('ORDERS.db')
# print("Base de datos abierta satisfactoriamente")

# c) CREANDO NUESTRAS TABLAS EN SQLITE PARA PYTHON
# 1, 2
# Crear la tabla users
cur.execute("""CREATE TABLE IF NOT EXISTS users(
 userid INT PRIMARY KEY,
 fname TEXT,
 lname TEXT,
 gender TEXT);
""")
conn.commit()

# 6, 7
# Crear la tabla orders
cur.execute("""CREATE TABLE IF NOT EXISTS orders(
 orderid INT PRIMARY KEY,
 date TEXT,
 userid TEXT,
 total TEXT);
""")
conn.commit()

# Cierra la conexión
conn.close()
# conn_existing.close()  # Comentamos la línea para cerrar una conexión que no está abierta

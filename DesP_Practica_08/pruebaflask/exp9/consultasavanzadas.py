import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('ORDERS.db')
cur = conn.cursor()

# a) SQLITE Y PREVENCIÓN DE ATAQUES DE INYECCIÓN

# 1. Variables con valores para cargar en la base de datos
order = (5, '15/06/2015', 3, 400215)

# 2. Cargar datos en la base de datos
cur.execute("INSERT INTO orders VALUES(?, ?, ?, ?);", order)
conn.commit()

# 3. Otra forma con una lista de tuplas
moreOrders = [(6, '03/10/2021', 3, 2015478), (7, '02/01/2019', 3, 2015698)]
cur.executemany("INSERT INTO orders VALUES(?, ?, ?, ?);", moreOrders)
conn.commit()

# b) USANDO FETCHONE () EN SQLITE CON PYTHON

# 1. Uso de la función fetchone()
cur.execute("SELECT * FROM orders;")
one_result = cur.fetchone()
print(one_result)

# 2. Resultado
# (1, '02/12/2021', '1', '25000.0')

# c) USANDO FETCHMANY () EN SQLITE CON PYTHON

# 1. Uso de la función fetchmany()
cur.execute("SELECT * FROM orders;")
three_results = cur.fetchmany(3)
print(three_results)

# 2. Resultado
# [(1, '02/12/2021', '1', '25000.0'), (3, '04/12/2019', '3', '415203'), (4, '02/09/2019', '4', '2541360')]

# d) USANDO FETCHALL () EN SQLITE CON PYTHON

# 1. Uso de la función fetchall()
cur.execute("SELECT * FROM orders;")
all_results = cur.fetchall()
print(all_results)

# e) UNIR TABLAS CON SQLITE EN PYTHON

# 2. Consulta compleja para unir tablas
cur.execute("""
    SELECT *, users.fname, users.lname
    FROM orders
    LEFT JOIN users ON users.userid = orders.userid;
""")
print(cur.fetchall())

# Cerrar la conexión
conn.close()

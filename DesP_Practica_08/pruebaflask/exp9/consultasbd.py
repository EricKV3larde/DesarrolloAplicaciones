import sqlite3

def insertar_registros():
    conn = sqlite3.connect('ORDERS.db')
    print("Base de datos abierta satisfactoriamente")

    # Insertar registros en la tabla ORDERS
    conn.execute("INSERT INTO ORDERS (ORDERID, DATE, USERID, TOTAL) VALUES (1, '02/12/2021', 1, 20000)")
    conn.execute("INSERT INTO ORDERS (ORDERID, DATE, USERID, TOTAL) VALUES (2, '02/10/2021', 2, 210)")
    conn.execute("INSERT INTO ORDERS (ORDERID, DATE, USERID, TOTAL) VALUES (3, '04/12/2019', 3, 415203)")
    conn.execute("INSERT INTO ORDERS (ORDERID, DATE, USERID, TOTAL) VALUES (4, '02/09/2019', 4, 2541360)")

    conn.commit()
    print("Registros creados satisfactoriamente")
    conn.close()

def seleccionar_registros():
    conn = sqlite3.connect('ORDERS.db')
    print("Base de datos abierta satisfactoriamente")

    # Seleccionar y mostrar registros de la tabla ORDERS
    cursor = conn.execute("SELECT ORDERID, DATE, USERID, TOTAL from ORDERS")
    for row in cursor:
        print("ORDERID = ", row[0])
        print("DATE = ", row[1])
        print("USERID = ", row[2])
        print("TOTAL = ", row[3], "\n")

    print("Operacion realizada satisfactoriamente")
    conn.close()

def actualizar_registros():
    conn = sqlite3.connect('ORDERS.db')
    print("Base de datos abierta satisfactoriamente")

    # Actualizar un registro en la tabla ORDERS
    conn.execute("UPDATE ORDERS set TOTAL = 25000.00 where ORDERID = 1")
    conn.commit()

    print("Número total de registros actualizados: ", conn.total_changes)

    # Seleccionar y mostrar registros actualizados
    cursor = conn.execute("SELECT ORDERID, DATE, USERID, TOTAL from ORDERS")
    for row in cursor:
        print("ORDERID = ", row[0])
        print("DATE = ", row[1])
        print("USERID = ", row[2])
        print("TOTAL = ", row[3], "\n")

    print("Actualización realizada satisfactoriamente")
    conn.close()

def eliminar_registro():
    conn = sqlite3.connect('ORDERS.db')
    print("Base de datos abierta satisfactoriamente")

    # Eliminar un registro en la tabla ORDERS
    conn.execute("DELETE from ORDERS where ORDERID = 2;")
    conn.commit()

    print("Número total de registros borrados: ", conn.total_changes)

    # Seleccionar y mostrar registros restantes
    cursor = conn.execute("SELECT ORDERID, DATE, USERID, TOTAL from ORDERS")
    for row in cursor:
        print("ORDERID = ", row[0])
        print("DATE = ", row[1])
        print("USERID = ", row[2])
        print("TOTAL = ", row[3], "\n")

    print("Eliminación realizada satisfactoriamente")
    conn.close()

# Ejecutar las operaciones
insertar_registros()
seleccionar_registros()
actualizar_registros()
eliminar_registro()

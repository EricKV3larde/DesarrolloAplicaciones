from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from datetime import datetime

app = Flask(__name__)

# Configuración de la base de datos
db = mysql.connector.connect(
    host="localhost",      
    user="root",      
    password="123456",  
    database="venta_pasajes"   
)

@app.route("/", methods=["GET", "POST"])
def calcular_precio():
    if request.method == "POST":
        fecha_nacimiento = request.form["fecha_nacimiento"]
        categoria = determinar_categoria(fecha_nacimiento)
        precio = calcular_precio_pasaje(categoria)
        return render_template("resultado.html", categoria=categoria, precio=precio)
    return render_template("formulario.html")

def determinar_categoria(fecha_nacimiento):
    # Calcula la edad a partir de la fecha de nacimiento
    fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
    hoy = datetime.now()
    edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))

    # Determina la categoría según la edad
    if edad >= 18:
        return "Adulto"
    elif 2 <= edad <= 17:
        return "Menor de Edad"
    else:
        return "Infante"

def calcular_precio_pasaje(categoria):
    cursor = db.cursor()
    cursor.execute("SELECT precio FROM precios WHERE categoria = %s", (categoria,))
    precio = cursor.fetchone()[0]
    cursor.close()
    return precio

if __name__ == "__main__":
    app.run(debug=True)
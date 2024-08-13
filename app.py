import os
from flask import Flask, render_template, request, redirect, session, url_for, flash
from flask_mysqldb import MySQL
import MySQLdb.cursors
# Crear la aplicación
app = Flask(__name__)

# Crear una llave secreta
app.secret_key = 'barberos_elites'

# Configurar la base de datos MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'elitebarber'

# Inicializar MySQL
mysql = MySQL(app)

@app.route('/')
def inicio():

    return render_template('./eliteBS/index.html')

@app.route('/clientes/')
def clientes():
    return render_template('./eliteBS/clientes.html')

@app.route('/agregar/cliente/', methods=['POST'])
def agg_client():
    nombre = request.form['nombre']
    telefono = request.form['telefono']
    
    conexion = mysql.connection
    cursor = conexion.cursor()
    
    cursor.execute("SELECT COALESCE(MAX(turno), 0) FROM clientes")
    max_turno = cursor.fetchone()[0]
    
    nuevo_turno = max_turno + 1
    
    cursor.execute("INSERT INTO clientes (id, nombre, telefono, turno) VALUES (NULL, %s, %s, %s)", (nombre, telefono, nuevo_turno))
    
    # Confirmar la transacción
    conexion.commit()
    
    # Cerrar la conexión
    cursor.close()
    conexion.close()
    
    # Usar flash para pasar un mensaje a la siguiente solicitud
    flash(f'Cliente: {nombre} agregado con éxito. Turno asignado: {nuevo_turno}')
    
    return redirect('/')

@app.route('/admin/')
def admin():
    return render_template('./admin/login.html')

@app.route('/admin/clientes/')
def admin_cliente():
    return render_template('./admin/clientes.html')

if __name__ == '__main__':
    app.run(port = 3000, debug=True)
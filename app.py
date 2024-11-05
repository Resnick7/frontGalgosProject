from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Configuración de la base de datos SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modelo de la tabla 'usuario'
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    mail = db.Column(db.String(100), unique=True, nullable=False)

# Crear la base de datos y tabla 'usuario'
with app.app_context():
    db.create_all()

# Ruta para mostrar el formulario
@app.route('/')
def index():
    return render_template('form.html')

# Ruta para procesar el formulario
@app.route('/submit', methods=['POST'])
def submit():
    nombre = request.form.get('nombre')
    apellido = request.form.get('apellido')
    mail = request.form.get('mail')

    # Guardar datos en la base de datos
    nuevo_usuario = Usuario(nombre=nombre, apellido=apellido, mail=mail)
    db.session.add(nuevo_usuario)
    db.session.commit()
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

from pymongo import MongoClient
from flask import Flask, request, render_template, redirect, url_for

# Establecer la cadena de conexión de Atlas
connection_string = "mongodb+srv://heyshaske:medicfy@cluster0.ksrc8pi.mongodb.net/"

client = MongoClient(connection_string)
db = client['test']  
users_collection = db['registro_usuarios'] 

app = Flask(__name__)


@app.route('/registro', methods=['GET'])
def registro():
    return render_template('registro.html', registro_exitoso=False)



@app.route('/register', methods=['POST'])
def register():
    first_name = request.form['first-name']
    last_name = request.form['last-name']
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirm-password']
    
    #verificar si el usuario ya existe en la base de datos
    if users_collection.find_one({'email': email}):
        return 'El usuario ya existe'
    
    #verificar si las contraseñas coinciden
    if password != confirm_password:
        return 'Las contraseñas no coinciden'
    
    #crear un nuevo documento para el usuario
    new_user = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'password': password
    }
    
    # Insertar el nuevo usuario en la colección
    users_collection.insert_one(new_user)
    
    return render_template('registro.html', registro_exitoso=True)

# Ruta para el inicio de sesión de usuarios
@app.route('/login', methods=['POST'])
def login():
    # Obtener los datos del formulario de inicio de sesión
    email = request.form['email']
    password = request.form['password']
    
    # Verificar las credenciales del usuario en la base de datos
    user = users_collection.find_one({'email': email, 'password': password})
    if user:
        return redirect(url_for('menu'))
    else:
        return render_template('iniciar-sesion.html', error='Credenciales inválidas')


@app.route('/inicio')
def inicio():
    return render_template('iniciar-sesion.html')


@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/recordatorios')
def recordatorios():
    return render_template('recordatorios.html')

@app.route('/integrantes')
def integrantes():
    return render_template('quienes-somos.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/membresias')
def membresias():
    return render_template('membresias.html')

if __name__ == '__main__':
    app.run()

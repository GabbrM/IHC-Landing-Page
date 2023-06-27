from pymongo import MongoClient
from flask import Flask, request, render_template


client = MongoClient('mongodb://localhost:27017/')
db = client['test']  
users_collection = db['registro_usuarios'] 

app = Flask(__name__)


@app.route('/registro', methods=['GET'])
def registro():
    return render_template('registro.html') 


@app.route('/register', methods=['POST'])
def register():
  
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    
   
    if users_collection.find_one({'username': username}):
        return 'El usuario ya existe'
    

    new_user = {
        'username': username,
        'email': email,
        'password': password
    }
    
    # Insertar el nuevo usuario en la colección
    users_collection.insert_one(new_user)
    
    return 'Registro exitoso'

# Ruta para el inicio de sesión de usuarios
@app.route('/login', methods=['POST'])
def login():
    # Obtener los datos del formulario de inicio de sesión
    username = request.form['username']
    password = request.form['password']
    
    # Verificar las credenciales del usuario en la base de datos
    user = users_collection.find_one({'username': username, 'password': password})
    if user:
        return 'Inicio de sesión exitoso'
    else:
        return 'Credenciales inválidas'


if __name__ == '__main__':
    app.run()

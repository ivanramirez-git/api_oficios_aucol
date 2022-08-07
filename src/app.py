# importamos flask
from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_marshmallow import Marshmallow
from config import config

app = Flask(__name__)
app.config.from_object(config['development'])


db = MySQL(app)
ma = Marshmallow(app)

# Models:
from models.ModelUser import ModelUser

# Entities:
from models.entities.User import User

# Creación de tablas
    
# Ruta login
@app.route('/login', methods=['POST'])
def login():
    # Obtenemos los datos del usuario
    print(request.json)
    user =  User(None, request.json['username'], request.json['password'], None, None, None, None)
    logger_user = ModelUser.login(db, user)
    if logger_user is not None:
        return jsonify(logger_user.__dict__)
    else:
        return jsonify({"error": "Usuario o contraseña incorrectos"})

# Ruta registro
@app.route('/register', methods=['POST'])
def register():
    # Obtenemos los datos del usuario
    print(request.json)
    user =  User(0, request.json['username'], request.json['password'], request.json['email'], request.json['fullname'], request.json['role'], request.json['code'])
    if ModelUser.register(db, user):
        return jsonify({"success": "Usuario registrado correctamente"})
    else:
        return jsonify({"error": "Usuario o contraseña incorrectos"})

# Ruta Consula por id
@app.route('/get_by_id/<int:id>', methods=['GET'])
def get_by_id(id):
    user = ModelUser.get_by_id(db, id)
    if user is not None:
        return jsonify(user.__dict__)
    else:
        return jsonify({"error": "Usuario no encontrado"})

# Inicio del programa
if __name__ == '__main__':
    app.run()
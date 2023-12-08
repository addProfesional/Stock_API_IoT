from src.data_example.users import usuarios

#Routes
from .routes import DevicesRoutes, UsersRoutes, MerchantRoutes
from .database.Database import Database, obtener_sqlalchemy, db
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import os
servidor = Flask(__name__)

# Configura SQLAlchemy con la URL de la base de datos
servidor.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Gmo901pKeL#@192.168.1.110/notes'
# servidor.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

root_dir = os.path.dirname(__file__)
cert = os.path.join(root_dir, 'utils/server.crt')
clave_privada = os.path.join(root_dir, 'utils/server.key')
ssl_context = (cert, clave_privada)

# SQLAlchemy(servidor)
db.init_app(servidor)

@servidor.route('/')
def index():
    return 'Index!'
def iniciar():

    #Blueprints
    servidor.register_blueprint(DevicesRoutes.router, url_prefix='/dispositivos')
    servidor.register_blueprint(UsersRoutes.router, url_prefix='/usuarios')
    servidor.register_blueprint(MerchantRoutes.router, url_prefix='/mercancias')
    print('Iniciando la aplicación')
    print(root_dir)
    return servidor

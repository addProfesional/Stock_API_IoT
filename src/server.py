from src.data_example.users import usuarios

#Routes
from .routes import DevicesRoutes, UsersRoutes, MerchantRoutes
from flask import Flask

import os
servidor = Flask(__name__)

root_dir = os.path.dirname(__file__)
cert = os.path.join(root_dir, 'utils/server.crt')
clave_privada = os.path.join(root_dir, 'utils/server.key')
ssl_context = (cert, clave_privada)
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

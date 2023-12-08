#Routes
from .routes import DevicesRoutes, UsersRoutes, MerchantRoutes, InventoryRoutes, HistoryRoutes
from .database.Database import Database, db
from flask import Flask

import os
servidor = Flask(__name__)

# Configura SQLAlchemy con la URL de la base de datos
servidor.config['SQLALCHEMY_DATABASE_URI'] = Database.obtener_uri()
# servidor.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

root_dir = os.path.dirname(__file__)
cert = os.path.join(root_dir, 'utils/server.crt')
clave_privada = os.path.join(root_dir, 'utils/server.key')
ssl_context = (cert, clave_privada)

db.init_app(servidor)

@servidor.route('/')
def index():
    return 'Index!'
def iniciar():

    #Blueprints
    servidor.register_blueprint(DevicesRoutes.router, url_prefix='/dispositivos')
    servidor.register_blueprint(UsersRoutes.router, url_prefix='/usuarios')
    servidor.register_blueprint(MerchantRoutes.router, url_prefix='/mercancias')
    servidor.register_blueprint(InventoryRoutes.router, url_prefix='/inventarios')
    servidor.register_blueprint(HistoryRoutes.router, url_prefix='/historial')

    return servidor

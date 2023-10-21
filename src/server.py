from src.data_example.users import usuarios

#Routes
from .routes import DevicesRoutes, UsersRoutes, MerchantRoutes
from flask import Flask
aervidor = Flask(__name__)

@aervidor.route('/')
def index():
    return 'Index!'
def iniciar():
    #Blueprints
    aervidor.register_blueprint(DevicesRoutes.router, url_prefix='/dispositivos')
    aervidor.register_blueprint(UsersRoutes.router, url_prefix='/usuarios')
    aervidor.register_blueprint(MerchantRoutes.router, url_prefix='/mercancias')
    print('Iniciando la aplicación')
    return aervidor

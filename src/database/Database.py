import mysql.connector as mariadb
from mysql.connector import Error
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from dotenv import load_dotenv
import os

class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
load_dotenv('.env.dev')

class Database:
    _conexion = None
    @staticmethod
    def obtener_uri():
        user = os.environ.get('USER_DB')
        password = os.environ.get('PASS_DB')
        host = os.environ.get('HOST_DB')
        db_name = os.environ.get('DB_NAME')

        uri = 'mysql://'+user+':'+password+'@'+host+'/'+db_name
        return uri

    @classmethod
    def obtener_conexion(cls):
        if cls._conexion is None:
            cls._conexion = cls._crear_conexion()
        return cls._conexion

    @classmethod
    def _crear_conexion(cls):
        try:
            conexion = mariadb.connect(
                host='192.168.1.110',
                user='root',
                password='Gmo901pKeL#',
                database='notes'
            )
            print('Conexión establecida')
            return conexion
        except Error as e:
            print(f'Error: {e}')
            return None


def obtener_sqlalchemy(app):
    # Configura la aplicación Flask con SQLAlchemy
    db.init_app(app)
    return db

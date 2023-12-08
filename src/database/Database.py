import mysql.connector as mariadb
from mysql.connector import Error
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class Database:
    _conexion = None

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

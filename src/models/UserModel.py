from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.orm import Mapped, mapped_column
from ..database.Database import Database
from ..database.Database import db

# db = Database.obtener_conexion()

class UserModel(db.Model):
    __tablename__ = 'usuarios'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    username: Mapped[str] = mapped_column(String(32))
    email: Mapped[str] = mapped_column(String(255))
    num_employee: Mapped[str] = mapped_column(String(32))
    number_phone: Mapped[str] = mapped_column(String(16))
    risk_rating: Mapped[int] = mapped_column(Integer)
    password: Mapped[str] = mapped_column(String(500))
    roles: Mapped[str] = mapped_column(String(32))

    '''id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    username = Column(String(32))
    email = Column(String(255))
    num_employee = Column(String(32))
    number_phone = Column(String(16))
    risk_rating = Column(Integer)
    password = Column(String(500))
    roles = Column(String(32))'''

    def __init__(self, name, username, email, num_employee, number_phone, risk_rating, password, roles):
        self.name = name
        self.username = username
        self.email = email
        self.num_employee = num_employee
        self.number_phone = number_phone
        self.risk_rating = risk_rating
        self.password = password
        self.roles = roles

    @classmethod
    def crear_desde_json(cls, datos_json):
        # Crea una instancia del modelo a partir de un diccionario JSON
        return cls(**datos_json)
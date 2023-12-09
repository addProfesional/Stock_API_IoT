from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from ..database.Database import db

class UserModel(db.Model):
    __tablename__ = 'usuarios'

    user_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    username: Mapped[str] = mapped_column(String(32))
    email: Mapped[str] = mapped_column(String(255))
    num_employee: Mapped[str] = mapped_column(String(32))
    number_phone: Mapped[str] = mapped_column(String(16))
    risk_rating: Mapped[int] = mapped_column(Integer)
    password: Mapped[str] = mapped_column(String(500))
    roles: Mapped[str] = mapped_column(String(32))
    created_at: Mapped[int] = mapped_column(Integer)
    deleted: Mapped[bool] = mapped_column(Boolean)

    def __init__(self, name, username, email, num_employee, number_phone, risk_rating, password, roles, deleted, created_at):
        self.name = name
        self.username = username
        self.email = email
        self.num_employee = num_employee
        self.number_phone = number_phone
        self.risk_rating = risk_rating
        self.password = password
        self.roles = roles
        self.deleted = deleted
        self.created_at = created_at

    @classmethod
    def crear_desde_json(cls, datos_json):
        # Crea una instancia del modelo a partir de un diccionario JSON
        return cls(**datos_json)
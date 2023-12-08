from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from ..database.Database import db

class DevicesModel(db.Model):
    __tablename__ = 'dispositivos'

    device_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(128))
    type: Mapped[str] = mapped_column(String(50))
    created_at: Mapped[int] = mapped_column(Integer)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('usuarios'))

    def __init__(self, name, type, created_at, user_id):
        self.name = name
        self.type = type
        self.created_at = created_at
        self.user_id = user_id

    @classmethod
    def crear_desde_json(cls, datos_json):
        # Crea una instancia del modelo a partir de un diccionario JSON
        return cls(**datos_json)
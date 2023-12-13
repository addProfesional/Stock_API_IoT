from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from ..database.Database import db

class AppConfigModel(db.Model):
    __tablename__ = 'appconfig'

    config_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    time_session: Mapped[int] = mapped_column(Integer)
    created_at: Mapped[int] = mapped_column(Integer)

    def __init__(self, time_session, created_at):
        self.time_session = time_session
        self.created_at = created_at

    @classmethod
    def crear_desde_json(cls, datos_json):
        # Crea una instancia del modelo a partir de un diccionario JSON
        return cls(**datos_json)
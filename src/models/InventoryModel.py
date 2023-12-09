from sqlalchemy import Integer, String, Boolean, ForeignKey, Float
from sqlalchemy.orm import Mapped, mapped_column
from ..database.Database import db

class InventoryModel(db.Model):
    __tablename__ = 'inventarios'

    inventory_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    merchant_id: Mapped[int] = mapped_column(Integer, ForeignKey('mercancias'))
    quantity: Mapped[int] = mapped_column(Integer)
    description: Mapped[str] = mapped_column(String(255))
    value:  Mapped[float] = mapped_column(Float)
    deleted: Mapped[bool] = mapped_column(Boolean)
    created_at: Mapped[int] = mapped_column(Integer)


    def __init__(self, name, merchant_id, quantity, description, value, deleted, created_at):
        self.name = name
        self.merchant_id = merchant_id
        self.quantity = quantity
        self.description = description
        self.value = value
        self.deleted = deleted
        self.created_at = created_at


    @classmethod
    def crear_desde_json(cls, datos_json):
        # Crea una instancia del modelo a partir de un diccionario JSON
        return cls(**datos_json)
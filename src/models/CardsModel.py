from sqlalchemy import Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional
from ..database.Database import db

class CardsModel(db.Model):
    __tablename__ = 'cards'

    card_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    uuid_card: Mapped[str] = mapped_column(String(128))
    type: Mapped[str] = mapped_column(String(50))  # { 'MERCHANT', 'USER', 'ADMIN' }
    created_at: Mapped[int] = mapped_column(Integer)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('usuarios'))
    merchant_id : Mapped[Optional[int]] = mapped_column(Integer, ForeignKey('mercancias'), nullable=True)
    deleted: Mapped[bool] = mapped_column(Boolean)

    def __init__(self, uuid_card, type, created_at, user_id, merchant_id, deleted):
        self.uuid_card = uuid_card
        self.type = type
        self.created_at = created_at
        self.user_id = user_id
        self.merchant_id = merchant_id
        self.deleted = deleted

    @classmethod
    def crear_desde_json(cls, datos_json):
        # Crea una instancia del modelo a partir de un diccionario JSON
        return cls(**datos_json)
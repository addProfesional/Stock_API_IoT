from sqlalchemy import Integer, String, Boolean, ForeignKey, BigInteger
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional
from ..database.Database import db

class HistoryModel(db.Model):
    __tablename__ = 'historial'

    history_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    type: Mapped[str] = mapped_column(String(20))  # { 'InvIn', 'InvOut', 'AccessIn', 'AccessOut', 'newMerchant'}
    user_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey('usuarios'), nullable=True)
    device_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey('dispositivos'), nullable=True)
    inventory_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey('inventarios'), nullable=True)
    merchant_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey('mercancias'), nullable=True)
    created_at: Mapped[int] = mapped_column(BigInteger)
    deleted: Mapped[bool] = mapped_column(Boolean)

    def __init__(self, type, user_id, device_id, inventory_id, merchant_id, created_at, deleted):
        self.type =  type
        self.user_id = user_id
        self.device_id = device_id
        self.inventory_id = inventory_id
        self.merchant_id = merchant_id
        self.deleted = deleted
        self.created_at = created_at

    @classmethod
    def crear_desde_json(cls, datos_json):
        # Crea una instancia del modelo a partir de un diccionario JSON
        return cls(**datos_json)
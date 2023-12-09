from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from ..database.Database import db

class MerchantModel(db.Model):
    __tablename__ = 'mercancias'

    merchant_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    categories: Mapped[str] = mapped_column(String(1000))
    name: Mapped[str] = mapped_column(String(128))
    unit_of_measure: Mapped[str] = mapped_column(String(50))  # { 'UNIT', 'KG', 'LT', ... }
    barcode: Mapped[str] = mapped_column(String(128))
    type_of_merchant: Mapped[str] = mapped_column(String(50))   # { 'UNIT', 'PACK' }
    rfid_code : Mapped[str] = mapped_column(String(254))
    created_at: Mapped[int] = mapped_column(Integer)
    deleted:  Mapped[bool] = mapped_column(Boolean)

    def __init__(self, categories, name, unit_of_measure, barcode, type_of_merchant, rfid_code, created_at, deleted):
        self.categories = categories
        self.name = name
        self.unit_of_measure = unit_of_measure
        self.barcode = barcode
        self.type_of_merchant = type_of_merchant
        self.rfid_code = rfid_code
        self.created_at = created_at
        self.deleted = deleted

    @classmethod
    def crear_desde_json(cls, datos_json):
        # Crea una instancia del modelo a partir de un diccionario JSON
        return cls(**datos_json)
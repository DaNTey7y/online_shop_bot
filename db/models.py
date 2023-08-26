from sqlalchemy import Column, BigInteger, Integer, DATE, VARCHAR, TEXT
from datetime import datetime

from .base import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(BigInteger, unique=True, nullable=False, primary_key=True, autoincrement=False)

    orders_amount = Column(Integer, default=0)

    reg_date = Column(DATE, default=datetime.today().date())

    def __str__(self):
        return f"<User:{self.user_id}>"


class Section(Base):
    __tablename__ = "sections"

    section_id = Column(Integer, unique=True, primary_key=True)

    name = Column(VARCHAR(255))

    section_image_path = Column(TEXT)

    image_caption = Column(TEXT)


class Product(Base):
    __tablename__ = "goods"

    product_id = Column(Integer, unique=True, primary_key=True)

    section_id = Column(Integer)

    cost = Column(Integer)

    name = Column(VARCHAR(255))

    def __str__(self):
        return f"<Product:_section#{self.section_id};_id#{self.product_id}>"

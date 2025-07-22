from sqlalchemy import create_engine, Column, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from datetime import datetime
import uuid

Base = declarative_base()

class Product(Base):
    __tablename__ = "products"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    your_price = Column(Float, nullable=False)
    url = Column(String)

from sqlalchemy import Column, Integer, Float, String
from app import db


class Coefficient(db.Model):
    __tablename__ = 'coefficients'
    id = Column(Integer, primary_key=True)
    a = Column(Float())
    b = Column(Float())
    c = Column(Float())
    x1 = Column(String(10))
    x2 = Column(String(10))

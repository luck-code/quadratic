from sqlalchemy import MetaData, Table, Column, Integer, Float, String
from sqlalchemy.ext.declarative import declarative_base
from flask import request
from app import db

metadata = MetaData()
Base = declarative_base()


class Coefficient(db.Model):
    __tablename__ = 'coefficients'
    id = Column(Integer, primary_key=True)
    a = Column(Float())
    b = Column(Float())
    c = Column(Float())
    x1 = Column(String(10))
    x2 = Column(String(10))

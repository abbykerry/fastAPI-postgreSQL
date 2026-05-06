from sqlalchemy import Column, Integer, String
from database import Base

class Farmer(Base):
    __tablename__ = "farmers"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    phone_number = Column(String, unique=True, nullable=False)
    cluster = Column(String, nullable=True)
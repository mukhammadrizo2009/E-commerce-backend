import enum 
from datetime import datetime
from sqlalchemy import (Column, Integer, String, Text,
DateTime, CheckConstraint, Enum)
from schemas.database import Base

class Genre(str, enum.Enum):
    pass

class Book(Base):
    __tablename__ = "books"
    
    book_id = Column("id", Integer, primary_key=True, index=True, nullable=False)
    book_title = Column
    author = Column
    price = Column
    quantity = Column
    pages = Column
    genre = Column
    description = Column
    
    created_at = Column
    updated_at = Column
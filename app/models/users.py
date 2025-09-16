import enum 
from datetime import datetime
from sqlalchemy import (Column, Integer, String, Numeric, Text,
DateTime, CheckConstraint, Enum)
from app.schemas.database import Base

class Genre(str, enum.Enum):
    # O‘zbek adabiyoti
    SHE_RIYAT = "She’riyat"
    DOSTON = "Doston"
    NASR = "Nasr"
    DRAMA = "Drama"
    FOLKLOR = "Folklor"
    QISSA = "Qissa"
    ROMAN = "Roman"
    ERTak = "Ertak"
    MAQOL_MATAL = "Maqol va matal"
    LATIFA = "Latifa"

    # Jahon adabiyoti
    FICTION = "Badiiy adabiyot"
    FANTASY = "Fantastika"
    SCIENCE_FICTION = "Ilmiy fantastika"
    DETECTIVE = "Detektiv"
    HISTORICAL = "Tarixiy"
    BIOGRAPHY = "Biografiya"
    POETRY = "She’riyat (jahon)"
    DRAMA_WORLD = "Drama (jahon)"
    TRAGEDY = "Tragediya"
    COMEDY = "Komedya"
    SATIRE = "Satira"
    LITERARY_CRITICISM = "Adabiy tanqid"
    ADVENTURE_FANTASY = "Fantastik sarguzasht"
    PSYCHOLOGICAL = "Psixologik roman"

class Book(Base):
    __tablename__ = "books"
    
    book_id = Column("id", Integer, primary_key=True, index=True, nullable=False)
    book_title = Column(String(length=64), nullable=False)
    author = Column(String(length=64), nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    quantity = Column(Integer, CheckConstraint("quantity >= 0"), nullable=False)
    pages = Column(Integer, CheckConstraint("pages >= 1"), nullable=False)
    genre = Column(Enum(Genre), nullable=False)
    description = Column(Text)
    
    created_at = Column("created_at", DateTime, default=datetime.now())
    updated_at = Column("updated_at", DateTime, onupdate=datetime.now())
from typing import Annotated
from enum import Enum 
from fastapi import FastAPI, Path, Query, Depends, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from app.schemas.database import Base, engine , get_db, SessionLocal
from app.models.users import Book , Genre


app = FastAPI(title="Bookshop")
Base.metadata.create_all(engine)

@app.get("/api/books/{book_id}")
def get_book_detail(
    book_id: Annotated[int, Path(title="Bitta kitob ID", ge=1, le=1000000)],
    db: Annotated[Session, Depends(get_db)]
):
    result = db.query(Book).filter(Book.book_id == book_id).first()
    if not result:
        raise HTTPException(
            status_code=404,
            detail=f"ID {book_id} bo'lgan kitob toplimadi"
        )
    return {
        "id": result.book_id,
        "title": result.book_title,
        "author": result.author,
        "price": float(result.price),
        "quantity": result.quantity,
        "pages": result.pages,
        "genre": result.genre.value if result.genre else None,
        "description": result.description,
        "created_at": result.created_at,
        "updated_at": result.updated_at,
    }
class BookCreate(BaseModel):
    book_title: str
    author: str
    price: float
    quantity: int
    pages: int
    genre: Genre
    description: str | None = None
    
@app.post("/api/books/")
def created_book(
    book_data: BookCreate,
    db: Annotated[Session , Depends(get_db)]
):
    book = Book(
        book_title=book_data.book_title,
        author=book_data.author,
        price=book_data.price,
        quantity=book_data.quantity,
        pages=book_data.pages,
        genre=book_data.genre,
        description=book_data.description 
    )
    db.add(book)
    db.commit()
    db.refresh(book)
    return {
        "id": book.book_id,
        "title": book.book_title,
        "author": book.author,
        "price": float(book.price),
        "quantity": book.quantity,
        "pages": book.pages,
        "genre": book.genre.value,
        "description": book.description,
        "created_at": book.created_at,
        "updated_at": book.updated_at,
    }
    
@app.delete("/books/{book_id}")
def delete_book(
    book_id: int,
    db: Annotated[Session, Depends(get_db)]
):
    book = db.query(Book).filter(Book.book_id == book_id).first()
    if not book:
        raise HTTPException(
            status_code=404,
            detail=f"Book with id {book_id} no found"
        )
    db.delete(book)
    db.commit()
    return {"message": f"Book with id {book_id} deleted successfully"}

@app.put("/books/{book_id}")
def edit_book(
    book_id: int,
    book_data: BookCreate,
    db: Annotated[Session, Depends(get_db)]
):
    book = db.query(Book).filter(Book.book_id == book_id).first()
    if not book:
        raise HTTPException(
            status_code=404,
            detail=f"Book with id {book_id} no found"
        )
    book.book_title = book_data.book_title
    book.author = book_data.author
    book.price = book_data.price
    book.quantity = book_data.quantity
    book.pages = book_data.pages
    book.genre = book_data.genre
    book.description = book_data.description

    db.commit()
    db.refresh(book)

    return {
        "message": f"Book with id {book_id} updated successfully",
        "book": {
            "id": book.book_id,
            "title": book.book_title,
            "author": book.author,
            "price": float(book.price),
            "quantity": book.quantity,
            "pages": book.pages,
            "genre": book.genre.value,
            "description": book.description,
            "created_at": book.created_at,
            "updated_at": book.updated_at,
        }
    }
    
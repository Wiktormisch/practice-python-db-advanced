from db import Session, engine
from models import Base, Author, Book
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from sqlalchemy import func


Base.metadata.create_all(engine)

# Dodawanie autorow i ksiazek

with Session(engine) as session:
    try:
        author_1 = Author(name="Maciek Nowak")
        author_2 = Author(name="Anna Kowalska")
        book_1 = Book(title="Python dla poczatkujacych", author=author_1)
        book_2 = Book(title="Golf w praktyce", author=author_2)
        book_3 = Book(title="Podstawy tenisa", author=author_2)
        book_4 = Book(title="Gotowanie krok po kroku", author=author_2)
        session.add_all([author_1, author_2, book_1,
                        book_2, book_3, book_4])
        session.commit()
        print("Autorzy i ksiazki dodani pomyslnie")
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Blad podczas dodawania autorow i ksiazek: {e}")

# Odczytywanie ksiazek autora Maciek Nowak

with Session(engine) as session:
    try:
        nowak_books = session.query(Book).filter(
            Book.author.has(name="Maciek Nowak")).all()
        print("Ksiazki autorstwa Maciek Nowak:")
        for book in nowak_books:
            print(f"- {book.title}")
    except SQLAlchemyError as e:
        print(f"Blad pobierania ksiazek: {e}")

# Wypisanie autorow ktorzy maja wiecej niz 1 ksiazke

with Session(engine) as session:
    try:
        authors_query = (session.query(Author, func.count(Book.id).label(
            "book_count"))).join(Book).group_by(Author.id).having(func.count(Book.id) > 1)

        results = authors_query.all()

        print("Autorzy z wiecej niz jedna ksiazka:")
        for author, count_books in results:
            print(author.name, count_books)
    except SQLAlchemyError as e:
        print(f"Blad pobrania autorow:  {e}")
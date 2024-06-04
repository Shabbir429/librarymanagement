from src.author_book.models.author_books import AuthorBook
from database import Base, engine

Base.metadata.create_all(engine)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("postgresql://postgres:postgres@localhost/postgres",
    echo=True
)

Base=declarative_base()

SessionLocal=sessionmaker(bind=engine)
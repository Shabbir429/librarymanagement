from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("postgresql://lb@1234:lb@1234@localhost/postgres",
    echo=True
)

Base=declarative_base()

SessionLocal=sessionmaker(bind=engine)
# from sqlalchemy.sql.expression import null
from database import Base
from sqlalchemy import String, Integer, Column


class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    city = Column(String(30))

    def __repr__(self):
        return f"<Student name={self.name} city={self.city}>"

# from sqlalchemy.sql.expression import null
from database import Base
from sqlalchemy import String, Integer, Column, Float, Date, ForeignKey, relationship

class Payment(Base):
    __tablename__ = 'payment'
    id = Column(Integer, primary_key=True, autoincrement=True)
    member_id = Column(Integer, ForeignKey('members.id'), nullable=False)
    amount = Column(Float, nullable=False)
    payment_date = Column(Date, nullable=False)
    payment_method = Column(String(50), nullable=False)
    member = relationship('Member', back_populates='payments')


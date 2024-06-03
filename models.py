# from sqlalchemy.sql.expression import null
from database import Base
from sqlalchemy import String, Integer, Column, Float, Date, ForeignKey

class Payment(Base):
    __tablename__ = 'payment'
    id = Column(Integer, primary_key=True, autoincrement=True)
    member_id = Column(Integer, ForeignKey('members.id'), nullable=False)
    amount = Column(Float, nullable=False)
    payment_date = Column(Date, nullable=False)
    payment_method = Column(String(50), nullable=False)


    def __repr__(self):
        return f"<Payment member_id={self.member_id} amount={self.amount} payment_date={self.payment_date} payment_method={self.payment_method}>"
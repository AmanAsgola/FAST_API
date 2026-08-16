from sqlalchemy import Column, Integer, String, Float, DateTime
from Database import Base

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    amount = Column(Float)
    category = Column(String, index=True)
    date = Column(DateTime)
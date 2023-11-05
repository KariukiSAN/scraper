from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Company(Base):
    __tablename__ = 'companies'

    rank = Column(Integer, primary_key=True)
    name = Column(String)
    industry = Column(String)
    revenue = Column(String)
    revenue_growth = Column(String)
    employees = Column(String)
    headquarters = Column(String)

    def __str__(self):
        return f"Rank: {self.rank}\nName: {self.name}\nIndustry: {self.industry}\nRevenue: {self.revenue}\nRevenue Growth: {self.revenue_growth}\nEmployees: {self.employees}\nHeadquarters: {self.headquarters}\n"
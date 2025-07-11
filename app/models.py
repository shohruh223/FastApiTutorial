from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, CheckConstraint, Text
from sqlalchemy.orm import relationship
from .database import Base


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, nullable=False, index=True)

    # One-to-many: Category → Products
    products = relationship("Product", back_populates="category", cascade="all, delete")

    def __str__(self):
        return self.title


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    image = Column(String, nullable=False)
    title = Column(String, nullable=False, index=True)

    # ForeignKey to category table
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False, index=True)
    category = relationship("Category", back_populates="products")  # assuming reverse relation

    price = Column(Numeric(10, 2), nullable=False, index=True)  # Decimal: max 99999999.99
    review = Column(Integer, CheckConstraint('review BETWEEN 1 AND 5'), nullable=True, index=True)
    text = Column(Text, nullable=True)
    quantity = Column(Integer, nullable=True, default=1, index=True)




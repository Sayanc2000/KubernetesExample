from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    password = Column(String)

    blogs = relationship("Blog", back_populates="writer")


class Blog(Base):
    __tablename__ = "blogs"
    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)

    writerId = Column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    writer = relationship("User", back_populates="blogs")

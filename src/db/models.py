from sqlalchemy import Column, Integer, VARCHAR, TEXT, ForeignKey
from sqlalchemy.orm import relationship
from src.db import Base


class User(Base):
    __tablename__ = "users"

    telegram_id = Column(Integer, unique=True, nullable=False)
    user_name = Column(VARCHAR(50), unique=True, nullable=True)

    urls = relationship("ShortedUrl", back_populates="user")

    def __str__(self) -> str:
        return f"<User: {self.user_id}>"


class ShortedUrl(Base):
    __tablename__ = "urls"

    original_url = Column(TEXT, nullable=False, unique=False)
    shorted_url = Column(TEXT, nullable=False, unique=False)
    title = Column(VARCHAR(100), nullable=False, unique=False)
    telegram_id = Column(Integer, ForeignKey('users.telegram_id'))

    user = relationship("User", back_populates="urls")

    def __str__(self) -> str:
        return f"<Title: {self.title}>"

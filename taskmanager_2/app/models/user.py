from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.backend.db import Base
import slugify


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)

    tasks = relationship("Task", back_populates="user")

    def __repr__(self):
        return f"<User(id={self.id!r}, username={self.username!r})>"

    @classmethod
    def create_slug(cls, name):
      return slugify.slugify(name)
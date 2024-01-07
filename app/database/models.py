from sqlalchemy import create_engine, String, ForeignKey, inspect
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, declared_attr, Session
from typing import List

class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    
    @classmethod
    @declared_attr
    def __tablename__(cls):
        """Задаёт таблице имя по умолчанию, как имя класса"""
        return cls.__name__.lower()

class User(Base):
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False)
    fullname: Mapped[str] = mapped_column(nullable=False)
    
    mems: Mapped[List["Mem"]] = relationship(back_populates='user')
    
    def __repr__(self):
        return f'UserModel(id={self.id!r}, username={self.username!r})'

class Mem(Base):
    __tablename__ = 'mems'
    
    mem_name: Mapped[str] = mapped_column(String(30))
    user_id = mapped_column(ForeignKey('users.id'))
    
    user: Mapped[User] = relationship(back_populates='mems')
    
    def __repr__(self):
        return f'MemModel(id={self.id}, mem_name={self.mem_name})'


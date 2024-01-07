from sqlalchemy import String, ForeignKey
from sqlalchemy.ext.asyncio import AsyncAttrs

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, declared_attr
from typing import List

class Base(AsyncAttrs, DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    
    user_id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False)
    fullname: Mapped[str] = mapped_column(nullable=False)
    
    mems: Mapped[List["Mem"]] = relationship(back_populates='user')
    
    def __repr__(self):
        return f'UserModel(user_id={self.user_id!r}, username={self.username!r})'

class Mem(Base):
    __tablename__ = 'mems'
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    
    mem_name: Mapped[str] = mapped_column(String(30))
    user_id = mapped_column(ForeignKey('users.user_id'))
    
    user: Mapped[User] = relationship(back_populates='mems')
    
    def __repr__(self):
        return f'MemModel(id={self.id}, mem_name={self.mem_name}, user={self.user.username})'


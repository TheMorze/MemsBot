from sqlalchemy import create_engine, String, ForeignKey, inspect
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, declared_attr, Session
from typing import List

engine = create_engine(url='sqlite+pysqlite:///:memory:', echo=True)
session = Session(engine)

class AbstractModel(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    
    @classmethod
    @declared_attr
    def __tablename__(cls):
        """Задаёт таблице имя по умолчанию, как имя класса"""
        return cls.__name__.lower()

class UserModel(AbstractModel):
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False)
    fullname: Mapped[str] = mapped_column(nullable=False)
    
    mems: Mapped[List["MemModel"]] = relationship(back_populates='user')
    
    def __repr__(self):
        return f'UserModel(id={self.id!r}, username={self.username!r})'

class MemModel(AbstractModel):
    __tablename__ = 'mems'
    
    mem_name: Mapped[str] = mapped_column(String(30))
    user_id = mapped_column(ForeignKey('users.id'))
    
    user: Mapped[UserModel] = relationship(back_populates='mems')
    
    def __repr__(self):
        return f'MemModel(id={self.id}, mem_name={self.mem_name})'

AbstractModel.metadata.create_all(engine)

user = UserModel(id=123,
                username='Zorex',
                fullname='Stas Cool')

session.add(user)
print(session.new)
print(session.dirty)
session.flush()

user.fullname = 'Stas COOLEST'
print(session.new)
print(session.dirty)


from loguru import logger

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session


from app.database.models import Base, User, Mem


class Database:
    
    __engine = create_engine(url='sqlite+pysqlite:///app/database/database.db', echo=True)
    
    @classmethod
    def create_tables(cls):
        Base.metadata.create_all(cls.__engine)
    
    @classmethod
    def add_user(cls, user_id: int, username: str, fullname: str) -> None:
        with Session(cls.__engine) as session:
            
            user = session.get(User, user_id)
            
            if not user:
                user = User(id=user_id,
                            username=username,
                            fullname=fullname)
                
                session.add(user)
                session.commit()
            
            else:
                logger.info('Пользователь уже находится в базе данных!')

    @classmethod
    def add_mem(cls, mem_name: str, user_id: int) -> None:
        with Session(cls.__engine) as session:
            mem = Mem(mem_name=mem_name,
                      user_id=user_id)
            
            session.add(mem)
            session.commit()

    @classmethod
    def get_mem(cls, mem_id: int) -> Mem:
        with Session(cls.__engine) as session:
            mem = session.get(Mem, mem_id)
            
            return mem





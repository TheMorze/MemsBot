from loguru import logger
from typing import Tuple

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, \
                                   AsyncSession


from app.database.models import Base, User, Mem


class Database:
    
    __engine = create_async_engine(url='sqlite+aiosqlite:///app/database/database.db', echo=True)
    __async_session = async_sessionmaker(__engine, expire_on_commit=False)
    
    @classmethod
    async def create_tables(cls):
        async with cls.__engine.begin() as conn: 
            await conn.run_sync(Base.metadata.create_all)
    
    @classmethod
    async def add_user(cls, user_id: int, username: str, fullname: str) -> Tuple[User, bool]:
        async with cls.__async_session() as session:
            
            user = await session.get(User, user_id)
            
            if not user:
                in_bd = False
                user = User(user_id=user_id,
                            username=username,
                            fullname=fullname)

                session.add(user)
                await session.commit()
            else:
                in_bd = True
                logger.info('Пользователь уже находится в базе данных!')
            
        return (user, in_bd)

    @classmethod
    async def add_mem(cls, mem_name: str, user_id: int) -> None:
        async with cls.__async_session() as session:
            mem = Mem(mem_name=mem_name,
                      user_id=user_id)
            
            session.add(mem)
            await session.commit()

    @classmethod
    async def get_mem(cls, mem_id: int) -> Mem:
        async with cls.__async_session() as session:
            mem = await session.get(Mem, mem_id)
            user = await mem.awaitable_attrs.user
            return mem





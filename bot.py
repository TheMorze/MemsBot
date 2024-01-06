import asyncio
from loguru import logger
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage, Redis

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.handlers import user_handlers
from config import load_config


async def main() -> None:
    config = load_config()
    
    engine = create_engine(url='sqlite+pysqlite:///database.db', echo=True)
    session = Session(engine)
    
    bot = Bot(config.tg_bot.token, parse_mode='HTML')
    redis = Redis(host='localhost')
    dp = Dispatcher(redis=redis)
    dp.include_router(user_handlers.router)
    
    logger.info('Bot was successfully started!')
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    
if __name__ == '__main__':
    asyncio.run(main())
    
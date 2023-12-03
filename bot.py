import asyncio
from loguru import logger
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage, Redis

from handlers import user_handlers
from config_data.config import load_config

async def main() -> None:
    config = load_config()
    
    bot = Bot(config.tg_bot.token, parse_mode='HTML')
    redis = Redis(host='localhost')
    dp = Dispatcher(redis=redis)
    dp.include_router(user_handlers.router)
    
    logger.info('Bot was successfully started!')
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    
if __name__ == '__main__':
    asyncio.run(main())
    

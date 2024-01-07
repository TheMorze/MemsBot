from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart

from app.lexicon.bot_lexicon import LEXICON_RU
from app.keyboards.reply_keyboards import get_menu_keyboard
from app.database.requests import Database

router: Router = Router()

@router.message(CommandStart())
async def process_start_cmd(message: Message):
    
    user, in_bd = await Database.add_user(user_id=message.from_user.id,
                      username=message.from_user.username,
                      fullname=message.from_user.full_name)
    
    # Если пользователь зашёл в бота впервые
    if not in_bd:
        await message.answer(text=LEXICON_RU['greeting_1'].format(name=message.from_user.first_name),
                             reply_markup=get_menu_keyboard())
    # Если уже находится в базе данных
    else:
        await message.answer(text=LEXICON_RU['greeting_2'].format(name=message.from_user.first_name),
                             reply_markup=get_menu_keyboard())
    
@router.message(F.text.lower() == 'загрузить мем')
async def process_load_mem(message: Message):
    await Database.add_mem(mem_name='MEMAS',
                     user_id=message.from_user.id)
    
    await message.answer(text='Добавлен!')

@router.message(F.text.lower() == 'быстрый мем')
async def process_get_mem(message: Message):
    mem = await Database.get_mem(1)
    
    await message.answer(text=str(mem))

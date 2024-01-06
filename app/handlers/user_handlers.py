from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart

from keyboards.reply_keyboards import get_menu_keyboard
from database.models import UserModel

router: Router = Router()

@router.message(CommandStart())
async def process_start_cmd(message: Message):
    user = UserModel(id=message.from_user.id,
                     username=message.from_user.username)
    await message.answer(text='Hello!', reply_markup=get_menu_keyboard())
    
@router.message(F.text.lower() == 'получить мем')
async def process_get_mem(message: Message):
    pass

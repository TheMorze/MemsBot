from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from keyboards.reply_keyboards import get_menu_keyboard

router: Router = Router()

@router.message(CommandStart())
async def process_start_cmd(message: Message):
    await message.answer(text='Hello!', reply_markup=get_menu_keyboard())
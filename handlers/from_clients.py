from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from sqlalchemy.ext.asyncio import AsyncSession

from db import User

from keyboards.shop_keyboards import main_menu_ikb
from content import *


router = Router()
router.message.filter(F.chat.type == "private")


@router.message(CommandStart())
async def start_cmd(message: Message, session: AsyncSession):
    await session.merge(User(user_id=message.from_user.id))
    await session.commit()

    await message.reply("Привет! Это бот онлайн магазин.")


@router.message()
async def message_handler(message: Message):
    image = FSInputFile('static/images/oblojka.png')
    await message.answer_photo(photo=image, caption="Главное меню",
                               reply_markup=main_menu_ikb())

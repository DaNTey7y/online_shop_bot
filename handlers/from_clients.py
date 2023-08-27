from aiogram import Router, Bot, F
from aiogram.types import Message, PreCheckoutQuery, ContentType
from aiogram.filters import CommandStart
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from db import User, get_user_data

from keyboards.shop_keyboards import main_menu_ikb
from content import *


router = Router()
router.message.filter(F.chat.type == "private")


@router.pre_checkout_query()
async def pre_checkout(pre_checkout_q: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)


@router.message(F.content_type == ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: Message, session: AsyncSession):
    payment_info = message.successful_payment

    user = await get_user_data(session, message.from_user.id)
    new_orders_amount = user.orders_amount + 1

    statement = (
        update(User).
        where(User.user_id == message.from_user.id).
        values(orders_amount=new_orders_amount)
    )

    await session.execute(statement)
    await session.commit()

    await message.answer_photo(
        photo=FOOL_IMAGE,
        caption=f"Платеж на сумму {payment_info.total_amount // 100} "
                f"{payment_info.currency} прошел успешно!\n\n"
                f"Но товар мы вам не дадим..."
    )


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

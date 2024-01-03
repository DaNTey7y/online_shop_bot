from aiogram import Router, Bot, F
from aiogram.types import Message, PreCheckoutQuery, ContentType
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.context import FSMContext

from sqlalchemy.ext.asyncio import AsyncSession

from db import User, Operation
from states import Support

from config_reader import config

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

    product_id = int(payment_info.invoice_payload.split("#")[1])

    await session.merge(Operation(product_id=product_id, user_id=message.from_user.id))
    await session.commit()

    await message.answer_photo(
        photo=FOOL_IMAGE,
        caption=f"Платеж на сумму {payment_info.total_amount // 100} "
                f"{payment_info.currency} прошел успешно!\n\n"
                f"Но товар мы вам не дадим..."
    )


@router.message(StateFilter(Support.waiting_for_question))
async def got_an_appeal(message: Message, bot: Bot, state: FSMContext):
    await state.clear()
    try:
        await bot.send_message(chat_id=config.support_chat, text=f"Для вас новое обращение")
        await message.forward(config.support_chat)
        await message.reply("Ваше обращение передано в чат поддержки. Ждите ответа.\n\n"
                            "Можете продолжить пользоваться ботом.")
    except Exception:
        await message.answer("К сожалению обратиться за помощью сейчас нельзя")


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

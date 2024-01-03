from aiogram import Router, Bot, F
from aiogram.types import CallbackQuery, LabeledPrice
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession

from db import *
from states import Support

from config_reader import config
from keyboards.shop_keyboards import *
from content import *


router = Router()
router.callback_query.filter(F.message.chat.type == "private")


@router.callback_query(StateFilter(Support.waiting_for_question), F.data == "menu")
async def back_from_support(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await back_to_menu(callback=callback)


@router.callback_query(F.data == "menu")
async def back_to_menu(callback: CallbackQuery):
    await callback.message.edit_media(media=OBLOJKA_IMAGE, reply_markup=main_menu_ikb())


@router.callback_query(F.data.in_({"shop", "profile", "faq",
                                  "guarantees", "reviews", "support"}))
async def menu_transition(callback: CallbackQuery, session: AsyncSession, state: FSMContext):
    if callback.data == "shop":
        sections = await get_sections(session)
        await callback.message.edit_media(media=SHOP_IMAGE, reply_markup=make_shop_ikb(sections))
    elif callback.data == "guarantees":
        await callback.message.edit_media(media=GUARANTEES_IMAGE, reply_markup=back_in_menu())
    elif callback.data == "profile":
        orders_amount = await get_user_history(session, callback.from_user.id)
        user = await get_user_data(session, callback.from_user.id)
        await callback.message.edit_media(
            media=show_user_info(user.user_id, len(orders_amount), user.reg_date),
            reply_markup=get_profile_ikb()
        )
    elif callback.data == "faq":
        await callback.message.edit_media(media=FAQ_IMAGE, reply_markup=back_in_menu())
    elif callback.data == "reviews":
        await callback.message.edit_media(media=REVIEWS_DATA, reply_markup=back_in_menu())
    elif callback.data == "support":
        await state.set_state(Support.waiting_for_question)
        await callback.message.edit_media(media=SUPPORT_IMAGE, reply_markup=back_in_menu())


@router.callback_query(F.data.startswith("shop_section"))
async def section_goods(callback: CallbackQuery, session: AsyncSession):
    section_id = int(callback.data.split("#")[1])
    section_info = await get_section_data(session, section_id)
    goods = await get_goods_by_section(session, section_id)
    await callback.message.edit_media(
        media=show_section_info(section_info.section_image_path,
                                section_info.image_caption),
        reply_markup=make_goods_ikb(goods)
    )


@router.callback_query(F.data.startswith("product"))
async def product_page(callback: CallbackQuery, session: AsyncSession, bot: Bot):
    product_id = int(callback.data.split("#")[1])
    product = await get_product(session, product_id)

    if config.payments_token.get_secret_value().split(":")[1] == "TEST":
        await bot.send_message(callback.message.chat.id, "Тестовый платеж")

        photo_url = "https://github.com/DaNTey7y/online_shop_bot/blob/master/static/images/figs.png?raw=true"
        price = LabeledPrice(label=product.name, amount=product.cost*100)

        await bot.send_invoice(
            chat_id=callback.message.chat.id,
            title="Покупка товара",
            description=f"Вы получите: {product.name}",
            provider_token=config.payments_token.get_secret_value(),
            currency="rub",
            photo_url=photo_url,
            is_flexible=False,
            prices=[price],
            payload=f"buying-product#{product.product_id}"
        )

    else:
        info = f"Наименование товара: {product.name}\n" \
               f"Цена: {product.cost}\n\n" \
               f"Вы не хотите его покупать."
        await callback.message.edit_caption(
            caption=info,
            reply_markup=back_in_menu()
        )


@router.callback_query(F.data == "history")
async def show_history(callback: CallbackQuery, session: AsyncSession):
    orders_info = await get_user_history(session, callback.from_user.id)
    rows = []

    for i, order in enumerate(orders_info, 1):
        product_info = await get_product(session, order.product_id)
        row = f"{i}) {product_info.name}, стоимость: {product_info.cost}р, дата: {order.purchase_day}"
        rows.append(row)

    await callback.message.edit_media(media=show_orders_history(rows),
                                      reply_markup=orders_history_ikb())
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


BACK_IN_MENU_BTN = InlineKeyboardButton(text="Назад", callback_data="menu")


def main_menu_ikb():
    builder = InlineKeyboardBuilder()
    shop_button = InlineKeyboardButton(text="Магазин", callback_data="shop")
    profile_button = InlineKeyboardButton(text="Профиль", callback_data="profile")
    faq_button = InlineKeyboardButton(text="FAQ", callback_data="faq")
    guarantees_button = InlineKeyboardButton(text="Гарантии", callback_data="guarantees")
    reviews_button = InlineKeyboardButton(text="Отзывы", callback_data="reviews")
    support_button = InlineKeyboardButton(text="Поддержка", callback_data="support")
    builder.add(shop_button, profile_button,
                faq_button, guarantees_button,
                reviews_button, support_button)
    builder.adjust(2)
    return builder.as_markup()


def make_shop_ikb(sections):
    builder = InlineKeyboardBuilder()
    for section in sections:
        builder.button(text=section.name, callback_data=f"shop_section#{section.section_id}")
    builder.row(BACK_IN_MENU_BTN)
    return builder.as_markup()


def make_goods_ikb(goods):
    builder = InlineKeyboardBuilder()
    for product in goods:
        builder.button(text=product.name, callback_data=f"product#{product.product_id}")
    builder.adjust(2)
    builder.row(InlineKeyboardButton(text="Назад", callback_data="shop"))
    return builder.as_markup()


def back_in_menu():
    builder = InlineKeyboardBuilder()
    builder.add(BACK_IN_MENU_BTN)
    return builder.as_markup()


def get_profile_ikb():
    builder = InlineKeyboardBuilder()
    builder.button(text="История покупок", callback_data="history")
    builder.add(BACK_IN_MENU_BTN)
    builder.adjust(1)
    return builder.as_markup()

from aiogram.types import InputMediaPhoto, FSInputFile


def show_user_info(user_id, orders, reg_date):
    months = {1: "января", 2: "февраля", 3: "марта",
              4: "апреля", 5: "мая", 6: "июня",
              7: "июля", 8: "августа", 9: "сентября",
              10: "октября", 11: "ноября", 12: "декабря"}

    f_date = f"{reg_date.day} {months[reg_date.month]} {reg_date.year}"

    return InputMediaPhoto(
        media=FSInputFile("static/images/profile.png"),
        caption=f"Ваш ID профиля: {user_id}\n"
                f"Кол-во ваших заказов: {orders}\n"
                f"Дата регистрации: {f_date}"
    )


def show_section_info(img_path, img_caption):
    return InputMediaPhoto(
        media=FSInputFile(img_path),
        caption=img_caption
    )


def show_orders_history(orders_info):
    f_message = "Ваши покупки:\n" + "\n".join(orders_info[::-1])

    return InputMediaPhoto(
        media=FSInputFile("static/images/profile.png"),
        caption=f_message
    )


FOOL_IMAGE = FSInputFile("static/images/fool.png")


OBLOJKA_IMAGE = InputMediaPhoto(
    media=FSInputFile("static/images/oblojka.png"),
    caption="Главное меню"
)

SHOP_IMAGE = InputMediaPhoto(
    media=FSInputFile("static/images/oblojka.png"),
    caption="Выберите категорию"
)

GUARANTEES_IMAGE = InputMediaPhoto(
    media=FSInputFile("static/images/guarantees.png"),
    caption="Вот наши гарантии"
)

SHOP_SECTION_1 = InputMediaPhoto(
    media=FSInputFile("static/images/figs.png"),
    caption="Выберите товар (фигуру)"
)

FAQ_IMAGE = InputMediaPhoto(
    media=FSInputFile("static/images/faq.png"),
    caption='Здесь можно почитать ответы на <a href="'
            'https://telegra.ph/BLya-karochi-voobshchem-sasite-08-09">'
            'Часто Задаваемы Вопросы (FAQ)</a>'
)

REVIEWS_DATA = InputMediaPhoto(
    media=FSInputFile("static/images/pomoyka.png"),
    caption='Вот чат с отзывами, писать может кто угодно\n'
            '<a href="https://t.me/+drs2ld7NusI2YzYy">Чат с отзывами</a>'
)

SHOP_SECTION_2 = InputMediaPhoto(
    media=FSInputFile("static/images/oh.jpg")
)

SUPPORT_IMAGE = InputMediaPhoto(
    media=FSInputFile("static/images/support.png"),
    caption='Задайте свой вопрос модератору и получите на него ответ'
)
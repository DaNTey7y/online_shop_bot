from aiogram.types import InputMediaPhoto, FSInputFile


def show_user_info(user_id, orders, reg_date):
    return InputMediaPhoto(
        media=FSInputFile("static/images/profile.png"),
        caption=f"Ваш ID профиля: {user_id}\n"
                f"Кол-во ваших заказов: {orders}\n"
                f"Дата регистрации: {reg_date}"
    )


def show_section_info(img_path, img_caption):
    return InputMediaPhoto(
        media=FSInputFile(img_path),
        caption=img_caption
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

from aiogram import Bot, Router, F
from aiogram.types import Message, User

from config_reader import config


router = Router()
router.message.filter(F.chat.id == config.support_chat,
                      F.chat.type.in_({'group', 'supergroup'}))


@router.message()
async def answer_to_appeal(message: Message, bot: Bot):
    if message.reply_to_message.__class__ is Message:
        if message.reply_to_message.from_user.is_bot:
            if message.reply_to_message.forward_from.__class__ is User:
                user_id = message.reply_to_message.forward_from.id
                notification = await bot.send_message(chat_id=user_id,
                                                      text="На ваше недавнее обращение "
                                                           "поступил ответ от модератора")
                await message.copy_to(chat_id=user_id, reply_to_message_id=notification.message_id)

from aiogram import Bot, Router, F
from aiogram.types import Message

from config_reader import config


router = Router()
router.message.filter(F.chat.id == config.support_chat,
                      F.chat.type.in_({'group', 'supergroup'}))


@router.message(F.reply_to_message)
async def answer_to_appeal(message: Message, bot: Bot):
    user_id = message.reply_to_message.forward_from.id
    await bot.send_message(chat_id=user_id, text="На ваше недавнее обращение поступил ответ от модератора")
    await message.copy_to(chat_id=user_id)

import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.utils.callback_answer import CallbackAnswerMiddleware

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from config_reader import config
from middlewares import DbSessionMiddleware
from handlers import from_clients, callbacks, from_mods
from db import Base


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )

    # Подключение БД
    engine = create_async_engine(url=str(config.db_url), echo=False)
    session_maker = async_sessionmaker(engine, expire_on_commit=False)

    # Создаем модели
    async with engine.begin() as con:
        await con.run_sync(Base.metadata.create_all)

    bot = Bot(token=config.bot_token.get_secret_value(), parse_mode="HTML")

    dp = Dispatcher(storage=MemoryStorage())
    dp.update.middleware(DbSessionMiddleware(session_pool=session_maker))
    dp.callback_query.middleware(CallbackAnswerMiddleware())

    # Подключение роутеров
    dp.include_router(from_clients.router)
    dp.include_router(from_mods.router)
    dp.include_router(callbacks.router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

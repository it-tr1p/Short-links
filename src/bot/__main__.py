from aiogram import Dispatcher, Bot
from src.configuration import conf
import asyncio
import logging
from logic import register_user_commands
from src.db.engine import build_async_engine, get_session_maker


async def main() -> None:
    logging.basicConfig(level=logging.DEBUG)

    dp = Dispatcher()
    bot = Bot(token=conf.bot.token, parse_mode="HTML")

    register_user_commands(dp)

    postgres_url = conf.db.build_connection_url()
    async_engine = build_async_engine(url=postgres_url)
    session_maker = get_session_maker(engine=async_engine)

    await dp.start_polling(bot, session_maker=session_maker)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Bot stopped")

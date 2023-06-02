__all__ = ["start", "register_user_commands"]

from aiogram import F
from aiogram import Router
from aiogram.filters import CommandStart, Command
from src.bot.logic.start import start
from src.bot.utils import GetLink
from .callbacks import short_link_callback, short_link_func


def register_user_commands(router: Router) -> None:
    # Register commands
    router.message.register(start, CommandStart())

    # Register callbacks
    router.callback_query.register(short_link_callback, F.data == "short")

    # Register states
    router.message.register(short_link_func, GetLink.get_link)

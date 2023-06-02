from aiogram import types, Bot
from aiogram.fsm.context import FSMContext
from src.bot.utils import GetLink
import pyshorteners as ps


async def short_link_callback(call: types.CallbackQuery, state: FSMContext):
    await state.set_state(GetLink.get_link)
    await call.message.answer(text="<b>Вставьте ссылку</b>")


async def short_link_func(message: types.Message, state: FSMContext):
    await state.clear()
    short = ps.Shortener()
    link_shorted = short.tinyurl.short(message.text)
    await message.answer(text=link_shorted)

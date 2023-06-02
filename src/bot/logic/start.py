from aiogram import types
from src.bot.utils import start_keyboard
from aiogram.fsm.context import FSMContext


async def start(message: types.Message, state: FSMContext) -> None:
    await state.clear()
    await message.answer("<b>Выберите ваше действие:</b>", reply_markup=start_keyboard().as_markup())

from aiogram.utils.keyboard import InlineKeyboardBuilder


def start_keyboard() -> InlineKeyboardBuilder:
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="Сократить ссылку", callback_data="short")
    keyboard.button(text="Посмотреть мои ссылки", callback_data="show")
    keyboard.adjust(2)
    return keyboard


def yes_or_no_keyboard() -> InlineKeyboardBuilder:
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="Да", callback_data="yes")
    keyboard.button(text="Нет", callback_data="no")
    keyboard.adjust(2)
    return keyboard

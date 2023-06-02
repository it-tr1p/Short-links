from aiogram.filters.callback_data import CallbackData


class UrlCallbackData(CallbackData, prefix="url"):
    long_url: str
    short_url: str
    title: str
from aiogram import Dispatcher
from .settings import settings_from_callback, settings_from_command

from .settings import color
from states.state import SetColor
from aiogram.types import ContentTypes


def setup(dp: Dispatcher):

    dp.register_message_handler(
        settings_from_command, commands=['settings']
    )

    dp.register_callback_query_handler(
        settings_from_callback,
        lambda c: c.data and c.data.startswith('settings_menu')
    )

    dp.register_callback_query_handler(
        color.join,
        lambda c: c.data and c.data.startswith('color')
    )

    dp.register_message_handler(
        color.handle,
        state=SetColor.input_state,
        content_types=ContentTypes.TEXT
    )
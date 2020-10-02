from aiogram.types import Message, CallbackQuery
from config import STARTING_MESSAGE
from middlewares.userdata import userdata_required
from models.user import User
from keyboards.inline.menu import settings_menu, main_menu


@userdata_required
async def start_from_command(msg: Message, user: User):
    await msg.answer(
        STARTING_MESSAGE,
        reply_markup=main_menu()
    )


@userdata_required
async def start_from_callback(callback_query: CallbackQuery, user: User):
    await callback_query.bot.edit_message_text(
        chat_id=callback_query.from_user.id,
        message_id=callback_query.message.message_id,
        text=STARTING_MESSAGE,
        reply_markup=main_menu()
    )

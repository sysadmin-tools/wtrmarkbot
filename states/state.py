from aiogram.dispatcher.filters.state import State, StatesGroup


class SetWatermark(StatesGroup):
    get_pic = State()
    set_position = State()
    set_textcolor = State()
    set_opacity = State()
    set_font = State()
    # TODO: размер шрифта
    # TODO: какой текст

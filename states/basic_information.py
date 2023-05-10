from telebot.handler_backends import State, StatesGroup

class UserInfoState(StatesGroup):
    name = State()
    telephone_number = State()
    showroom = State()
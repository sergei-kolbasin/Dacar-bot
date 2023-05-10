from telebot import types
import emoji
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Сайт компании
def inline_button_1():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton(text=f'Наш сайт {emoji.emojize(":globe_with_meridians:")}', url='https://dacar.su/'))
    return markup

# Скидки
def inline_button_2():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton(text=f'Скидки и акции {emoji.emojize("🤑")}', url='https://dacar.su/promo/'))
    return markup


# Авто с пробегом
def inline_button_3():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton(text=f'Авто с пробегом 🚗', url='https://dacar.su/catalog/used/'))
    return markup

# Информация по сдаче авто в ТИ
def inline_button_4():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton(text='ЗДЕСЬ', url='https://dacar.su/trade-in/'))
    return markup


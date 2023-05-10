from telebot.custom_filters import StateFilter
from loader import bot
import handlers
from utils.set_bot_commands import set_default_commands

if __name__ == "__main__":
    set_default_commands(bot) # запускаем все программы бота
    bot.add_custom_filter(StateFilter(bot)) # запускаем состояние
    bot.infinity_polling() # бот работает без остановки

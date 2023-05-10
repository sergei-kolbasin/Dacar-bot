from telebot import TeleBot
from telebot.storage import StateMemoryStorage
from config import config

storage = StateMemoryStorage() # глобальная переменная для хранения
bot = TeleBot(token=config.BOT_TOKEN, state_storage=storage) # создается сам бот

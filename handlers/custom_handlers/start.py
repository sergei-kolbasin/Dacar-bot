import emoji
from keyboards.inline import inline_button_1
from main import bot
from config.config import photo_url
from telebot.types import Message

@bot.message_handler(commands=['start'])
def start(message: Message) -> None:
    bot.send_photo(message.chat.id,
                   photo=photo_url,
                   caption=f'Добрый день, уважаемый клиент! {emoji.emojize(":grinning_face:")}'
                            f'\nЯ бот-помощник компании <b>\'Dacar\'</b> {emoji.emojize(":robot:")}'
                            '\nВот что я могу:\n'
                            f'\n/talk - пообщаться с тобой и помочь в решении проблемы 🤝'
                            f'\n/custom_info - создать заявку на обратный звонок ',
                   reply_markup=inline_button_1(),
                     parse_mode="html")
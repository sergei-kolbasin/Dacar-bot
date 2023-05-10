from states.basic_information import UserInfoState
from main import bot
from keyboards.keyboard import kb5
from config.config import telephone_pattern
import re
from telebot.types import Message
from config.config import list_1


@bot.message_handler(commands=['custom_info'])
def info(message: Message) -> None:
    bot.set_state(message.from_user.id, UserInfoState.name, message.chat.id)
    bot.send_message(message.from_user.id, 'Укажите, пожалуйста, Ваше ФИО.')

# ФИО
@bot.message_handler(state=UserInfoState.name)
def get_name(message: Message) -> None:
    if len(message.text.split()) >= 3:
        bot.send_message(message.from_user.id, f'Спасибо за ответ, {message.text}. Теперь укажите Ваш контактный <b>номер телефона</b>\n\n Пример: 89991234567', parse_mode="html")
        bot.set_state(message.from_user.id, UserInfoState.telephone_number, message.chat.id)

        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['name'] = message.text
    else:
        bot.send_message(message.from_user.id, 'Пожалуйста, введите полностью <b>Фамилию, Имя, Отчество</b>\n\nПример : Иванов Иван Иванович', parse_mode="html")

# Номер телефона

@bot.message_handler(state=UserInfoState.telephone_number)
def get_telephone(message: Message) -> None:
    if re.match(telephone_pattern, message.text) is not None:
        bot.send_message(message.from_user.id, f'Спасибо, записал! {message.text}, укажите салон, в который Вы бы хотели обратиться по Вашему вопросу:'
                                               f'\n\n1. Пулковское шоссе, 44к1 (Hyundai) '
                                               f'\n2. Таллинское шоссе, 202Д (Hyundai) '
                                               f'\n3. ул. Кржижановского, 15к2с2 (Kia)'
                                               f'\n4. пр. Богатырский, 14к2 (Kia)'
                                               f'\n5. Таллинское шоссе, 202с3 (Renault)'
                                               f'\n6. ул. Кржижановского, 15к2 (УАЗ)'
                                               f'\n7. Таллинское шоссе, 202 (Mitsubishi)'
                                               f'\n8. ул. Кржижановского, 15к2 (Chery)'
                                               f'\n9. Таллинское шоссе, 202с3 (Geely)'
                                               f'\n10. ул. Кржижановского, 15к2 (Geely)'
                                               f'\n11. Таллинское шоссе, 202 (OMODA)'
                                               f'\n12. пр. Богатырский, 14к2 (Kaiyi)\n\n<b>Напишите только цифру</b>)', reply_markup=kb5(),  parse_mode="html")
        bot.set_state(message.from_user.id, UserInfoState.showroom, message.chat.id)

        with bot.retrieve_data(message.from_user.id, message.chat_id) as data:
            data['telephone_number'] = message.text
    else:
        bot.send_message(message.from_user.id, 'Пожалуйста, введите номер телефона как в примере выше. \n'
                                               'Номер телефона должен:\n1) Начинаться с цифры 8\n2) Иметь 11 цифр\n3) Состоять только из цифр')

# Салон
@bot.message_handler(state=UserInfoState.showroom)
def get_showroom(message: Message) -> None:
    if message.text in list_1:

        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['showroom'] = message.text

        bot.send_message(message.from_user.id, 'Спасибо за информацию! 😁\nС Вами свяжутся в ближайшее время!')
    else:
        bot.send_message(message.from_user.id, 'Укажите цифры из списка салонов от 1 до 12')

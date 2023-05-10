import emoji
from utils.check_pattern import check_pattern, check_str
from keyboards.keyboard import kb, kb1, kb2, kb3, kb4, kb6
from keyboards.inline import inline_button_2, inline_button_3, inline_button_4
from main import bot
from config.config import photo, car_list, help
from telebot.types import Message



@bot.message_handler(content_types=['text'])
def text(message: Message) -> None:
    if message.text == '/talk':
        bot.send_photo(message.chat.id, photo=photo,
                   caption=f'С удовольствием пообщаюсь с Вами 😃'
                            '\nПодскажите по какому вопросу Вы к нам обращаетесь:\n'
                            f'\n{emoji.emojize(":keycap_1:")} Интересует покупка нового автомобиля'
                            f'\n{emoji.emojize(":keycap_2:")} Интересует покупка/продажа поддержанного автомобиля'
                            f'\n{emoji.emojize(":keycap_3:")} Хочу записаться на тест-драйв'
                            f'\n{emoji.emojize(":keycap_4:")} Сервис'
                            f'\n{emoji.emojize(":keycap_5:")} Вопрос по документам\n'
                            '\nВведите цифру на клавиатуре.',
                   reply_markup=kb(),  parse_mode="html")
    elif message.text == '1':
        bot.send_message(message.chat.id, 'Укажите <b>модель</b>, которая вас заинтересовала:\n\n1) С5 2WD\n2) C5 4WD\n3) S5', reply_markup=kb1(),  parse_mode="html")
    elif message.text == '2':
        bot.send_message(message.chat.id, 'Подскажите, Вы бы хотели <b>купить</b> или <b>продать</b> свой автомобиль', reply_markup=kb6(), parse_mode="html")
    elif message.text == 'Купить':
        bot.send_message(message.chat.id, 'Укажите <b>модель</b>, которая вас заинтересовала:'
                                          '\n\n1) KIA\n2) HYUNDAI\n3) AUDI\n4) RENAULT\n5) BMW\n6) LADA\n7) VOLKSWAGEN\n8) OPEL\n9) Другая марка', reply_markup=kb2(), parse_mode="html")
    elif message.text == 'Продать':
        bot.send_message(message.chat.id, 'Чтобы продать свой автомобиль, необходимо подъехать в салон и провести его оценку для определения конечной стоимости Вашего авто.'
                                          '\nБудем ждать Вас в салоне!\nС более подробной информацией Вы можете ознакомиться', reply_markup=inline_button_4())
    elif message.text in car_list:
        bot.send_message(message.chat.id, 'Отлично! У нас есть автомобиль этой марки на складе. Вы можете ознакомиться с более точной информацией, пройдя по ссылке снизу, либо позвонить'
                                          'нашему менеджеру, он Вас сориентирует по всем вопросам\nТелефон для связи: +7 (812) 416-01-67', reply_markup=inline_button_3())
    elif message.text == 'Другая марка':
        bot.send_message(message.chat.id, 'Какой у Вас интересный вкус. Давайте посмотрим что у нас есть на складе', reply_markup=inline_button_3())
    elif message.text == '3':
        bot.send_message(message.chat.id, 'Укажите <b>модель</b> автомобиля, на котором бы хотели пройти тест-драйв:\n\n1) С5\n2) C5 AWD\n3) S5 2WD', reply_markup=kb4(),  parse_mode="html")
    elif message.text == '4':
        bot.send_message(message.chat.id, 'Напишите что с Вашим автомобиль:\n\n1) На сервисе\n2) Хочу записаться\n3) Другое', reply_markup=kb3())
    elif message.text == '5':
        bot.send_message(message.chat.id, 'Опишите Ваш запрос. Начните его со слов <b>"Добрый день!"</b>', parse_mode="html")
    elif message.text == 'C5 2WD' or message.text == 'C5 4WD' or message.text == 'S5':
        bot.send_message(message.chat.id, 'Отличный выбор, проходите по данной ссылке и получите скидку до 200т.р. на данную модель', reply_markup=inline_button_2())
    elif message.text == 'C5' or message.text == 'C5 AWD' or message.text == 'S5 2WD':
        bot.send_message(message.chat.id, 'Пожалуйста, выберите дату и время, когда бы вы хотели записаться на тест-драйв ⏱'
                                          '\n\nФормат: <b>01.01.2023 14:30</b>',  parse_mode="html")
    elif check_pattern(message.text):
        bot.send_message(message.chat.id, f'Отлично, мы записали Вас на тест-драйв на <b>{message.text[:10]} в {message.text[10:]} </b>\n'
                                          f'При себе необходимо будет иметь:\n\n1) Водительское удостоверение\n2) Паспорт\n3) Трезвое состояние 😝\n\n Ждем Вас!  ', parse_mode="html")
    elif message.text == 'Хочу записаться':
        bot.send_message(message.chat.id, 'В данном случае необходимо оставить заявку, чтобы с Вами связался наш сотрудник. Нажмите на /custom_info')
    elif message.text == 'На сервисе':
        bot.send_message(message.chat.id, 'В данном случае необходимо необходимо набрать координатора сервиса по номеру +7 (812) 416-01-67')
    elif message.text == 'Другое':
        bot.send_message(message.chat.id, 'В данном случае необходимо оставить заявку, чтобы с Вами связался наш сотрудник. Нажмите на /custom_info')
    elif message.text == 'Назад':
        bot.send_message(message.chat.id, f'С удовольствием пообщаюсь с Вами 😃'
                               '\nПодскажите по какому вопросу Вы к нам обращаетесь:\n'
                               f'\n{emoji.emojize(":keycap_1:")} Интересует покупка нового автомобиля'
                               f'\n{emoji.emojize(":keycap_2:")} Интересует покупка/продажа поддержанного автомобиля'
                               f'\n{emoji.emojize(":keycap_3:")} Хочу записаться на тест-драйв'
                               f'\n{emoji.emojize(":keycap_4:")} Сервис'
                               f'\n{emoji.emojize(":keycap_5:")} Вопрос по документам\n'
                               '\nВведите цифру на клавиатуре.',
                       reply_markup=kb(), parse_mode="html")
    elif check_str(message.text):
        bot.send_message(message.chat.id, 'Спасибо за ответ!\nЯ отправил Вашу заявку в нужный отдел. С Вами свяжутся в ближайшее время 😉')
    else:
        bot.send_photo(message.chat.id, photo=help,
                       caption='Что-то я Вас не понимаю 🧐, давайте попробуем как указано в примере, либо воспользуемся встроенной клавиатурой, она вот тут-а')

from telebot.types import ReplyKeyboardMarkup, KeyboardButton


# Клавиатура на старт
def kb():
    markup = ReplyKeyboardMarkup()
    markup.row_width = 3
    markup.row_width = 3
    markup.add(KeyboardButton('1'), KeyboardButton('2'), KeyboardButton('3'),
               KeyboardButton('4'), KeyboardButton('5'), KeyboardButton('Назад'))
    return markup


# Выбор нового авто
def kb1():
    markup = ReplyKeyboardMarkup()
    markup.row_width = 2
    markup.row_width = 2
    markup.add(KeyboardButton('C5 2WD'), KeyboardButton('C5 4WD'),
               KeyboardButton("S5"), KeyboardButton('Назад'))
    return markup


# Выбор б/у авто
def kb2():
    markup = ReplyKeyboardMarkup()
    markup.row_width = 3
    markup.row_width = 3
    markup.row_width = 3
    markup.row_width = 1
    markup.add(KeyboardButton('KIA'), KeyboardButton('HYUNDAI'), KeyboardButton('AUDI'),
               KeyboardButton('RENAULT'), KeyboardButton('BMW'), KeyboardButton('LADA'),
               KeyboardButton('VOLKSWAGEN'), KeyboardButton('OPEL'), KeyboardButton('Другое'),
               KeyboardButton('Назад'))
    return markup


# Сервис
def kb3():
    markup = ReplyKeyboardMarkup()
    markup.row_width = 2
    markup.row_width = 2
    markup.add(KeyboardButton('На сервисе'), KeyboardButton('Хочу записаться'),
               KeyboardButton("Другое"), KeyboardButton('Назад'))
    return markup


# Тест-драйв
def kb4():
    markup = ReplyKeyboardMarkup()
    markup.row_width = 2
    markup.row_width = 2
    markup.add(KeyboardButton('C5'), KeyboardButton('C5 AWD'),
               KeyboardButton("S5 2WD"), KeyboardButton('Назад'))
    return markup

# Выбор салона
def kb5():
    markup = ReplyKeyboardMarkup()
    markup.row_width = 4
    markup.row_width = 4
    markup.row_width = 4
    markup.add(KeyboardButton('1'), KeyboardButton('2'), KeyboardButton('3'),
               KeyboardButton('4'), KeyboardButton('5'), KeyboardButton('6'),
               KeyboardButton('7'), KeyboardButton('8'), KeyboardButton('9'),
               KeyboardButton('10'), KeyboardButton('11'), KeyboardButton('12'))
    return markup


# Выбор куда в отдел ТИ
def kb6():
    markup = ReplyKeyboardMarkup()
    markup.row_width = 2
    markup.add(KeyboardButton('Купить'), KeyboardButton('Продать'))
    return markup
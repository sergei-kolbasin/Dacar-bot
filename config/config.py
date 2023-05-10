import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()


BOT_TOKEN = os.getenv("TOKEN")
telephone_pattern = '8\d{10}'
photo_url = 'https://procontext.ru/assets/images/recommend/logos/dacar.jpg'
photo = open('f.png', 'rb')
car_list = ['KIA,' 'HYUNDAI', 'AUDI', 'RENAULT', 'BMW', 'LADA', 'VOLKSWAGEN', 'OPEL']
help = 'https://infostart.ru/upload/iblock/525/52543df0c79ebcb5b11919c504885d01.png'
list_1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']

DEFAULT_COMMANDS = (
    ("start", "Запустить бота"),
    ("custom_info", "Отправить информацию о себе"),
    ("talk", "Поговорить")
)

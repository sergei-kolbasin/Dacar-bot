import re
from typing import Any

# Функция проверяет правильность написания формата даты и времени записи на тест-драйв
def check_pattern(data: str) -> Any:
    data_pattern = '\d\d.\d\d.\d{4} \d\d:\d\d'
    check = re.fullmatch(data_pattern, data)
    if check:
        return True

# Функция проверяет правильность написания заявки
def check_str(data: str) -> Any:
    start_str = 'Добрый день!'
    if data.startswith(start_str):
        return True
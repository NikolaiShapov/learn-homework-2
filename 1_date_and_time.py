"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import datetime, timedelta

def print_days():
    data_today1 = datetime.now() # сегодня
    data_today2 = datetime.today() # сегодня
    # datetime.now() datetime.today() в чем принципиальная разница и какой метод в каких случаях применяется?

    yesterday = data_today1 - timedelta(days = 1) # вчера
    ago_30_days  = data_today1 - timedelta(days = 30) # 30 дней назад

    print(f'сегодня_1: {data_today1}')
    print(f'сегодня_2: {data_today2}')
    print(f'вчера: {yesterday}')
    print(f'30 дней назад: {ago_30_days}')


def str_2_datetime(date_string):
    print(datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f'))
    object_datetime_data = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
    print(type(object_datetime_data))

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))

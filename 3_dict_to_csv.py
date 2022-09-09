"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору.
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv

base_user = [{'name': 'Маша', 'age': 25, 'job': 'Scientist'},
            {'name': 'Вася', 'age': 8, 'job': 'Programmer'},
            {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
            {'name': 'Оля', 'age': 41, 'job': 'Doctor'},
            ]

def main():
    with open('export.csv', 'w', encoding='utf-8', newline='') as f:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(f, fields, delimiter=';')
        writer.writeheader()
        for user in base_user:
            writer.writerow(user)
        print('Файл export.csv сохранен, проверяй ;)!')


if __name__ == "__main__":
    main()

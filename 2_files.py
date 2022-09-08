"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main():
    with open('referat.txt', 'r', encoding= 'utf_8') as f:
        dump_text = f.read()
        len_dump_text = len(dump_text)
        print(f'длина получившейся строки(файла): {len_dump_text}')

        word_count = len(dump_text.split())
        print(f'количество слов в тексте: {word_count}')

    with open('referat.txt', 'r', encoding= 'utf_8') as f:
        for line in f:
            line = line.replace('.','!')
            with open ('referat2.txt', 'a', encoding= 'utf_8') as file:
                file.write(line)
        print('Файл referat2.txt сохранен, проверяй ;)!')

if __name__ == "__main__":
    main()

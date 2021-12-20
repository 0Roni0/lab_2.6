#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    # Список людей.
    fellows = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные о человеке.
            name = input("Фамилия и инициалы? ")
            number = input("Номер телефона? ")
            birthday = list(map(int, input("Дата рождения? ").split()))
            # Создать словарь.
            fellow = {
                'name': name,
                'number': number,
                'birthday': birthday,
            }
            # Добавить словарь в список.
            fellows.append(fellow)
            # Отсортировать список в случае необходимости.
            if len(fellows) > 1:
                fellows.sort(key=lambda x: x.get('birthday')[::-1])

        elif command == 'list':
            # Заголовок таблицы.
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 15
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^15} |'.format(
                    "№",
                    "Ф.И.О.",
                    "Номер телефона",
                    "Дата рождения"
                )
            )
            print(line)

            # Вывести данные о всех людях.
            for idx, fellow in enumerate(fellows, 1):
                print(
                    '| {:>4} | {:<30} | {:<20} | {:>15} |'.format(
                        idx,
                        fellow['name'],
                        fellow['number'],
                        # переводим дату рождения в строку
                        ' '.join((str(i) for i in fellow['birthday']))
                    )
                )
            print(line)
        elif command == 'whois':
            who = input('Кого ищем?: ')
            print(name)
            print(number)
            print(birthday)
        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить работника;")
            print("list - вывести список работников;")
            print("whois - вывести нужного работника;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print('Неизвестная команда', command, file=sys.stderr)

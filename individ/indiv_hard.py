#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import sys
from distutils import command
import jsonschema
from jsonschema import validators

def get_reys(reys):
    """
    Запросить данные о рейсе.
    """
    pynkt = input("Пункта назначения рейса: ")
    numb = int(input("Номер рейса: "))
    samolet = input("Тип самолета: ")

    # Создать словарь.
    rey = {
        'pynkt': pynkt,
        'numb': numb,
        'samolet': samolet,
    }

    # Добавить словарь в список.
    reys.append(rey)

    # Отсортировать список в случае необходимости.
    if len(reys) > 1:
        reys.sort(key=lambda item: item.get('numb', ''))
    return reys


def display_reys(re):
    """
    Отобразить список рейсов.
    """
    # Проверить, что список работников не пуст.
    if re:
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,

            '-' * 8
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
                "No",
                "Пункт назначения",
                "Номер рейса",
                "Тип"
            )
        )
        print(line)

        # Вывести данные о всех рейсах.
        for idx, rey in enumerate(re, 1):
            print(
                '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
                    idx,
                    rey.get('pynkt', ''),
                    rey.get('numb', ''),
                    rey.get('samolet', 0)
                )
            )
            print(line)

    else:
        print("Список рейсов пуст.")


def select_reys(re, pynkt_pr):
    """
    Выбрать рейс с нужным пунктом.
    """
    # Сформировать список работников.
    result = []
    for employee in re:
        if employee.get('pynkt') == pynkt_pr:
            result.append(employee)
        else:
            print("Нет рейсов в указаный пункт")

    # Возвратить список выбранных работников.
    return result


def save_reys(file_name, staff):
    """
    Сохранить все рейсы в файл JSON.
    """
    # Открыть файл с заданным именем для записи.
    with open(file_name, "w", encoding="utf-8") as fout:
        # Выполнить сериализацию данных в формат JSON.
        # Для поддержки кирилицы установим ensure_ascii=False
        json.dump(staff, fout, ensure_ascii=False, indent=4)


def load_reys(file_name):
    """
    Загрузить всех работников из файла JSON.
    """
    # Открыть файл с заданным именем для чтения.
    with open(file_name, "r", encoding="utf-8") as fin:
        return json.load(fin)


def main():
    """
    Главная функция программы.
    """
    #Список рейсов
    reys = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            reys = get_reys(reys)

        elif command == 'list':
            display_reys(reys)

        elif command.startswith('select '):
            # Разбить команду на части.
            parts = command.split(' ', maxsplit=1)
            # Получить требуемый город.
            pynkt_pr = str(parts[1])

            selected = select_reys(reys, pynkt_pr)
            display_reys(selected)

        elif command.startswith("save "):
            # Разбить команду на части для выделения имени файла.
            parts = command.split(maxsplit=1)
            # Получить имя файла.
            file_name = parts[1]

            # Сохранить данные в файл с заданным именем.
            save_reys(file_name, reys)

        elif command.startswith("load "):
            # Разбить команду на части для выделения имени файла.
            parts = command.split(maxsplit=1)
            # Получить имя файла.
            file_name = parts[1]

            # Сохранить данные в файл с заданным именем.
            reys = load_reys(file_name)

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить работника;")
            print("list - вывести список работников;")
            print("select <стаж> - запросить работников со стажем;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")


if __name__ == '__main__':
    main()

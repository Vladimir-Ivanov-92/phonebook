from .menu_service import (get_data_from_many_condition_menu,
                           get_data_from_one_condition_menu,
                           get_data_from_update_menu)
from .menu_text import (many_condition_menu, one_condition_menu,
                        search_menu)
from service.phonebook_entry import PhonebookEntry
from service.search_entry import SearchEntry


def handle_search_menu(search_entry: SearchEntry) -> None:
    """Обработчик меню поиска"""

    while True:
        user_input = search_menu()

        if user_input == "0":
            break
        elif user_input == "1":
            try:
                index = int(input("Введите номер строки: "))
                search_entry.index_search(index - 1)
            except ValueError:
                print("Введите цифру соответствующую порядковому номеру записи!")

        elif user_input == "2":
            column, data = get_data_from_one_condition_menu(one_condition_menu())
            search_entry.condition_search(column, data)
        elif user_input == "3":
            handle_conditions_search(search_entry)


def handle_conditions_search(search_entry: SearchEntry) -> None:
    """Обработчик меню поиска по нескольким условиям"""

    conditions = []
    while True:
        user_input = many_condition_menu()

        if user_input == "0":
            break
        elif user_input == "7":
            search_entry.conditions_search(conditions)
            break
        else:
            column, data = get_data_from_many_condition_menu(
                user_input)
            conditions.append((column, data))


def handle_edit_menu(phonebook_entry: PhonebookEntry,
                     search_entry: SearchEntry) -> None:
    """Обработчик меню добавления записи"""

    while True:
        user_input = search_menu()

        if user_input == "0":
            break
        elif user_input == "1":
            index = int(input("Введите номер строки: "))
            result_search = search_entry.index_search(index - 1)
            try:
                column, data = get_data_from_update_menu()
                phonebook_entry.edit_entry(result_search, (column, data))
            except Exception:
                pass
        elif user_input == "2":
            number_one_condition_menu = one_condition_menu()
            try:
                column, data = get_data_from_one_condition_menu(
                    number_one_condition_menu)
                result_search = search_entry.condition_search(column, data)
                if len(result_search) > 1:
                    print()
                    print("Выбрано более одного значения. Воспользуйтесь поиском с "
                          "несколькими условиями, чтоб выбрать одно значение!")
                else:
                    column, data = get_data_from_update_menu()
                    phonebook_entry.edit_entry(result_search, (column, data))
            except Exception:
                pass
        elif user_input == "3":
            handle_conditions_edit(phonebook_entry, search_entry)


def handle_conditions_edit(phonebook_entry: PhonebookEntry,
                           search_entry: SearchEntry) -> None:
    """Обработчик меню выбора нескольких условий"""

    conditions = []
    while True:
        number_many_condition_menu = many_condition_menu()

        if number_many_condition_menu == "0":
            break
        elif number_many_condition_menu == "7":
            result_search = search_entry.conditions_search(conditions)
            if len(result_search) > 1:
                print()
                print("Выбрано более одного значения. Воспользуйтесь поиском с "
                      "дополнительными условиями, чтоб выбрать одно значение!")
            else:
                column, data = get_data_from_update_menu()
                phonebook_entry.edit_entry(result_search, (column, data))
                break
        else:
            column, data = get_data_from_many_condition_menu(
                number_many_condition_menu)
            conditions.append((column, data))

import config
from phonebook.main_menu_handlers.add_new_row import add_new_row
from phonebook.main_menu_handlers.display_all_phone_book import \
    display_directory_entries_on_the_screen_with_paginate
from phonebook.main_menu_handlers.find_a_record import FindRecord
from phonebook.main_menu_handlers.record_editing import PhonebookEntry


def main_menu():
    print("Главное меню:")
    print("1 - Вывести весь справочник")
    print("2 - Добавить новую запись в справочник")
    print("3 - Найти запись в справочнике")
    print("4 - Редактировать запись в справочнике")
    print("0 - Завершить программу")

    user_input_main = input("Укажите номер выбранного варианта: ")
    return user_input_main


def search_menu():
    print("Меню поиска:")
    print("1 - Поиск по номеру записи")
    print("2 - Поиск по одному условию")
    print("3 - Поиск по нескольким условиям")
    print("0 - Назад")

    user_input_search = input("Укажите номер выбранного варианта: ")
    return user_input_search


def one_condition_menu():
    print("Выберите условие:")
    print("1 - Фамилия")
    print("2 - Имя")
    print("3 - Отчество")
    print("4 - Название организации:")
    print("5 - Телефон (рабочий):")
    print("6 - Телефон личный (сотовый):")
    print("7 - Поиск")
    print("0 - Завершить")

    user_input_search = input("Укажите номер выбранного варианта: ")
    return user_input_search


def many_condition_menu():
    print("Выберите условие:")
    print("1 - Фамилия")
    print("2 - Имя")
    print("3 - Отчество")
    print("4 - Название организации:")
    print("5 - Телефон (рабочий):")
    print("6 - Телефон личный (сотовый):")
    print("7 - Поиск")
    print("0 - Назад")

    user_input_search = input("Укажите номер выбранного варианта: ")
    return user_input_search


def update_menu():
    print("Выберите условие:")
    print("1 - Фамилия")
    print("2 - Имя")
    print("3 - Отчество")
    print("4 - Название организации:")
    print("5 - Телефон (рабочий):")
    print("6 - Телефон личный (сотовый):")
    print("0 - Назад")

    user_input_search = input("Укажите номер выбранного варианта: ")
    return user_input_search

def main():
    FLAG_MAIN = True

    while FLAG_MAIN:
        user_input = main_menu()
        # TODO pattern matching
        if user_input == "0":
            print("Работа программы завершена!")
            FLAG_MAIN = False
        elif user_input == "1":
            display_directory_entries_on_the_screen_with_paginate(config.PAGINATE)
        elif user_input == "2":
            add_new_row(config.TABLE_NAME)
        elif user_input == "3":

            FLAG_SEARCH = True
            FLAG_CONDITION = True

            while FLAG_SEARCH:
                number_search_menu = search_menu()
                find_record = FindRecord(config.TABLE_NAME)
                if number_search_menu == "0":
                    FLAG_SEARCH = False
                elif number_search_menu == "1":
                    index = int(input("Введите номер строки: "))
                    find_record.index_search(index - 1)
                elif number_search_menu == "2":

                    number_one_condition_menu = one_condition_menu()
                    if number_one_condition_menu == "1":
                        data = input("Введите фамилию: ")
                        find_record.condition_search("Фамилия", data)
                    elif number_one_condition_menu == "2":
                        data = input("Введите имя: ")
                        find_record.condition_search("Имя", data)
                    elif number_one_condition_menu == "3":
                        data = input("Введите отчество: ")
                        find_record.condition_search("Отчество", data)
                    elif number_one_condition_menu == "4":
                        data = input("Название организации: ")
                        find_record.condition_search("Название организации", data)
                    elif number_one_condition_menu == "5":
                        data = input("Телефон (рабочий): ")
                        find_record.condition_search("Телефон (рабочий)", data)
                    elif number_one_condition_menu == "6":
                        data = input("Телефон личный (сотовый): ")
                        find_record.condition_search("Телефон личный (сотовый)", data)



                elif number_search_menu == "3":

                    conditions = []
                    while FLAG_CONDITION:
                        number_many_condition_menu = many_condition_menu()
                        if number_many_condition_menu == "0":
                            FLAG_CONDITION = False
                        elif number_many_condition_menu == "1":
                            data = input("Введите фамилию: ")
                            conditions.append(("Фамилия", data))
                        elif number_many_condition_menu == "2":
                            data = input("Введите имя: ")
                            conditions.append(("Имя", data))
                        elif number_many_condition_menu == "3":
                            data = input("Введите отчество: ")
                            conditions.append(("Отчество", data))
                        elif number_many_condition_menu == "4":
                            data = input("Название организации: ")
                            conditions.append(("Название организации", data))
                        elif number_many_condition_menu == "5":
                            data = input("Телефон (рабочий): ")
                            conditions.append(("Телефон (рабочий)", data))
                        elif number_many_condition_menu == "6":
                            data = input("Телефон личный (сотовый): ")
                            conditions.append(("Телефон личный (сотовый)", data))
                        elif number_many_condition_menu == "7":  # TODO! IndexError: list index out of range
                            find_record.conditions_search(conditions)
                            conditions = []

        elif user_input == "4":
            FLAG_SEARCH = True
            FLAG_CONDITION = True

            while FLAG_SEARCH:
                number_search_menu = search_menu()
                find_record = FindRecord(config.TABLE_NAME)
                phonebook_entry = PhonebookEntry(config.TABLE_NAME)
                if number_search_menu == "0":
                    FLAG_SEARCH = False
                elif number_search_menu == "1":
                        index = int(input("Введите номер строки: "))
                        result_search = find_record.index_search(index - 1)
                        number_update_menu = update_menu()
                        if number_update_menu == "0":
                            pass
                        if number_update_menu == "1":
                            data = input("Введите фамилию: ")
                            phonebook_entry.edit_entry(result_search, ("Фамилия", data))
                        elif number_update_menu == "2":
                            data = input("Введите имя: ")
                            phonebook_entry.edit_entry(result_search, ("Имя", data))
                        elif number_update_menu == "3":
                            data = input("Введите отчество: ")
                            phonebook_entry.edit_entry(result_search, ("Отчество", data))
                        elif number_update_menu == "4":
                            data = input("Название организации: ")
                            phonebook_entry.edit_entry(result_search, ("Название организации", data))
                        elif number_update_menu == "5":
                            data = input("Телефон (рабочий): ")
                            phonebook_entry.edit_entry(result_search, ("Телефон (рабочий)", data))
                        elif number_update_menu == "6":
                            data = input("Телефон личный (сотовый): ")
                            phonebook_entry.edit_entry(result_search, ("Телефон личный (сотовый)", data))

                elif number_search_menu == "2":

                    number_one_condition_menu = one_condition_menu()
                    if number_one_condition_menu == "1":
                        data = input("Введите фамилию: ")
                        find_record.condition_search("Фамилия", data)
                    elif number_one_condition_menu == "2":
                        data = input("Введите имя: ")
                        find_record.condition_search("Имя", data)
                    elif number_one_condition_menu == "3":
                        data = input("Введите отчество: ")
                        find_record.condition_search("Отчество", data)
                    elif number_one_condition_menu == "4":
                        data = input("Название организации: ")
                        find_record.condition_search("Название организации", data)
                    elif number_one_condition_menu == "5":
                        data = input("Телефон (рабочий): ")
                        find_record.condition_search("Телефон (рабочий)", data)
                    elif number_one_condition_menu == "6":
                        data = input("Телефон личный (сотовый): ")
                        find_record.condition_search("Телефон личный (сотовый)", data)



                elif number_search_menu == "3":

                    conditions = []
                    while FLAG_CONDITION:
                        number_many_condition_menu = many_condition_menu()
                        if number_many_condition_menu == "0":
                            FLAG_CONDITION = False
                        elif number_many_condition_menu == "1":
                            data = input("Введите фамилию: ")
                            conditions.append(("Фамилия", data))
                        elif number_many_condition_menu == "2":
                            data = input("Введите имя: ")
                            conditions.append(("Имя", data))
                        elif number_many_condition_menu == "3":
                            data = input("Введите отчество: ")
                            conditions.append(("Отчество", data))
                        elif number_many_condition_menu == "4":
                            data = input("Название организации: ")
                            conditions.append(("Название организации", data))
                        elif number_many_condition_menu == "5":
                            data = input("Телефон (рабочий): ")
                            conditions.append(("Телефон (рабочий)", data))
                        elif number_many_condition_menu == "6":
                            data = input("Телефон личный (сотовый): ")
                            conditions.append(("Телефон личный (сотовый)", data))
                        elif number_many_condition_menu == "7":  # TODO! IndexError: list index out of range
                            find_record.conditions_search(conditions)
                            conditions = []
            # record_editing(config.TABLE_NAME)


if __name__ == '__main__':
    main()

    # index_search(config.TABLE_NAME, 0)

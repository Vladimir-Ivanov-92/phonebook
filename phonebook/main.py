import config
from phonebook.handlers.add_new_row import add_new_row
from phonebook.handlers.display_all_phone_book import \
    display_directory_entries_on_the_screen_with_paginate
from phonebook.handlers.find_a_record import FindRecord
from phonebook.handlers.record_editing import PhonebookEntry
from phonebook.menu.menu_service import get_data_from_update_menu, \
    get_data_from_one_condition_menu, get_data_from_many_condition_menu
from phonebook.menu.menu_text import main_menu, search_menu, one_condition_menu, \
    many_condition_menu


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
                    column, data = get_data_from_one_condition_menu(
                        number_one_condition_menu)
                    find_record.condition_search(column, data)

                elif number_search_menu == "3":
                    FLAG_CONDITION = True
                    conditions = []
                    while FLAG_CONDITION:
                        number_many_condition_menu = many_condition_menu()
                        if number_many_condition_menu == "0":
                            FLAG_CONDITION = False
                        elif number_many_condition_menu == "7":
                            find_record.conditions_search(conditions)
                            conditions = []
                            FLAG_CONDITION = False
                        else:
                            column, data = get_data_from_many_condition_menu(
                                number_many_condition_menu)
                            conditions.append((column, data))

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
                    try:
                        column, data = get_data_from_update_menu()
                        phonebook_entry.edit_entry(result_search, (column, data))
                    except:
                        FLAG_SEARCH = False
                elif number_search_menu == "2":
                    number_one_condition_menu = one_condition_menu()
                    try:
                        column, data = get_data_from_one_condition_menu(
                            number_one_condition_menu)
                        result_search = find_record.condition_search(column, data)
                        column, data = get_data_from_update_menu()
                        phonebook_entry.edit_entry(result_search, (column, data))
                    except:
                        FLAG_SEARCH = False

                elif number_search_menu == "3":
                    conditions = []
                    while FLAG_CONDITION:
                        number_many_condition_menu = many_condition_menu()
                        if number_many_condition_menu == "0":
                            FLAG_CONDITION = False
                        elif number_many_condition_menu == "7":  # TODO! IndexError: list index out of range
                            result_search = find_record.conditions_search(conditions)
                            column, data = get_data_from_update_menu()
                            phonebook_entry.edit_entry(result_search, (column, data))
                            conditions = []
                        else:
                            column, data = get_data_from_many_condition_menu(
                                number_many_condition_menu)
                            conditions.append((column, data))


if __name__ == '__main__':
    main()

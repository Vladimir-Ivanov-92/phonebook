import config

from menu.handlers_menu import handle_edit_menu, handle_search_menu
from menu.menu_text import main_menu
from service.phonebook_entry import PhonebookEntry
from service.search_entry import SearchEntry


def main() -> None:
    """Запуск программы, создание главного меню"""
    phonebook_entry = PhonebookEntry(config.TABLE_NAME, config.PAGINATE)
    search_entry = SearchEntry(config.TABLE_NAME)

    while True:
        user_input = main_menu()

        if user_input == "0":
            print("Работа программы завершена!")
            break
        elif user_input == "1":
            phonebook_entry.view_all_entries_paginated()
        elif user_input == "2":
            phonebook_entry.add_new_row()
        elif user_input == "3":
            handle_search_menu(search_entry)
        elif user_input == "4":
            handle_edit_menu(phonebook_entry, search_entry)


if __name__ == '__main__':
    main()

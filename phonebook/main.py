import config
from phonebook.menu.handlers_menu import handle_search_menu, handle_edit_menu
from phonebook.service.search_entry import SearchEntry
from phonebook.service.phonebook_entry import PhonebookEntry

from phonebook.menu.menu_text import main_menu


def main() -> None:
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

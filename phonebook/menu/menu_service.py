from typing import Optional

from .menu_text import update_menu


def get_data_from_update_menu() -> Optional[tuple[str, str | int]]:
    number_update_menu = update_menu()
    if number_update_menu == "0":
        return None
    if number_update_menu == "1":
        data = input("Введите фамилию: ")
        return ("Фамилия", data)
    elif number_update_menu == "2":
        data = input("Введите имя: ")
        return ("Имя", data)
    elif number_update_menu == "3":
        data = input("Введите отчество: ")
        return ("Отчество", data)
    elif number_update_menu == "4":
        data = input("Название организации: ")
        return ("Название организации", data)
    elif number_update_menu == "5":
        data = input("Телефон (рабочий): ")
        return ("Телефон (рабочий)", data)
    elif number_update_menu == "6":
        data = input("Телефон личный (сотовый): ")
        return ("Телефон личный (сотовый)", data)


def get_data_from_one_condition_menu(number_one_condition_menu: str) -> Optional[
        tuple[str, str | int]]:
    if number_one_condition_menu == "0":
        return None
    elif number_one_condition_menu == "1":
        data = input("Введите фамилию: ")
        return ("Фамилия", data)
    elif number_one_condition_menu == "2":
        data = input("Введите имя: ")
        return ("Имя", data)
    elif number_one_condition_menu == "3":
        data = input("Введите отчество: ")
        return ("Отчество", data)
    elif number_one_condition_menu == "4":
        data = input("Название организации: ")
        return ("Название организации", data)
    elif number_one_condition_menu == "5":
        data = input("Телефон (рабочий): ")
        return ("Телефон (рабочий)", data)
    elif number_one_condition_menu == "6":
        data = input("Телефон личный (сотовый): ")
        return ("Телефон личный (сотовый)", data)


def get_data_from_many_condition_menu(number_many_condition_menu: str) -> Optional[
        tuple[str, str | int]]:
    if number_many_condition_menu == "1":
        data = input("Введите фамилию: ")
        return ("Фамилия", data)
    elif number_many_condition_menu == "2":
        data = input("Введите имя: ")
        return ("Имя", data)
    elif number_many_condition_menu == "3":
        data = input("Введите отчество: ")
        return ("Отчество", data)
    elif number_many_condition_menu == "4":
        data = input("Название организации: ")
        return ("Название организации", data)
    elif number_many_condition_menu == "5":
        data = input("Телефон (рабочий): ")
        return ("Телефон (рабочий)", data)
    elif number_many_condition_menu == "6":
        data = input("Телефон личный (сотовый): ")
        return ("Телефон личный (сотовый)", data)

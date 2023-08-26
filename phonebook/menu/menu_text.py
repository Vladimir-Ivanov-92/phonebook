def main_menu() -> str:
    print("Главное меню:")
    print("1 - Вывести весь справочник")
    print("2 - Добавить новую запись в справочник")
    print("3 - Найти запись в справочнике")
    print("4 - Редактировать запись в справочнике")
    print("0 - Завершить программу")

    user_input_main = input("Укажите номер выбранного варианта: ")
    return user_input_main


def search_menu() -> str:
    print("Меню поиска:")
    print("1 - Поиск по номеру записи")
    print("2 - Поиск по одному условию")
    print("3 - Поиск по нескольким условиям")
    print("0 - Назад")

    user_input_search = input("Укажите номер выбранного варианта: ")
    return user_input_search


def one_condition_menu() -> str:
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


def many_condition_menu() -> str:
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


def update_menu() -> str:
    print("Выберите обновляемые данные:")
    print("1 - Фамилия")
    print("2 - Имя")
    print("3 - Отчество")
    print("4 - Название организации:")
    print("5 - Телефон (рабочий):")
    print("6 - Телефон личный (сотовый):")
    print("0 - Назад")

    user_input_search = input("Укажите номер выбранного варианта: ")
    return user_input_search

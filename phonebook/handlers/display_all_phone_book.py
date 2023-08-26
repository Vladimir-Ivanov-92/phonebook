from phonebook import config
from phonebook.service import _get_column_names_from_df, _get_all_row_from_df


def display_directory_entries_on_the_screen_with_paginate(page_size):
    name_columns = _get_column_names_from_df(config.TABLE_NAME)
    all_row = _get_all_row_from_df(config.TABLE_NAME)

    num_pages = (len(all_row) + page_size - 1) // page_size

    for page_num in range(num_pages):
        start_num = page_num * page_size
        end_num = min((page_num + 1) * page_size, len(all_row))
        page_data = all_row[start_num:end_num]

        print(f"--- Страница {page_num + 1} of {num_pages} ---")
        print(name_columns)
        for row in page_data:
            print(row)

        if page_num == num_pages - 1:
            break
        else:
            user_input = input("Нажмите Enter чтоб перейти на следующую "
                               "страницу or 'q' для выхода: ")
            if user_input.lower() == 'q':
                break

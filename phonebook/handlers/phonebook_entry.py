from typing import Any

import pandas as pd
from pandas import DataFrame

from phonebook.handlers.handlers_service import _get_dataframe, \
    _get_column_names_from_df, \
    _input_data_for_new_row


class PhonebookEntry():
    """ Запись в телефонной книге"""

    def __init__(self, table_name: str, page_size: int):
        self.table_name = table_name
        self.page_size = page_size
        self.df = _get_dataframe(self.table_name)

    def _get_formated_row(self, row: tuple[Any]) -> str:
        formatted_row = "{:<5} {:<10} {:<10} {:<15} {:<30} {:<20} {:<25}".format(
            row[0] + 1, row[1], row[2], row[3],
            row[4], row[5],
            row[6]
        )
        return formatted_row

    def _formatted_print_for_all_row(self, result_search: DataFrame,
                                     title: str = None) -> list[str]:
        """Отформатированный вывод в консоль всех строк"""
        name_columns = _get_column_names_from_df(self.table_name)
        all_formatted_row = []
        if title:
            print(title)
        print(name_columns)
        for row in result_search.itertuples():
            formatted_row = self._get_formated_row(row)
            all_formatted_row.append(formatted_row)
        return all_formatted_row

    def _formatted_print(self, result_search: DataFrame, title: str = None) -> None:
        """Отформатированный вывод в консоль выбранных строк"""
        name_columns = _get_column_names_from_df(self.table_name)
        if title:
            print(title)
        print(name_columns)
        for row in result_search.itertuples():
            formatted_row = self._get_formated_row(row)
            print(formatted_row)

    def view_all_entries_paginated(self) -> None:
        """Просмотр всех строк в телефонной книге"""
        all_row = self._formatted_print_for_all_row(self.df)

        num_pages = (len(all_row) + self.page_size - 1) // self.page_size

        for page_num in range(num_pages):
            start_num = page_num * self.page_size
            end_num = min((page_num + 1) * self.page_size, len(all_row))
            page_data = all_row[start_num:end_num]

            print(f"--- Страница {page_num + 1} of {num_pages} ---")

            for row in page_data:
                print(row)

            if page_num == num_pages - 1:
                break
            else:
                user_input = input("Нажмите Enter чтоб перейти на следующую "
                                   "страницу or 'q' для выхода: ")
                if user_input.lower() == 'q':
                    break

    def add_new_row(self) -> None:
        """Добавлет новую запись в конец csv файла"""
        data = _input_data_for_new_row()

        new_row_df = pd.DataFrame([data], columns=self.df.columns)
        new_df = pd.concat((self.df, new_row_df), ignore_index=True)

        file_path = f"data/{self.table_name}.csv"
        new_df.to_csv(file_path, index=False)

        # Вывод в терминал обновленной строки
        title = "Добавлена новая запись: "

        # Создаем новый объект DataFrame с данными добавленной строки
        df = pd.DataFrame([new_df.iloc[-1]])
        self._formatted_print(df, title)

    def edit_entry(self, result_search: DataFrame, data) -> None:
        """Редактирование записи"""
        # Индекс записи и имя столбца для обновления
        row_index = result_search.index
        column_name = data[0]

        # Новое значение для обновления
        new_value = data[1]

        # Обновление значения
        self.df.loc[row_index, column_name] = new_value

        # Сохранение обновленной строки в csv файл
        file_path = f"data/{self.table_name}.csv"
        self.df.to_csv(file_path, index=False)

        # Вывод в терминал обновленной строки
        title = "Обновленная строка: "
        self._formatted_print(self.df.iloc[row_index], title)

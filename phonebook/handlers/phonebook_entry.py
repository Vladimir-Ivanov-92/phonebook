import pandas as pd
from pandas import DataFrame

from phonebook.service import _get_dataframe, _get_column_names_from_df, \
    _input_data_for_new_row


class PhonebookEntry():
    """ Запись в телефонной книге"""

    def __init__(self, table_name):
        self.table_name = table_name
        self.df = _get_dataframe(self.table_name)

    def _formatted_print(self, result_search: DataFrame, title: str):
        """Отформатированный вывод в консоль полученных данных"""
        name_columns = _get_column_names_from_df(self.table_name)
        print(title)
        print(name_columns)

        for row in result_search.itertuples():
            formatted_row = "{:<5} {:<10} {:<10} {:<15} {:<30} {:<20} {:<25}".format(
                row[0] + 1, row[1], row[2], row[3],
                row[4], row[5],
                row[6]
            )
            print(formatted_row)

    def add_new_row(self):
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

    def edit_entry(self, result_search: DataFrame, data):
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

from pandas import DataFrame

from phonebook.service import _get_dataframe, _get_column_names_from_df


class PhonebookEntry():

    def __init__(self, table_name):
        self.table_name = table_name
        self.df = _get_dataframe(self.table_name)

    def _formatted_print(self, result_search):
        name_columns = _get_column_names_from_df(self.table_name)
        print("Обновленная строка: ")
        print(name_columns)

        for row in result_search.itertuples():
            formatted_row = "{:<5} {:<10} {:<10} {:<15} {:<30} {:<20} {:<25}".format(
                row[0] + 1, row[1], row[2], row[3],
                row[4], row[5],
                row[6]
            )
            print(formatted_row)


    def edit_entry(self, result_search:DataFrame, data):

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
        self._formatted_print(self.df.iloc[row_index])



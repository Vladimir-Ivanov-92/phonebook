import pandas as pd

from phonebook.service import _get_dataframe, _get_column_names_from_df


class FindRecord():

    def __init__(self, table_name):
        self.table_name = table_name
        self.df = _get_dataframe(self.table_name)
        self.num_rows = self.df.shape[0]  # Количество строк в DataFrame

    def _formatted_print(self, result_search):
        name_columns = _get_column_names_from_df(self.table_name)
        print("Результаты поиска: ")
        print(name_columns)

        for row in result_search.itertuples():
            formatted_row = "{:<5} {:<10} {:<10} {:<15} {:<30} {:<20} {:<25}".format(
                row[0] + 1, row[1], row[2], row[3],
                row[4], row[5],
                row[6]
            )
            print(formatted_row)

    def index_search(self, index):
        if index >= 0 and index < self.num_rows:
            result_search = pd.DataFrame([self.df.iloc[index]])
            self._formatted_print(result_search)
            return result_search
        else:
            print("Индекс за пределами диапазона")

    def condition_search(self, column: str, condition: str):
        result_search = self.df[self.df[column] == condition]
        self._formatted_print(result_search)
        return result_search

    def conditions_search(self, conditions: list[tuple[str, str]]):
        # Комбинирование условий с использованием оператора ИЛИ (&)
        combined_condition = self.df[conditions[0][0]] == conditions[0][1]
        for col, value in conditions[1:]:
            combined_condition = combined_condition & (self.df[col] == value)

        # Применение фильтра
        result_search = self.df[combined_condition]

        if result_search.empty:
            print(f"Совпадений с условием: {conditions} не найдено!")
        else:
            self._formatted_print(result_search)
            return result_search

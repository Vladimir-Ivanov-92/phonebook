import pandas as pd

from phonebook.models import NewRowData


def _get_dataframe(table_name):
    file_path = f"data/{table_name}.csv"
    df = pd.read_csv(file_path)
    return df

def _get_column_names_from_df(table_name: str):
    """Вывод наименований колонок из справочника на экран"""

    file_path = f"data/{table_name}.csv"
    df = pd.read_csv(file_path)

    columns = df.columns.values

    name_columns = "{:<5} {:<10} {:<10} {:<15} {:<30} {:<15} {:<20}".format(
        "№", columns[0], columns[1], columns[2], columns[3],
        columns[4], columns[5]
    )

    return name_columns


def _get_all_row_from_df(table_name: str):
    """Вывод постранично записей из справочника  на экран"""

    file_path = f"data/{table_name}.csv"
    df = pd.read_csv(file_path)

    all_formatted_row = []

    for row in df.itertuples():
        formatted_row = "{:<5} {:<10} {:<10} {:<15} {:<30} {:<20} {:<25}".format(
            row[0] + 1, row[1], row[2], row[3],
            row[4], row[5],
            row[6]
        )
        all_formatted_row.append(formatted_row)

    return all_formatted_row
def _input_data_for_new_row():
    last_name = input("Фамилия: ")
    first_name = input("Имя: ")
    patronymic = input("Отчество: ")
    name_of_organization = input("Название организации: ")
    work_phone = input("Телефон (рабочий): ")
    personal_phone_mobile = input("Телефон личный (сотовый): ")

    new_row_data = NewRowData(
        last_name=last_name,
        first_name=first_name,
        patronymic=patronymic,
        name_of_organization=name_of_organization,
        work_phone=work_phone,
        personal_phone_mobile=personal_phone_mobile
    )

    data_list = list(new_row_data.model_dump().values())
    return data_list

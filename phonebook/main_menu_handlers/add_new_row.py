import pandas as pd

from phonebook.service import _input_data_for_new_row, _get_column_names_from_df


def add_new_row(table_name):
    data = _input_data_for_new_row()

    file_path = f"data/{table_name}.csv"
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        pass

    df_1 = pd.DataFrame([data], columns=df.columns)
    df_new = pd.concat((df, df_1), ignore_index=True)

    df_new.to_csv(file_path, index=False)

    name_columns = _get_column_names_from_df(table_name)
    print(name_columns)


    row = df_new.iloc[-1].values

    formatted_row = "{:<5} {:<10} {:<10} {:<15} {:<30} {:<20} {:<25}".format(
        len(df) - 1, row[0], row[1],
        row[2], row[3], row[4],
        row[5]
    )
    print(formatted_row)

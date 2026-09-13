#!/usr/bin/env python3
#
#
#       Copyright 2025 Alejandro Gomez
#
#       This program is free software: you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation, either version 3 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import sys
import datetime
import pandas


def error_msg(exit_number: int, message: str) -> None:
    print(f"ERROR: {message}")
    sys.exit(exit_number)

def get_df(file_path: str) -> pandas.DataFrame:
    try:
        if os.path.exists(file_path):
            return pandas.read_csv(file_path)
    except FileNotFoundError:
        error_msg(2, f"The file {file_path} does not exist.")
    except pandas.errors.EmptyDataError:
        error_msg(3, f"The file {file_path} is empty.")
    except pandas.errors.ParserError:
        error_msg(4, f"Parsing the file {file_path} failed.")
    return pandas.DataFrame()

class DataFrameIncompatibleError(Exception):
    pass

def comprobar_compatibilidad(df_left: pandas.DataFrame, df_right: pandas.DataFrame) -> None:
    # Comprobar que los DataFrames no están vacíos
    if df_left.empty or df_right.empty:
        raise DataFrameIncompatibleError("One of the DataFrames is empty.")
    # Comprobar que los DataFrames tienen las mismas columnas
    if set(df_left.columns) != set(df_right.columns):
        raise DataFrameIncompatibleError("The DataFrames do not have the same columns.")

    # Comprobar que los DataFrames tienen el mismo tipo de datos en cada columna
    for col in df_left.columns:
        if df_left[col].dtype != df_right[col].dtype:
            raise DataFrameIncompatibleError(f"Column '{col}' has different data types in the DataFrames.")

def get_rows_only_in_left(df_left: pandas.DataFrame, df_right: pandas.DataFrame) -> pandas.DataFrame:
    rows_in_right = set(map(tuple, df_right.to_numpy()))
    return df_left.loc[[tuple(row) not in rows_in_right for row in df_left.to_numpy()]].copy()


def get_rows_only_in_right(df_left: pandas.DataFrame, df_right: pandas.DataFrame) -> pandas.DataFrame:
    rows_in_left = set(map(tuple, df_left.to_numpy()))
    return df_right.loc[[tuple(row) not in rows_in_left for row in df_right.to_numpy()]].copy()


def generar_datos(df_left: pandas.DataFrame, df_right: pandas.DataFrame, output_path: str) -> None:
    try:
        comprobar_compatibilidad(df_left, df_right)
    except DataFrameIncompatibleError as e:
        error_msg(5, f"{e}")

    # Calcular los valores
    total_left = len(df_left)
    total_right = len(df_right)

    # Calcular los valores únicos y duplicados
    uniques_left = df_left.drop_duplicates().shape[0]
    uniques_right = df_right.drop_duplicates().shape[0]
    duplicates_left = total_left - uniques_left
    duplicates_right = total_right - uniques_right

    # Calcular los valores que solo están en un lado
    df_only_left = get_rows_only_in_left(df_left, df_right)
    df_only_right = get_rows_only_in_right(df_left, df_right)
    only_left = len(df_only_left)
    only_right = len(df_only_right)

    # Calcular los valores que están en ambos lados
    in_both = df_left.apply(tuple, 1).isin(df_right.apply(tuple, 1)).sum()

    # Crear un nuevo DataFrame con los valores calculados
    df_result = pandas.DataFrame({
        "Total_left": [total_left],
        "Total_right": [total_right],
        "Uniques_left": [uniques_left],
        "Uniques_right": [uniques_right],
        "Duplicates_left": [duplicates_left],
        "Duplicates_right": [duplicates_right],
        "Only_left": [only_left],
        "Only_right": [only_right],
        "In_both": [in_both]
    })

    # String con el año, mes y día YYYYMMDD_HHMMSS
    current_date = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    # Crear el directorio en el directorio de salida añadiendo current_date
    final_path = os.path.join(output_path, current_date)
    os.makedirs(final_path, exist_ok=True)

    # Guardar el DataFrame en el directorio de salida
    df_result.to_csv(os.path.join(final_path, 'result.csv'), index=False)
    df_only_left.to_csv(os.path.join(final_path, 'left.csv'), index=False)
    df_only_right.to_csv(os.path.join(final_path, 'right.csv'), index=False)


def compare_csv(path_1: str, path_2: str, output_path: str) -> None:
    df_1 = get_df(path_1)
    df_2 = get_df(path_2)
    generar_datos(df_1, df_2, output_path)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        error_msg(1,f"Arguments must be: {sys.argv[0]} [FILE_PATH_LEFT] [FILE_PATH_RIGHT] [OUTPUT_FILE_PATH]")

    compare_csv(sys.argv[1], sys.argv[2], sys.argv[3])

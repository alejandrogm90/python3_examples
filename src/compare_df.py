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
import pandas


def exit_msg(exit_number: int, message: str) -> None:
    print(f"ERROR: {message}")
    exit(exit_number)

def get_df(file_path: str) -> pandas.DataFrame | None:
    extension = file_path.split(".")[-1]
    if os.path.exists(file_path):
        if extension == "csv":
            return pandas.read_csv(file_path)
        elif extension == "xlsx":
            return pandas.read_excel(file_path)

def get_output_path(file_path: str) -> str:
    extension = file_path.split(".")[-1]
    new_extension = "_diferencias.csv"
    if extension == "xlsx":
        return file_path.replace(".xlsx", new_extension)
    else:
        return file_path.replace(".csv", new_extension)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        exit_msg(1, f"Arguments must be: {sys.argv[0]} [FILE_1] [FILE_2]")

    df_left = get_df(sys.argv[1])
    df_right = get_df(sys.argv[2])
    if df_left is None:
        exit_msg(2, f"Not valid file: {sys.argv[1]}")
    if df_left is None:
        exit_msg(3, f"Not valid file: {sys.argv[2]}")

    # Calcular los valores
    total_left = len(df_left)
    total_right = len(df_right)

    # Calcular los valores únicos y duplicados
    uniques_left = df_left.drop_duplicates().shape[0]
    uniques_right = df_right.drop_duplicates().shape[0]
    duplicates_left = total_left - uniques_left
    duplicates_right = total_right - uniques_right

    # Calcular los valores que solo están en un lado
    only_left = df_left[~df_left.apply(tuple, 1).isin(df_right.apply(tuple, 1))].shape[0]
    only_right = df_right[~df_right.apply(tuple, 1).isin(df_left.apply(tuple, 1))].shape[0]

    # Calcular los valores que están en ambos lados
    both = df_left.apply(tuple, 1).isin(df_right.apply(tuple, 1)).sum()

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
        "Both": [both]
    })

    # Guardar el nuevo DataFrame en un archivo CSV
    df_result.to_csv(get_output_path(sys.argv[1]), index=False)

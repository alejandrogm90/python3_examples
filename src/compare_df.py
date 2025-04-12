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
    try:
        if os.path.exists(file_path):
            if extension == "csv":
                return pandas.read_csv(file_path)
            elif extension == "xlsx":
                return pandas.read_excel(file_path)
    except FileNotFoundError:
        print(f"Error: El ficheros {file_path} no existe")
        sys.exit(1)
    except pandas.errors.EmptyDataError:
        print(f"Error: El fichero {file_path} está vacío")
        sys.exit(1)
    except pandas.errors.ParserError:
        print(f"Error: Error al parsear el fichero {file_path}")

def get_output_path(file_path: str) -> str:
    extension = file_path.split(".")[-1]
    new_extension = "_diferencias.csv"
    if extension == "xlsx":
        return file_path.replace(".xlsx", new_extension)
    else:
        return file_path.replace(".csv", new_extension)


class DataFrameIncompatibleError(Exception):
    pass

def comprobar_compatibilidad(df_left, df_right):
    # Comprobar que los DataFrames tienen las mismas columnas
    if set(df_left.columns) != set(df_right.columns):
        raise DataFrameIncompatibleError("Los DataFrames no tienen las mismas columnas")

    # Comprobar que los DataFrames tienen el mismo tipo de datos en cada columna
    for col in df_left.columns:
        if df_left[col].dtype != df_right[col].dtype:
            raise DataFrameIncompatibleError(f"La columna '{col}' tiene tipos de datos diferentes en los DataFrames")

def calcular_valores(df_left: pandas.DataFrame, df_right: pandas.DataFrame) -> pandas.DataFrame | None:
    try:
        comprobar_compatibilidad(df_left, df_right)
    except DataFrameIncompatibleError as e:
        print(f"Error: {e}")
        return None

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
    return pandas.DataFrame({
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


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(f"Arguments must be: {sys.argv[0]} [FILE_1] [FILE_2]")
        exit(1)

    df_1 = get_df(sys.argv[1])
    df_2 = get_df(sys.argv[2])

    df_result = calcular_valores(df_1, df_2)

    if df_result is not None:
        # Guardar el nuevo DataFrame en un archivo CSV
        df_result.to_csv(get_output_path(sys.argv[1]), index=False)

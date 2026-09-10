#!/usr/bin/env python3
#
#
#       Copyright 2026 Alejandro Gomez
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
import matplotlib.pyplot as plt



def buscar_ficheros_por_nombre(directorio: str, subcadena: str):
    ficheros_encontrados = []
    for nombre_fichero in os.listdir(directorio):
        if subcadena in nombre_fichero:
            ficheros_encontrados.append(f'{directorio}/{nombre_fichero}')

    return ficheros_encontrados


def cargar_csv_a_dataframe(ficheros: list) -> pandas.DataFrame:
    # Lista para almacenar los DataFrames
    dataframes = []

    for fichero in ficheros:
        try:
            # Cargar cada CSV en un DataFrame
            df_temp = pandas.read_csv(fichero)
            dataframes.append(df_temp)
        except Exception as e:
            print(f"Error al cargar el archivo {fichero}: {e}")

    # Combinar todos los DataFrames en uno solo
    df = pandas.concat(dataframes, ignore_index=True)

    if "Ibex" in ficheros[0]:
        # Eliminar filas donde la columna "Índice" es nula
        df = df.dropna(subset=['Nombre'])

        # Definir las columnas a convertir
        numericas = ['Último', '% Dif', 'Máximo', 'Mínimo', 'Volumen', 'Efectivo (miles €)']

        # Convertir columnas necesarias a tipo numérico
        for col in numericas:
            df[col] = df[col].replace({'[^0-9,.]': ''}, regex=True)  # Eliminar caracteres no numéricos
            df[col] = df[col].str.replace('.', '', regex=False)  # Eliminar el "." de los miles
            df[col] = df[col].str.replace(',', '.', regex=False)  # Convertir la "," en "." para formato float
            df[col] = df[col].str.replace('%', '', regex=False)  # Convertir la "," en "." para formato float
            df[col] = df[col].astype(float)  # Convertir a float

    else:
        # Eliminar filas donde la columna "Índice" es nula
        df = df.dropna(subset=['Índice'])

        # Definir las columnas a convertir
        numericas = ['Último', '% Dif', 'Máximo', 'Mínimo', '% Dif.Año']

        # Convertir columnas necesarias a tipo numérico
        for col in numericas:
            df[col] = df[col].replace({'[^0-9,.]': ''}, regex=True)  # Eliminar caracteres no numéricos
            df[col] = df[col].str.replace('.', '', regex=False)  # Eliminar el "." de los miles
            df[col] = df[col].str.replace(',', '.', regex=False)  # Convertir la "," en "." para formato float
            df[col] = df[col].str.replace('%', '', regex=False)  # Convertir la "," en "." para formato float
            df[col] = df[col].astype(float)  # Convertir a float

    return df

def plot_indices(df: pandas.DataFrame) -> None:


    # Visualizar los datos
    plt.figure(figsize=(12, 6))

    # Gráfico de barras del precio 'Último'
    plt.bar(df['Índice'], df['Último'], color='lightgreen')
    plt.xlabel('Índices')
    plt.ylabel('Último Precio')
    plt.xticks(rotation=90)  # Girar los nombres de los índices para una mejor visualización
    plt.title('Último Precio de los Índices')
    plt.tight_layout()  # Ajustar para evitar el recorte de la etiqueta
    plt.show()

def plot_ibex35(df: pandas.DataFrame) -> None:
    # Visualizar los datos
    plt.figure(figsize=(6, 12))

    # Gráfico de barras del precio 'Último'
    plt.bar(df['Nombre'], df['Último'], color='skyblue')
    plt.xlabel('Acciones')
    plt.ylabel('Último Precio')
    plt.xticks(rotation=90)  # Girar los nombres de las acciones para una mejor visualización
    plt.title('Último Precio de las Acciones')
    plt.tight_layout()  # Ajustar para evitar el recorte de la etiqueta
    plt.show()

if __name__ == '__main__':
    output_directory = os.getenv("PATH_BOLSA", "~/Bolsa")

    lista_indices = buscar_ficheros_por_nombre(output_directory, "Índices_")
    lista_ibex35 = buscar_ficheros_por_nombre(output_directory, "info_Ibex35_")

    if len(lista_indices) == 0:
        print(f"Error al cargar la lista índices")
        sys.exit(1)
    elif len(lista_ibex35) == 0:
        print(f"Error al cargar la lista ibex35")
        sys.exit(2)

    df_indices = cargar_csv_a_dataframe(lista_indices)
    df_ibex35 = cargar_csv_a_dataframe(lista_ibex35)

    df_indices.to_csv(f'{output_directory}/final_indices.csv', index=False)
    df_ibex35.to_csv(f'{output_directory}/final_ibex.csv', index=False)

    #plot_indices(df_indices)
    #plot_ibex35(df_ibex35)

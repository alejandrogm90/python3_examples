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
import networkx as nx
import matplotlib.pyplot as plt

def get_df(file_path: str) -> pandas.DataFrame | None:
    extension = file_path.split(".")[-1]
    try:
        if os.path.exists(file_path):
            if extension == "csv":
                return pandas.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: El ficheros {file_path} no existe")
        sys.exit(1)
    except pandas.errors.EmptyDataError:
        print(f"Error: El fichero {file_path} está vacío")
        sys.exit(1)
    except pandas.errors.ParserError:
        print(f"Error: Error al parsear el fichero {file_path}")
    raise FileNotFoundError


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"Arguments must be: {sys.argv[0]} [FILE_1]")
        exit(1)

    df_1 = get_df(sys.argv[1])
    Grafo = nx.Graph()
    # Grafo.is_directed()
    fig, ax = plt.subplots(figsize=(2, 3))

    df_2 = df_1.copy()
    if df_2 is not None:
        df_2 = df_2[['Vertex']].drop_duplicates()
        for index, row in df_2.iterrows():
            Grafo.add_node(str(row['Vertex']))

    if df_1 is not None:
        for index, row in df_1.iterrows():
            Grafo.add_edge(str(row['Vertex']), str(row['Adjacent']))

    nx.draw(Grafo, with_labels=True, ax=ax)
    plt.show()

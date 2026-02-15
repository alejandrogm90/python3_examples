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
import json
import sys

import pandas
from common_functions import error_msg


def buscar_json_y_cargar(path) -> pandas.DataFrame:
    # Función para buscar archivos JSON y obtener los valores de "user"
    data = []

    # Recorrer todos los directorios y archivos en el path dado
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.json'):  # Comprobar la extensión .json
                print(file)
                file_path = os.path.join(root, file)  # Ruta completa del archivo

                # Cargar el archivo JSON
                with open(file_path, 'r') as json_file:
                    try:
                        contenido = json.load(json_file)
                        user = "ERROR"
                        if 'creator_id' in contenido:  # Comprobar si la clave "user" existe
                            user = contenido['creator_id']
                        else:
                            for item in contenido:
                                if 'user' in item:
                                    user = item['user']
                                    break
                        data.append({'user': user, 'path': file_path})
                    except json.JSONDecodeError:
                        print(f'Error al leer el archivo: {file_path}')  # Manejo de errores

    current_df = pandas.DataFrame(data).drop_duplicates(subset='user', keep='first')
    return current_df

if __name__ == '__main__':
    if sys.argv.__len__() != 2:
        error_msg(1, "Parámetros erróneos")

    directorio_a_buscar = sys.argv[1]
    if not os.path.isdir(directorio_a_buscar):
        error_msg(2, f"El directorio '{directorio_a_buscar}'")

    resultado_df = buscar_json_y_cargar(directorio_a_buscar)

    # Mostrar el DataFrame resultante
    print(resultado_df)
    resultado_df.to_csv(f"{directorio_a_buscar}/users.csv",header=False)

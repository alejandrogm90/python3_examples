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

def eliminar_ficheros_cero_bytes(ruta: str) -> None:
    """
    Busca y elimina ficheros con 0 bytes en un directorio y sus subcarpetas.

    :param ruta: Ruta del directorio donde buscar.
    """
    for root, dirs, files in os.walk(ruta):
        for file in files:
            ruta_file = os.path.join(root, file)
            try:
                if os.path.getsize(ruta_file) == 0:
                    os.remove(ruta_file)
                    print(f"Eliminado fichero '{ruta_file}' con 0 bytes")
            except Exception as e:
                print(f"Error al procesar {ruta_file}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Uso: python {sys.argv[0]} <ruta_directorio>")
        sys.exit(1)

    ruta_directorio = sys.argv[1]
    if not os.path.isdir(ruta_directorio):
        print(f"'{ruta_directorio}' no es un directorio válido")
        sys.exit(2)

    eliminar_ficheros_cero_bytes(ruta_directorio)

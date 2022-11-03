#!/usr/bin/env python3
#
#
#       Copyright 2022 Alejandro Gomez
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

import sys

# VARIABLES GLOBALES
BIBLIOTECA = {}

def sustituirCadena(cad):
    cad_temp = cad
    for elemento in BIBLIOTECA:
        cad_temp = cad_temp.replace(
            str('${'+str(elemento)+'}'), str(BIBLIOTECA[elemento]))
    return cad_temp

# Limpia los extremos de las cadena
def lc1(cad):
    cad_limp = cad.rstrip()
    return cad_limp.lstrip()


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Número de parámetros erroneo.")
        sys.exit(1)
    else:
        try:
            with open(sys.argv[1], 'r', encoding="utf-8") as properties_file:
                cadena1 = ""
                for line in properties_file.readlines():
                    if line[0] != "#" and len(line) > 3:
                        tmpl = lc1(line)
                        if tmpl[(len(tmpl)-1)] == "\\":
                            cadena1 = cadena1 + tmpl[0:(len(tmpl)-1)]
                        else:
                            cadena1 = cadena1 + tmpl
                            par = cadena1.split("=")
                            if len(par) > 1:
                                valor = par[1]
                                posicion = 2
                                while posicion < len(par):
                                    valor = valor + "=" + par[posicion]
                                    posicion = posicion + 1
                                BIBLIOTECA.update(
                                    {lc1(par[0]): lc1(sustituirCadena(valor).
                                                      replace("\n", ''))})
                            cadena1 = ""
        except properties_file:
            print("Error al leer el primer fichero.")

        # for elemento in BIBLIOTECA:
        #     print(elemento+" = "+BIBLIOTECA[elemento])
        # exit(0)

        try:
            with open(sys.argv[2], 'r', encoding="utf-8") as current_file:
                for line in current_file.readlines():
                    sys.stdout.write(sustituirCadena(line))
        except current_file:
            print("Error al leer el segundo fichero.")

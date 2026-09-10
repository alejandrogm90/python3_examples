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
from asyncio.windows_events import NULL


class PropertiesFile:
    def __init__(self, location):
        self.file_location = location
        self.propiedades = list()
        current_file = open(self.file_location, 'r', encoding="utf-8")
        line = current_file.readline()
        while line:
            propiedad = self.es_propiedad(line)
            if propiedad != NULL:
                self.propiedades.append(propiedad)
            line = current_file.readline()

    def get_num_propiedades(self):
        return len(self.propiedades)

    def get_propiedades(self):
        return self.propiedades

    def get_propiedad(self, indice):
        for propiedad in self.propiedades:
            if indice == propiedad[0]:
                return propiedad
        return NULL

    @staticmethod
    def es_propiedad(line):
        if line[0] != ' ' and "=" in line:
            partes = line.split("=")
            # if partes[0] != "":
            print("---- PARTES:  " + partes[1])
            if partes[0] != "":
                return partes
        return NULL

    def existe_propiedad(self, propiedad):
        for propiedadActual in self.propiedades:
            if propiedad == propiedadActual[0]:
                return True
        return False

    def contiene(self, fichero):
        num_propiedad_no_existente = 0
        for propiedadActual in self.propiedades:
            if not fichero.existe_propiedad(propiedadActual[0]):
                print("[WARN] No existe: " + propiedadActual[0])
                num_propiedad_no_existente = num_propiedad_no_existente + 1
        if num_propiedad_no_existente > 0:
            print("[ERROR] Faltan " + str(num_propiedad_no_existente) + " propiedades")
        else:
            print("[MSG] Contiene todas las propiedades")

    def contiene2(self, fichero):
        num_propiedad_no_existente = 0
        for propiedadActual in self.propiedades:
            existe = ""
            for propiedadOtro in fichero.get_propiedades():
                if propiedadOtro[0] == propiedadActual[0]:
                    existe = "si"
                    break
            if existe == "":
                print("[WARN] No existe: " + propiedadActual[0])
                num_propiedad_no_existente = num_propiedad_no_existente + 1
        if num_propiedad_no_existente > 0:
            print("[ERROR] Faltan " + str(num_propiedad_no_existente) + " propiedades")
        else:
            print("[MSG] Contiene todas las propiedades")


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("ERROR:\n" + sys.argv[0] + " fichero1.csv fichero2.csv")
        sys.exit(1)

    FIRST_FILE = PropertiesFile(sys.argv[1])
    SECOND_FILE = PropertiesFile(sys.argv[2])

    FIRST_FILE.contiene(SECOND_FILE)
    print(str(FIRST_FILE.get_num_propiedades()) + " - " + str(SECOND_FILE.get_num_propiedades()) + " = " + str(
        FIRST_FILE.get_num_propiedades() - SECOND_FILE.get_num_propiedades()))

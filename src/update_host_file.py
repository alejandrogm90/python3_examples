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

import os
import platform
import sys

import common_functions as cf

# GLOBALS
SALTO_LINEA = "\n"
FICHERO_SERBIDORES_LINUX = "/etc/hosts"
FICHERO_SERBIDORES_WINDOWS = "/etc/hosts"


class Dominio():
    def __init__(self, nombre, nombre2=""):
        self.nombre = nombre
        self.listaNombres = []
        if nombre2 != "":
            self.listaNombres.append(nombre2)

    def devolverNombre(self):
        return self.nombre

    def devolverListaNombres(self):
        return self.listaNombres

    def existeElemento(self, nombre):
        for elemento in self.listaNombres:
            if elemento == nombre:
                return True
        return False

    def agregarNombre(self, nombre):
        if not self.existeElemento(nombre):
            self.listaNombres.append(nombre)

    def __str__(self):
        texto = ""
        for elemento in self.listaNombres:
            texto += self.nombre + " " + elemento + SALTO_LINEA
        return texto


class Gestor():
    def __init__(self):
        self.listaDominios = []
        self.cabecera = []

    def devolverCabecera(self):
        return self.cabecera

    def devolverListaDominios(self):
        return self.listaDominios

    def existeDominio(self, dominio):
        for elemento in self.listaDominios:
            if dominio.devolverNombre() == elemento.devolverNombre():
                return True
        return False

    def leerFichero(self, direccion):
        f1 = open(direccion, "r")
        lineas = f1.readlines()
        f1.close()
        for linea in lineas:
            linea2 = linea.replace(SALTO_LINEA, "")
            if len(linea2) > 0 and "#" == linea2[1]:
                print(linea2)
            else:
                self.cabecera.append(linea2)

    def agregarDominio(self, dominio):
        existe = False
        for elemento in self.listaDominios:
            if dominio.devolverNombre() == elemento.devolverNombre():
                existe = True
                for nombre in dominio.devolverListaNombres():
                    elemento.agregarNombre(nombre)
                break
        if not existe:
            self.listaDominios.append(dominio)

    def combinar(self, dominio_B):
        self.cabecera = dominio_B.devolverCabecera()
        listaDominios2 = []
        for dominio in dominio_B.devolverListaDominios():
            self.agregarDominio(dominio)

    def __str__(self):
        texto = ""
        for elemento in self.cabecera:
            texto += elemento + SALTO_LINEA
        for elemento in self.listaDominios:
            texto += str(elemento)
        return texto


def devolverFicheroSerbidores():
    if platform.system() == "Windows":
        return FICHERO_SERBIDORES_WINDOWS
    elif platform.system() == "Linux":
        return FICHERO_SERBIDORES_LINUX
    else:
        cf.error_msg(3, "Plataforma no soportada")


if __name__ == '__main__':
    # Add Banner
    cf.print_mega_banner(cf.get_file_name(sys.argv[0], True).split(".")[0])
    print("")

    if len(sys.argv) == 2:
        if not os.path.isfile(sys.argv[1]):
            cf.error_msg(2, "El parámetro introducido '" + sys.argv[1] + "' no es un fichero.")
        else:
            # Origen
            gestor_1 = Gestor()
            gestor_1.leerFichero(devolverFicheroSerbidores())
            # Datos
            gestor_2 = Gestor()
            gestor_2.leerFichero(sys.argv[1])
            # Combinación
            gestor_1.combinar(gestor_2)
            print(gestor_1)
    elif len(sys.argv) == 3:
        # Origen
        gestor_1 = Gestor()
        gestor_1.leerFichero(devolverFicheroSerbidores())
        dominio_1 = Dominio(sys.argv[1], sys.argv[2])
        # print(dominio_1)
        gestor_1.agregarDominio(dominio_1)
        print(gestor_1)
    else:
        cf.error_msg(1, "Número de parámetros erróneos")

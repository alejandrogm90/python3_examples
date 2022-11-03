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

import sqlite3
import pyfiglet
from calendar import monthrange

def isDate(cadena):
    """ Check is the text recived is a rigth date
    :param cadena: datatime text (YYYY-MM-DD)
    :return: True or False
    """
    if len(cadena) != 10:
        return False
        
    if cadena[4] != "-" or cadena[7] != "-":
        return False

    try:
        anno = int(cadena[0:4])
        mes = int(cadena[5:7])
        dia = int(cadena[8:10])
    except:
        return False

    if mes > 12 or mes < 1:
        return False

    if anno < mes or anno < dia:
        return False

    if dia > monthrange(anno, mes)[1] or dia < 1:
        return False

    return True


def create_sqlitle3_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)

    return conn


def printBanner(character, sice, textList):
    """ Add Banner character, sice, text """
    print(character * sice)
    for line in textList:
        print(line)
    print(character * sice)


def printMegaBanner(text):
    ascii_banner = pyfiglet.figlet_format(text)
    print(ascii_banner)


def printFileEncoded(nombre):
    f1 = open(nombre,'r')
    linea = f1.readline()
    while (len(linea) > 0):
        nueva = ""
        for pos in range(0,len(linea)-1):
            nueva = nueva + str(chr(ord(linea[pos])+1))
        print(nueva)
        linea = f1.readline()

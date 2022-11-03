#!/usr/bin/env python3

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

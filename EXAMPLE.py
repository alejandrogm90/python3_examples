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

import configparser
import datetime
import random
import sys

import src.common_functions as cf
import src.extended_functions as ef

# GLOBALS
LOG_FILE = cf.get_file_name(sys.argv[0]) + ".log"
today = datetime.date.today()

if __name__ == '__main__':
    # Add Banner
    ef.print_mega_banner(cf.get_file_name(sys.argv[0], True))
    # Show script info
    info = {
        "name": str(cf.get_file_name(sys.argv[0], True)),
        "location": sys.argv[0],
        "description": "A simple script to print info",
        "Autor": "Alejandro Gómez",
        "calling": sys.argv[0] + " 2023-05-07 BTC ABC USD"
    }
    cf.show_script_info(info)

    config = configparser.ConfigParser()
    config.read_file(open("logging.conf", "r"))
    SECTION_NAME_1 = 'loggers'
    KEY_1 = 'keys'
    VALUE_1 = config.get(SECTION_NAME_1, KEY_1)
    print("\nSECTION_NAME: {0} | KEY: {1} | VALUE: {2}\n".format(SECTION_NAME_1, KEY_1, VALUE_1))

    textList = list()
    textList.append('La fecha actual en formato datetime : ' + str(datetime.datetime.now()))
    textList.append('La fecha actual en formato ctime : ' + today.ctime())
    cf.print_banner(".", textList)

    w = list()
    for i in range(4):
        w.append(random.uniform(0, 1))
    print(w)

    cf.info_msg("Mensaje informativo")
    cf.error_msg(0, "ERROR a drede")

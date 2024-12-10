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

import json
import logging
import os
from calendar import monthrange
from time import gmtime, strftime

logging.basicConfig(format='[%(asctime)s][%(levelname)s]%(message)s', datefmt='%Y-%d-%m %H:%M:%S', level=logging.INFO)
LOGGER = logging
SEPARATOR_1 = "###############################################################################################"
PROJECT_PATH = ""


def get_head_line(level: str) -> str:
    """ Returns log format headline

    :return: string log format
    """
    return "[" + get_time() + "][" + level + "]"


def info_msg(msg: str, output_file="") -> None:
    """ Show a menssage text

    :param msg: info menssage
    :param output_file: output file
    """
    LOGGER.info(": {0}".format(msg))
    if output_file != "":
        print_log_in_file(output_file, "{0}: {1}".format(get_head_line("INFO"), msg))


def warn_msg(msg: str, output_file="") -> None:
    """ Show a menssage text

    :param msg: warning menssage
    :param output_file: output file
    """
    LOGGER.warning(": {0}".format(msg))
    if output_file != "":
        print_log_in_file(output_file, "{0}: {1}".format(get_head_line("WARNING"), msg))


def error_msg(number: int, msg: str, output_file="") -> None:
    """ Show a menssage text and exits with output number

    :param number: output number
    :param msg: error menssage
    :param output_file: output file
    """
    LOGGER.error("[" + str(number) + "]: " + msg)
    if output_file != "":
        print_log_in_file(output_file, "{0}[{1}]: {2}".format(get_head_line("ERROR"), str(number), msg))
    exit(number)


def load_json(path: str) -> dict:
    """ Load a json file

    :param path: full path
    :return: json data
    """
    with open(path, 'r') as f1:
        data = json.load(f1)
    f1.close()
    return data


def load_config(project_path: str, log_file="") -> dict:
    """ Load a json config file

    :param project_path: full path
    :param log_file: log file
    :return: json data
    """
    full_path = "{0}/config/config.json".format(project_path)
    if os.path.exists(full_path):
        return load_json(full_path)
    else:
        error_msg(2, "Default configuration must be replaced", log_file)


def save_json(path: str, data: str) -> None:
    """ Write a json file

    :param path: full path
    :param data: data to write
    """
    father_directory = os.path.dirname(path)
    if not os.path.exists(father_directory):
        os.makedirs(father_directory)
    with open(path, 'w', encoding='utf-8') as f1:
        json.dump(data, f1, ensure_ascii=False, indent=4)
    f1.close()


def get_father_path(path: str) -> str:
    """ Returns father absolute path

    :return: path as string
    """
    return os.path.dirname(os.path.dirname(path))


def get_project_path() -> str:
    """ Returns the project absolute path
    PROJECT/src/src/cf.sh

    :return: path as string
    """
    if PROJECT_PATH != "":
        return PROJECT_PATH
    else:
        # Otra forma es usando os.path.dirname(os.path.abspath(sys.argv[0]))
        return os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


def get_time() -> str:
    """ Returns a complete date as YYYY-MM-dd HH:mm

    :return: all date as string
    """
    return strftime("%Y-%m-%d %H:%M:%S", gmtime())


def get_date() -> str:
    """ Returns a complete date as YYYY-MM-dd

    :return: all date as string
    """
    return strftime("%Y-%m-%d", gmtime())


def is_valid_date(cadena: str) -> bool:
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
    elif anno < mes or anno < dia:
        return False
    elif dia > monthrange(anno, mes)[1] or dia < 1:
        return False
    return True


def print_banner(characters: str, text_list: list) -> None:
    """ Print a simple banner
    :param characters: characters to repeat
    :param text_list: list to print
    """
    line_size = 0
    for line in text_list:
        if line_size < len(line):
            line_size = len(line)

    print(characters * (line_size + 4))
    for line in text_list:
        if len(line) == line_size:
            print(characters + " " + line + " " + characters)
        else:
            spaces = " " * (line_size - len(line) + 1)
            print(characters + " " + line + spaces + characters)
    print(characters * (line_size + 4))


def print_file_encoded(name: str) -> None:
    """ Print file with encoded text
    :param name: file's URI
    """
    f1 = open(name, 'r')
    linea = f1.readline()
    while len(linea) > 0:
        nueva = ""
        for pos in range(0, len(linea) - 1):
            nueva = nueva + str(chr(ord(linea[pos]) + 1))
        print(nueva)
        linea = f1.readline()


def get_file_name(location: str, extension=False) -> str:
    """ Returns file name not URI location
    :param location: URI of scritp
    :param extension: bool
    :return: file name
    """
    spliter_point = '.'
    name1 = os.path.split(location)[1]
    name2 = ""
    if extension:
        name2 = name1
    else:
        parts = len(name1.split(spliter_point))
        if parts <= 2:
            name2 = name1.split(spliter_point)[0]
        else:
            for part2 in range(0, (parts - 1)):
                name2 += name1.split(spliter_point)[part2]
    return name2


def get_file_log(location: str) -> str:
    """ Returns file name not URI location
    :param location: URI of scritp
    :return: file log name
    """
    return "{0}_{1}.log".format(get_file_name(location), get_date())


def print_log_in_file(output_file: str, msg: str) -> None:
    """ Print in log file

    :param output_file: file to write data
    :param msg: text to wirte
    """
    try:
        log_file = open(output_file, 'a')
        log_file.write(msg + os.linesep)
        log_file.close()
    except:
        print("Error writing in file: {0}".format(output_file))


def show_script_info(info: {}) -> None:
    """ Show a basic info
    :param info: array with all info
    """
    print(SEPARATOR_1)
    print("# Name            : " + info["name"])
    print("# Location        : " + info["location"])
    print("# Description     : " + info["description"])
    print("# Autor           : " + info["Autor"])
    print("# Execution_Date  : " + get_time())
    print("# Calling         : " + info["calling"])
    print(SEPARATOR_1)

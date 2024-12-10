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


def create_sqlitle3_connection(path: str):
    """ Create a database connection to the SQLite database specified by db_file
    :param path: path to database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(path)
    except sqlite3.Error as e:
        print(e)

    return conn


def get_values(path: str, sentence: str):
    """ Returns values from SQLite database specified by     db_file
    :param path: path to database file
    :param sentence: sentence
    :return: Connection object or None
    """
    conn = create_sqlitle3_connection(path)
    cur = conn.cursor()
    rows = ""
    try:
        cur.execute(sentence)
        rows = cur.fetchall()
    except sqlite3.Error as e:
        print(e)
    return rows


def execute(path: str, sentence: str):
    """ Execute a command in a SQLite database specified by db_file
    :param path: path to database file
    :param sentence: sentence
    """
    conn = create_sqlitle3_connection(path)
    cur = conn.cursor()
    try:
        cur.execute(sentence)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

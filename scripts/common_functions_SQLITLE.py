#!/usr/bin/env python3

import sqlite3


def create_sqlitle3_connection(db_file):
    """ Create a database connection to the SQLite database specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)

    return conn


@staticmethod
def get_values(path, sentence):
    """ Returns values from SQLite database specified by     db_file
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


@staticmethod
def execute(path, sentence):
    """ Execute a command in a SQLite database specified by db_file
    :param sentence: sentence
    """
    conn = create_sqlitle3_connection(path)
    cur = conn.cursor()
    try:
        cur.execute(sentence)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

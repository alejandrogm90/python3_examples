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

import pyfiglet


def print_mega_banner(text: str) -> None:
    """ Print a big banner

    :param text: text to print
    """
    print(pyfiglet.figlet_format(text))


def get_cpu_temperature() -> str:
    """ Return CPU temperature as a character string """
    res = os.popen('vcgencmd measure_temp').readline()
    return str(res.replace("temp=", "").replace("'C\n", ""))


def get_ram_info() -> str:
    """
    Return RAM information (unit=kb) in a list
    Index 0: total RAM
    Index 1: used RAM
    Index 2: free RAM
    """
    p = os.popen('free')
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i == 2:
            return str(line.split()[1:4])


def get_cpu_use() -> str:
    """ Return % of CPU used by user as a character string """
    return str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip())


def get_disk_space() -> str:
    """Return information about disk space as a list (unit included)
    Index 0: total disk space
    Index 1: used disk space
    Index 2: remaining disk space
    Index 3: percentage of disk used

    :return: disk space
    """
    p = os.popen("df -h /")
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i == 2:
            return str(line.split()[1:5])

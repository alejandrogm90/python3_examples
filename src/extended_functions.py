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


def get_cpu_temperature() -> str:
    """ Return CPU temperature as a character string """
    thermal_info = []
    # Leer todos los dispositivos de thermal_zone
    for zone in os.listdir('/sys/class/thermal'):
        if zone.startswith('thermal_zone'):
            type_path = os.path.join('/sys/class/thermal', zone, 'type')
            temp_path = os.path.join('/sys/class/thermal', zone, 'temp')

            # Comprobar si ambos archivos existen
            if os.path.exists(type_path) and os.path.exists(temp_path):
                with open(type_path, 'r') as type_file, open(temp_path, 'r') as temp_file:
                    thermal_type = type_file.read().strip()  # Tipos de temperatura
                    thermal_temp = temp_file.read().strip()  # Temperatura en miligrados
                    temp_celsius = f"{int(thermal_temp) / 1000:.1f}°C"  # Convertir a Celsius
                    thermal_info.append((thermal_type, temp_celsius))

    # Imprimir la información formateada
    return '\n'.join([f"{t}\t{c}" for t, c in thermal_info])

def get_cpu_use() -> str:
    """ Return % of CPU used by user as a character string """
    res = str(os.popen('lscpu | grep "MHz:"').readline()).strip().replace(' ', '')
    return res.split(':')[1]

def get_ram_info() -> list:
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
            return list(line.split()[1:4])

def get_disk_space() -> list:
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
            return list(line.split()[1:5])

def get_hostname():
    hostname = os.getenv('HOSTNAME')  # Obtiene la variable de entorno HOSTNAME
    if hostname is None:  # Si HOSTNAME no está definido
        hostname = os.uname().nodename  # Usa uname como respaldo
    return hostname

def print_full_hardware_info() -> None:
    # CPU information
    cpu_temp = get_cpu_temperature()
    cpu_usage = get_cpu_use()

    # RAM information
    # Output is in kb, here I convert it in Mb for readability
    ram_stats = get_ram_info()
    ram_total = str(round(int(ram_stats[0]) / 1000, 1))
    ram_used = str(round(int(ram_stats[1]) / 1000, 1))
    ram_free = str(round(int(ram_stats[2]) / 1000, 1))

    # Disk information
    disk_stats = get_disk_space()
    disk_total = disk_stats[0]
    disk_used = disk_stats[1]
    disk_perc = disk_stats[3]

    print('')
    print(f'HOSTNAME={get_hostname()}')
    print(f'CPU Temperature = {cpu_temp}')
    print(f'CPU Use = {cpu_usage}')
    print('')
    print(f'RAM Total = {ram_total} MB')
    print(f'RAM Used = {ram_used} MB')
    print(f'RAM Free = {ram_free} MB')
    print('')
    print(f'DISK Total Space = {disk_total} B')
    print(f'DISK Used Space = {disk_used} B')
    print(f'DISK Used Percentage = {disk_perc}')

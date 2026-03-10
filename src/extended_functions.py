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
import socket
import requests
from bs4 import BeautifulSoup


def local_ip():
    """ Return your local IP """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    respuesta = s.getsockname()[0]
    s.close()
    return respuesta

def global_ip() -> str:
    """ Return your global IP """
    response = requests.get('http://www.vermiip.es/')
    cad1 = ""
    # Verificar que la solicitud fue exitosa
    if response.status_code == 200:
        # Crear un objeto BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Buscar el objeto con id "ip"
        objeto = soup.find(id='ip')

        # Mostrar el contenido del objeto encontrado
        if objeto:
            cad1 = objeto.text
    return cad1

def get_cpu_temperature() -> str:
    """ Return CPU temperature as a character string """
    thermal_info = []
    for zone in os.listdir('/sys/class/thermal'):
        if zone.startswith('thermal_zone'):
            type_path = os.path.join('/sys/class/thermal', zone, 'type')
            temp_path = os.path.join('/sys/class/thermal', zone, 'temp')

            if os.path.exists(type_path) and os.path.exists(temp_path):
                with open(type_path, 'r') as type_file, open(temp_path, 'r') as temp_file:
                    thermal_type = type_file.read().strip()
                    thermal_temp = temp_file.read().strip()

                    # Comprobar que la temperatura no esté vacía
                    if thermal_temp:
                        temp_celsius = f"{int(thermal_temp) / 1000:.1f}°C"
                        thermal_info.append((thermal_type, temp_celsius))
                    else:
                        thermal_info.append((thermal_type, "N/A"))  # Manejo de temperatura vacía

    return '\n'.join([f"{t}\t{c}" for t, c in thermal_info]) if thermal_info else "No temperature data available"

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
            # Convertir cada elemento a tipo string
            return [value.decode('utf-8') for value in line.split()[1:4]]

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
            # Convertir cada elemento a tipo string
            return [value.decode('utf-8') for value in line.split()[1:5]]

def get_hostname() -> str:
    hostname = os.getenv('HOSTNAME')  # Obtiene la variable de entorno HOSTNAME
    if hostname is None:  # Si HOSTNAME no está definido
        hostname = os.uname().nodename  # Usa uname como respaldo
    return hostname

def get_full_info() -> dict:
    ram_stats = get_ram_info()
    disk_stats = get_disk_space()
    return {
        "hostname": get_hostname(),
        "local_ip": local_ip(),
        "global_ip": global_ip(),
        "cpu_temp": get_cpu_temperature(),
        "cpu_usage": get_cpu_use(),
        "ram_total": str(round(int(ram_stats[0]) / 1000, 1)),
        "ram_used": str(round(int(ram_stats[1]) / 1000, 1)),
        "ram_free": str(round(int(ram_stats[2]) / 1000, 1)),
        "disk_total": disk_stats[0],
        "disk_used": disk_stats[1],
        "disk_perc": disk_stats[3],
    }

def print_full_hardware_info() -> None:
    fi = get_full_info()

    print('')
    print(f'HOSTNAME: {fi.get("hostname")}')
    print(f'Local_IP: {fi.get("local_ip")}')
    print(f'Global_IP: {fi.get("global_ip")}')
    print('')
    print(f'CPU Temperature: {fi.get("cpu_temp")}')
    print(f'CPU Use: {fi.get("cpu_usage")}')
    print('')
    print(f'RAM Total: {fi.get("ram_total")} MB')
    print(f'RAM Used: {fi.get("ram_used")} MB')
    print(f'RAM Free: {fi.get("ram_free")} MB')
    print('')
    print(f'DISK Total Space: {fi.get("disk_total")} B')
    print(f'DISK Used Space: {fi.get("disk_used")} B')
    print(f'DISK Used Percentage: {fi.get("disk_perc")}')

def full_hardware_info_as_str() -> str:
    return str(get_full_info)

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
import time
import serial

# Settings for reading from Arduino Serial
SERIAL_PORT = "/dev/ttyACM0"
BAUD_RATE = 115200


def get_cpu_temperature():
    """ Return CPU temperature as a character string """
    res = os.popen('vcgencmd measure_temp').readline()
    return res.replace("temp=", "").replace("'C\n", "")


def get_cpu_use():
    """ Return % of CPU used by user as a character string """
    #return str(os.popen('top -n1 | grep "Cpu(s):"').readlines())
    res = str(os.popen('lscpu | grep "MHz:"').readline()).strip().replace(' ', '')
    return res.split(':')[1]


def get_ram_info():
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
            return line.split()[1:4]


def get_disk_space():
    """
    Return information about disk space as a list (unit included)
    Index 0: total disk space
    Index 1: used disk space
    Index 2: remaining disk space
    Index 3: percentage of disk used 
    """
    p = os.popen("df -h /")
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i == 2:
            return line.split()[1:5]


if __name__ == '__main__':
    if not os.path.exists(SERIAL_PORT):
        print(get_cpu_temperature())
        print(get_cpu_use())
        print(get_ram_info())
        print(get_disk_space())
        print("Arduino is not connected")
    else:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=0.5)
        time.sleep(2)

        # CPU information
        CPU_TEMP = get_cpu_temperature()
        CPU_USAGE = get_cpu_use()

        # RAM information - Output is in kb, here I convert it in Mb for readability
        RAM_stats = get_ram_info()
        RAM_total = str(round(int(RAM_stats[0]) / 1000, 1))
        RAM_used = str(round(int(RAM_stats[1]) / 1000, 1))
        RAM_free = str(round(int(RAM_stats[2]) / 1000, 1))

        # Disk information
        DISK_stats = get_disk_space()
        DISK_total = DISK_stats[0]
        DISK_used = DISK_stats[1]
        DISK_perc = DISK_stats[3]

        temp = ser.write(str.encode(f'{CPU_TEMP} {CPU_USAGE}'))

        data = ser.write(str.encode(
            CPU_TEMP + ':' + CPU_USAGE + ':' + RAM_total + ':' + RAM_used + ':' + RAM_free + ':' + DISK_total + ':' +
            DISK_used + ':' + DISK_perc))
        ser.flush()
        time.sleep(2)

        print('')
        print(f'CPU Temperature = {CPU_TEMP}')
        print(f'CPU Use = {CPU_USAGE}')
        print('')
        print('RAM Total = ' + str(RAM_total) + ' MB')
        print('RAM Used = ' + str(RAM_used) + ' MB')
        print('RAM Free = ' + str(RAM_free) + ' MB')
        print('')
        print('DISK Total Space = ' + str(DISK_total) + 'B')
        print('DISK Used Space = ' + str(DISK_used) + 'B')
        print('DISK Used Percentage = ' + str(DISK_perc))
        ser.close()

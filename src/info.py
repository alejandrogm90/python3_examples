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

from src.extended_functions import get_cpu_temperature, get_cpu_use, get_ram_info, get_disk_space

if __name__ == '__main__':
    # CPU information
    CPU_temp = get_cpu_temperature()
    CPU_usage = get_cpu_use()

    # RAM information
    # Output is in kb, here I convert it in Mb for readability
    RAM_stats = get_ram_info()
    RAM_total = str(round(int(RAM_stats[0]) / 1000, 1))
    RAM_used = str(round(int(RAM_stats[1]) / 1000, 1))
    RAM_free = str(round(int(RAM_stats[2]) / 1000, 1))

    # Disk information
    DISK_stats = get_disk_space()
    DISK_total = DISK_stats[0]
    DISK_used = DISK_stats[1]
    DISK_perc = DISK_stats[3]

    print('')
    print('CPU Temperature = ' + CPU_temp)
    print('CPU Use = ' + CPU_usage)
    print('')
    print('RAM Total = ' + str(RAM_total) + ' MB')
    print('RAM Used = ' + str(RAM_used) + ' MB')
    print('RAM Free = ' + str(RAM_free) + ' MB')
    print('')
    print('DISK Total Space = ' + str(DISK_total) + 'B')
    print('DISK Used Space = ' + str(DISK_used) + 'B')
    print('DISK Used Percentage = ' + str(DISK_perc))

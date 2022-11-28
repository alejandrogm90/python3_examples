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
serialPort = "/dev/ttyACM0"  # Change it to your Serial Port, Check in Arudino IDE
baudRate = 115200
ser = serial.Serial(serialPort, baudRate, timeout=0.5)
time.sleep(2)


def getCPUtemperature():
    """ Return CPU temperature as a character string """
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=", "").replace("'C\n", ""))


def getRAMinfo():
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
            return(line.split()[1:4])


def getCPUuse():
    """ Return % of CPU used by user as a character string """
    return(str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip()))


def getDiskSpace():
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
            return(line.split()[1:5])


if __name__ == '__main__':
    try:
        while True:
            # CPU informatiom
            CPU_temp = getCPUtemperature()
            CPU_usage = getCPUuse()

            # RAM information
            # Output is in kb, here I convert it in Mb for readability
            RAM_stats = getRAMinfo()
            RAM_total = str(round(int(RAM_stats[0]) / 1000, 1))
            RAM_used = str(round(int(RAM_stats[1]) / 1000, 1))
            RAM_free = str(round(int(RAM_stats[2]) / 1000, 1))

            # Disk information
            DISK_stats = getDiskSpace()
            DISK_total = DISK_stats[0]
            DISK_used = DISK_stats[1]
            DISK_perc = DISK_stats[3]

            temp = ser.write(str.encode(CPU_temp+' '+CPU_usage))

            data = ser.write(str.encode(CPU_temp+':'+CPU_usage+':'+RAM_total+':' +
                            RAM_used+':'+RAM_free+':'+DISK_total+':'+DISK_used+':'+DISK_perc))
            ser.flush()
            time.sleep(2)

            print('')
            print('CPU Temperature = '+CPU_temp)
            print('CPU Use = '+CPU_usage)
            print('')
            print('RAM Total = '+str(RAM_total)+' MB')
            print('RAM Used = '+str(RAM_used)+' MB')
            print('RAM Free = '+str(RAM_free)+' MB')
            print('')
            print('DISK Total Space = '+str(DISK_total)+'B')
            print('DISK Used Space = '+str(DISK_used)+'B')
            print('DISK Used Percentage = '+str(DISK_perc))

    except KeyboardInterrupt:
        if ser != None:
            ser.close()

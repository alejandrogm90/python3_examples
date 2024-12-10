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

import socket
import sys
import urllib.request


def local_ip():
    """ Return your local IP """
    respuesta = ""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    respuesta = s.getsockname()[0]
    s.close()
    return respuesta


def global_ip():
    """ Return your global IP """
    response = urllib.request.urlopen('http://www.vermiip.es/')
    html = response.read()
    cad1 = str(html)
    cad1 = cad1.split('id="cuerpo"')[1]
    cad1 = cad1.split('h2')[1]
    cad1 = cad1.split(' ')[4].split('<')[0]
    return cad1


if __name__ == '__main__':
    if len(sys.argv) >= 2:
        if sys.argv[1] == "-l" or sys.argv[1] == "--local":
            print(f'Local_IP: {local_ip()}')
        elif sys.argv[1] == "-g" or sys.argv[1] == "--global":
            print(f'Global_IP: {global_ip()}')
        else:
            print("ERROR:")
            print(sys.argv[0] + " -l or --local #LOCAL IP")
            print(sys.argv[0] + " -g or --global #GLOBAL IP")
            print(sys.argv[0] + " #GLOBAL IP")
    else:
        print(f'Local_IP: {local_ip()}')
        print(f'Global_IP: {global_ip()}')

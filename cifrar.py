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

import sys
import hashlib

def enMD5(cad1):
    token = hashlib.md5()
    token.update(cad1.encode('utf-8'))
    pass1 = token.hexdigest()
    return pass1

def enSHA1(cad1):
    token = hashlib.sha1()
    token.update(cad1.encode('utf-8'))
    pass1 = token.hexdigest()
    return pass1

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print("En MD5: "+enMD5(sys.argv[1]))
        print("En SHA1: "+enSHA1(sys.argv[1]))
    else:
        print("A parameter is required")

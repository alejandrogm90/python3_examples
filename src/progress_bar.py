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

import time

REFRES_TIME = 0.2
BAR_LEN = 24
elements = ['-','\\','|','/']

for i in range(BAR_LEN+1):
    frame = i % len(elements)
    # print(f'\r[{elements[frame]*i}]', end="")
    #  Normal
    print(f'\r[{elements[frame]*i:=<{BAR_LEN}}]', end="")
    # Desde atrás
    # print(f'\r[{elements[frame]*i:=>{BAR_LEN}}]', end="")
    # Desde el centro
    # print(f'\r[{elements[frame]*i:=^{BAR_LEN}}]', end="")
    time.sleep(REFRES_TIME)
print()

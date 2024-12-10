#!/usr/bin/env python3
#
#
#       Copyright 2024 Alejandro Gomez
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

if __name__ == '__main__':
    final_list = []

    if not sys.stdin.isatty():
        # use stdin if it's full
        input_stream = sys.stdin
    else:
        # otherwise, read the given file name
        try:
            input_file_name = sys.argv[1]
        except IndexError:
            raise IndexError('A file name is need as first parameter')
        # Load file in input_stream
        input_stream = open(input_file_name, 'r')

    for line in input_stream:
        c_line = str(line.split("\n")[0]).strip()
        if c_line != "" and c_line not in final_list:
            final_list.append(c_line)

    # Sort data
    final_list.reverse()

    for line in final_list:
        print(line)

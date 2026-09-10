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

import datetime
from datetime import date


select_date = '2019-12-24'
d1 = date.fromisoformat(select_date)
print(f'Date d1 ({select_date}) in date format: {d1}')

d2 = date(d1.year, d1.month, d1.day + 3)
print(f'Date d2 from d1 ({select_date}) + 3 days: {d2}')

d3 = d2 + datetime.timedelta(days=10)
print(f'Date dd3 from d2 ({d2}) + 10 days: {d3}')

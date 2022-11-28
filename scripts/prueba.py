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

import logging
import logging.config
import datetime
import random
import commonFunctions as cf
import sys

# GLOBALS
logging.config.fileConfig('~/bin/logging.conf')
LOGGER = logging.getLogger('testLogger')
today = datetime.date.today()

# Add Banner
cf.printMegaBanner(cf.getFiletName(sys.argv[0],True))
textList = list()
textList.append('La fecha actual en formato datetime : '+str(datetime.datetime.now()))
textList.append('La fecha actual en formato ctime : '+today.ctime())
cf.printBanner(".", textList)

w = list()
for i in range(100):
    w.append(random.uniform(0,1))

print(w)

cf.errorMsg(LOGGER,1,"ERROR a drede")
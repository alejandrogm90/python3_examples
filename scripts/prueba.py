#!/usr/bin/env python3

import datetime
import random

today = datetime.date.today()

print('La fecha actual es : '+str(datetime.datetime.now()))
print('La fecha actual es : '+today.ctime())

w = list()
for i in range(100):
    w.append(random.uniform(0,1))

print(w)

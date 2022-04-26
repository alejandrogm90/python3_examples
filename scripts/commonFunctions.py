#!/usr/bin/env python3

from calendar import monthrange

def isDate(cadena):
    if len(cadena) != 10:
        return False
        
    if cadena[4] != "-" or cadena[7] != "-":
        return False

    try:
        anno = int(cadena[0:4])
        mes = int(cadena[5:7])
        dia = int(cadena[8:10])
    except:
        return False

    if mes > 12 or mes < 1:
        return False

    if anno < mes or anno < dia:
        return False

    if dia > monthrange(anno, mes)[1] or dia < 1:
        return False

    return True

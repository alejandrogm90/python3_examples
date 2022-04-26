#!/usr/bin/env python3

def isDate(cadena):
    if len(cadena) != 10:
        print("10")
        return False
        
    if cadena[4] != "-" or cadena[7] != "-":
        print("-")
        return False

    try:
        anno = int(cadena[0:4])
        mes = int(cadena[5:7])
        dia = int(cadena[8:10])
    except:
        return False

    if dia > 31 or dia <= 0:
        return False

    if mes > 12 or mes <= 0:
        return False

    if anno < mes or anno < dia:
        return False

    return True

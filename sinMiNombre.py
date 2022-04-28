#!/usr/bin/env python3

import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Número de parámetros erroneo.")
        sys.exit(1)
    else:
        trozos = sys.argv[1].split("/")
        if len(trozos) <= 1:
            print("La cadena enviada es erronea erroneo.")
            sys.exit(2)
        else:
            CADENA_NUEVA = ""
            for parte in range(len(trozos)-1):
                CADENA_NUEVA = CADENA_NUEVA + trozos[parte] + "/"
            print(CADENA_NUEVA)

#!/usr/bin/env python3

def cambiarLinea(linea):
    nueva = ""
    for pos in range(0,len(linea)-1):
        """
        l2 = re.findall('[a-zA-Z0-9]*', linea[pos])
        if (l2[0] != ''):
            nueva = nueva + str(chr(ord(linea[pos])+1))
        else:
            nueva = nueva + linea[pos]
        """
        nueva = nueva + str(chr(ord(linea[pos])+1))
    return nueva


def procesarFichero(nombre):
    f1 = open(nombre,'r')
    linea = f1.readline()
    while (len(linea) > 0):
        print(cambiarLinea(linea))
        linea = f1.readline()

if __name__ == "__main__":
    procesarFichero('/opt/COMPARTIDA/PROYECTOS/myBin/bin/calculadora.py')
    
    


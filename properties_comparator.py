#!/usr/bin/env python3

from asyncio.windows_events import NULL
import sys

DELIMITER = '='


def show_error(num, text):
    print(text)
    sys.exit(num)


class propertiesFile():
    def __init__(self, location):
        self.file_location = location
        self.propiedades = list()
        current_file = open(self.file_location, 'r', encoding="utf-8")
        line = current_file.readline()
        while line:
            propiedad = self.esPropiedad(line)
            if propiedad != NULL:
                self.propiedades.append(propiedad)
            line = current_file.readline()

    def getNumPropiedades(self):
        return len(self.propiedades)

    def getPropiedades(self):
        return self.propiedades

    def getPropiedad(self, indice):
        for propiedad in self.propiedades:
            if indice == propiedad[0]:
                return propiedad
        return NULL

    def esPropiedad(self, line):
        if line[0] != ' ' and "=" in line:
            partes = line.split("=")
            # if partes[0] != "":
            print("---- PARTES:  "+partes[1])
            if partes[0] != "":
                return partes
        return NULL

    def existePropiedad(self, propiedad):
        resultado = ""
        for propiedadActual in self.propiedades:
            if propiedad == propiedadActual[0]:
                return True
        return False

    def contiene(self, fichero):
        numPropiNoExisten = 0
        for propiedadActual in self.propiedades:
            if not fichero.existePropiedad(propiedadActual[0]):
                print("[WARN] No existe: "+propiedadActual[0])
                numPropiNoExisten = numPropiNoExisten + 1
        if numPropiNoExisten > 0:
            print("[ERROR] Faltan "+str(numPropiNoExisten)+" propiedades")
        else:
            print("[MSG] Contiene todas las propiedades")

    def contiene2(self, fichero):
        numPropiNoExisten = 0
        for propiedadActual in self.propiedades:
            exitste = ""
            for propiedadOtro in fichero.getPropiedades():
                if propiedadOtro[0] == propiedadActual[0]:
                    exitste = "si"
                    break
            if exitste == "":
                print("[WARN] No existe: "+propiedadActual[0])
                numPropiNoExisten = numPropiNoExisten + 1
        if numPropiNoExisten > 0:
            print("[ERROR] Faltan "+str(numPropiNoExisten)+" propiedades")
        else:
            print("[MSG] Contiene todas las propiedades")


if __name__ == '__main__':
    if len(sys.argv) != 3:
        show_error(1, "ERROR:\n" + sys.argv[0] + " fichero1.csv fichero2.csv")

    FIRST_FILE = propertiesFile(sys.argv[1])
    SECOND_FILE = propertiesFile(sys.argv[2])

    FIRST_FILE.contiene(SECOND_FILE)
    print(str(FIRST_FILE.getNumPropiedades())+" - "+str(SECOND_FILE.getNumPropiedades()) +
          " = " + str(FIRST_FILE.getNumPropiedades() - SECOND_FILE.getNumPropiedades()))

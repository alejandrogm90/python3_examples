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


import sys
from email.mime.text import MIMEText
from smtplib import SMTP
 
if __name__ == "__main__" and len(sys.argv) == 2:
    correo = "FROM MAIL"
    destinatario = "TO MAIL"
    print(correo)
    try:
        fo = open(sys.argv[1], "r+")
        mensaje = fo.read()
        fo.close()
    except:
        print("Error al leer el fichero")
        exit(1)
    
    mime_mensaje = MIMEText(mensaje)
    mime_mensaje["From"] = correo[0]
    mime_mensaje["To"] = destinatario
    mime_mensaje["Content-type"] = "text/html" 
    mime_mensaje["Subject"] = "INFO"

    server = SMTP(correo[2], int(correo[3]))
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(correo[0], correo[1])
    server.sendmail(correo[0], destinatario, mime_mensaje.as_string())
    server.quit()
else:
    print("Faltan parámetros")

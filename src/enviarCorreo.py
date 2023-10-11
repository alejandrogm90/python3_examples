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
import common_functions as cf


def send_mail(file: str, sender: str, sender_pass: str, destiny: str, server_name: str, server_port: int):
    mime_message = MIMEText(file)
    mime_message["From"] = sender
    mime_message["To"] = destiny
    mime_message["Content-type"] = "text/html"
    mime_message["Subject"] = "INFO"

    server = SMTP(server_name, server_port)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(sender, sender_pass)
    server.sendmail(sender, destiny, mime_message.as_string())
    server.quit()


if __name__ == "__main__":
    if len(sys.argv) == 7:
        try:
            fo = open(sys.argv[1], "r+")
            message_text = fo.read()
            fo.close()

            send_mail(message_text, sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], int(sys.argv[6]))
        except:
            cf.error_msg(2, "Error reading file")
    else:
        cf.info_msg("file_path: str, sender_email: str, sender_pass: str, destiny_email: str, server: str, port: int")
        cf.error_msg(1, "Wrong parameters")

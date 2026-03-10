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
import smtplib

import common_functions as cf

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_mail(body: str, sender_email: str, password: str, receiver_email: str, server_name: str, server_port: int):
    try:
        # Create a multipart email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = "INFO"
        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP(server_name, server_port) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, password)  # Login to the server
            server.sendmail(sender_email, receiver_email, msg.as_string())  # Send the email
            print("Email sent successfully!")
    except smtplib.SMTPAuthenticationError:
        cf.error_msg(6, "Error: Authentication failed. Check your credentials.")
    except smtplib.SMTPConnectError:
        cf.error_msg(7, "Error: Could not connect to the SMTP server. Please check the server address and port.")
    except smtplib.SMTPRecipientsRefused:
        cf.error_msg(8, "Error: The recipient's address was refused by the server.")
    except smtplib.SMTPDataError:
        cf.error_msg(9, "Error: The SMTP server responded with an error to the data.")
    except Exception as e:
        cf.error_msg(10, f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) == 7:
        message_text = ""
        file_path = sys.argv[1]
        try:
            fo = open(file_path, "r+")
            message_text = fo.read()
            fo.close()
        except FileNotFoundError:
            cf.error_msg(2, f"Error: The file '{file_path}' does not exist.")
        except PermissionError:
            cf.error_msg(3, f"Error: You do not have permission to access '{file_path}'.")
        except IsADirectoryError:
            cf.error_msg(4, f"Error: '{file_path}' is a directory, not a file.")
        except Exception as e:
            cf.error_msg(5, f"An unexpected error occurred: {e}")

        send_mail(message_text, sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], int(sys.argv[6]))
    else:
        cf.info_msg("file_path: str, sender_email: str, sender_pass: str, destiny_email: str, server: str, port: int")
        cf.error_msg(1, "Wrong parameters")

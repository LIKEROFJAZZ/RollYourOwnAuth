

import os
#from dotenv import dotenv_values
import sqlite3
import re
import random
import ssl
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def email_check(email):
    regex = "(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
    if re.search(regex, email):
        return True
    else:
        return False

message_content = input("enter email: ")

        # the message is an email address - NEEDED
if email_check(message_content):
    if "@jazzsucks.ca" in message_content:
        # generate verification code - NEEDED
        verification_code = random.randint(100000, 999999)
        print("this is valid", verification_code)
else:
    print("not valid")

auth_submit = input("input the sent verification code: ")
if (len(auth_submit) == 6) and auth_submit.isdigit():
    if verification_code == int(auth_submit):
        print("you in")
    else:
        print("wrong code")

else:
    print("not a valid code")

'''
@version: Python 3.7.3
@Author: Louis
@Date: 2020-06-15 13:27:40
LastEditors: Louis
LastEditTime: 2020-08-18 15:00:02
'''
import os
from datetime import datetime
from email.mime.text import MIMEText
import smtplib

from .txx_consts import TODAY
from .txx_datetime import parse_date_in_str
from .txx_keyrings import peek_password


def simple_email(from_='txx@innoam.com', 
                 to_='txx@innoam.com',
                 server='smtp.exmail.qq.com',
                 user='Louis',
                 password=None,
                 file_path="/tmp/log/%Y%m%d.log"):
    """ Send a email with one attach (for log sending) """
    password = peek_password("txx", "email") if not password else password
    log_file = parse_date_in_str(file_path, TODAY)
    if not os.path.isfile(log_file):
        msg = MIMEText(f"No log file of {TODAY}")
        msg["Subject"] = f"NO LOG {TODAY}"
    else:
        with open(log_file, "r", encoding="utf8") as fp:
            msg = MIMEText(fp.read())
        msg["Subject"] = f"Log {TODAY}"
    msg["From"] = from_
    msg["To"] = to_

    server = smtplib.SMTP(server)
    server.login(user, password)
    server.sendmail(from_, [to_], msg.as_string())
    server.quit()

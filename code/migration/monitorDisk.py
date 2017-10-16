# !/usr/local/bin

' if disk usage reached,send email to managers '

import os
import smtplib
import ini
from email.mime.text import MIMEText
from email.header import Header
import datetime


def diskUsage():
    'get disk usage'
    disk = os.statvfs(ini.disk_path)
    return (disk.f_blocks - disk.f_bfree) * 100 / (disk.f_blocks - disk.f_bfree + disk.f_bavail) + 1


def sendEmail():
    'sen email'
    # email content
    msg = MIMEText('Hard disk occupancy rate reached the upper limit!', 'plain', 'utf-8')
    msg['From'] = Header(ini.from_mail, 'utf-8')
    msg['To'] = Header(ini.to_mail, 'utf-8')
    msg['Subject'] = Header('RTMP hard disk warning', 'utf-8')
    # send
    server = smtplib.SMTP_SSL(ini.mail_host, ini.mail_port)
    server.set_debuglevel(1)
    server.login(ini.from_mail, ini.from_password)
    server.sendmail(ini.from_mail, ini.to_mail.split(';'), msg.as_string())
    server.quit()


# main
try:
    if diskUsage() >= int(ini.warning_value):
        sendEmail()
        ini.writeLog(str(datetime.datetime.now()) + '---send email success--' + ini.to_mail, ini.log + 'mail/')
except Exception, e:
    ini.writeLog(str(datetime.datetime.now()) + 'send warning email error--' + str(e), ini.log + 'mail/')

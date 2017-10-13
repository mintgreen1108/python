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
    msg = MIMEText('waring!!!', 'plain', 'utf-8')
    msg['From'] = Header(ini.from_mail, 'utf-8')
    msg['To'] = Header(ini.to_mail, 'utf-8')
    msg['Subject'] = Header('disk warning', 'utf-8')
    # send
    server = smtplib.SMTP(ini.mail_host, ini.mail_port)
    server.set_debuglevel(1)
    server.login(ini.from_name, ini.from_password)
    server.sendmail(ini.from_mail, [ini.to_mail], msg.as_string())
    server.quit()


# main
try:
    if diskUsage() >= int(ini.warning_value):
        sendEmail()
        print 'complete'
        ini.writeLog('send email success--' + ini.to_mail + '---' + str(datetime.datetime.now()))
except Exception, e:
    print 'exception'
    ini.writeLog('send warning email error--' + str(e) + str(datetime.datetime.now()), ini.log + 'mail/')

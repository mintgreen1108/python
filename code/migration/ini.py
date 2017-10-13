# !/usr/local/bin

'read config information'

import ConfigParser
import datetime
import os

cf = ConfigParser.ConfigParser()
cf.read('config.conf')

# get ini config

src = cf.get('dictionary', 'src_path')
dst = cf.get('dictionary', 'dst_path')
log = cf.get('dictionary', 'log_path')

deletDate = cf.get('delete', 'date')

to_mail = cf.get('mail', 'to1')
from_mail = cf.get('mail', 'from_mail')
from_name = cf.get('mail', 'from_name')
from_password = cf.get('mail', 'from_password')
mail_host = cf.get('mail', 'mail_host')
mail_port = cf.get('mail', 'mail_port')

disk_path = cf.get('disk', 'mounted_path')
warning_value = cf.get('disk', 'warning_value')


def writeLog(content, logPath):
    'write move file exception'
    checkPath(logPath)
    fobj = open(logPath + str(datetime.date.today()) + ".log", 'a')
    fobj.writelines(['%s \n' % content])
    fobj.close()


def checkPath(path):
    'if path not found,create'
    if not os.path.exists(path):
        os.makedirs(path, 7777)

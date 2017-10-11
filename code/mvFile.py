# !/usr/local/bin python

'copy file from source to destination'

import os
import shutil
import datetime

src = '/var/www/python_file/'
dst = '/var/www/python_file3/'
logPath = '/var/www/python_file/'


def writeLog(content):
    fobj = open(logPath + str(datetime.date.today()) + ".log", 'a')
    fobj.writelines(['%s \n' % content])
    fobj.close()


# copy files
try:
    files = os.listdir(src)
    for file in files:
        if ((datetime.date.fromtimestamp(os.stat(src + file).st_ctime) - datetime.date.today()).days is 0):
            shutil.move(src + file, dst + file)
except Exception, e:
    writeLog('move file error--' + str(e))

print 'complete'

# !/usr/local/bin python

'copy file from source to destination'

import os
import shutil
import datetime

src = '/datas/rtmp-server/video/'
dst = '/tmp/rtmp-server/video/'
logPath = '/datas/rtmp-server/'


def writeLog(content):
    'write move file exception'
    fobj = open(logPath + str(datetime.date.today()) + ".log", 'a')
    fobj.writelines(['%s \n' % content])
    fobj.close()


def checkPath(path):
    'if path not found,create'
    if not os.path.exists(path):
        os.makedirs(path, 7777)


# move files
try:
    checkPath(dst)
    dicts = os.listdir(src)
    for dict in dicts:
        # source dictionary
        spath = src + dict + '/'
        # destination dictionary
        dpath = dst + dict + '/'
        files = os.listdir(spath)
        for file in files:
            if ((datetime.date.today() - datetime.date.fromtimestamp(os.stat(spath + file).st_ctime)).days > 7):
                checkPath(dpath)
                shutil.move(spath + file, dpath + file)
except Exception, e:
    writeLog('move file error--' + str(e))

print 'complete'

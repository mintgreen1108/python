# !/usr/local/bin python

'copy file from source to destination'

import os
import shutil
import datetime
import ini

# move files
ini.writeLog(str(datetime.datetime.now()) + '---move file---', ini.log + 'mvFile/info/')
try:
    ini.checkPath(ini.dst)
    dicts = os.listdir(ini.src)
    # find dictionary
    for dict in dicts:
        # source dictionary
        spath = ini.src + dict + '/'
        # destination dictionary
        dpath = ini.dst + dict + '/'
        files = os.listdir(spath)

        # find file
        for file in files:
            subDays = (datetime.date.today() - datetime.date.fromtimestamp(os.stat(spath + file).st_ctime)).days

            # if subDays > int(ini.deletDate):
            # os.remove(spath + file)
            if subDays > 7:
                ini.checkPath(dpath)
                shutil.move(spath + file, dpath + file)

except Exception, e:  # No space left on device
    ini.writeLog(str(datetime.datetime.now()) + '---move file error---' + str(e), ini.log + 'mvFile/error/')

ini.writeLog(str(datetime.datetime.now()) + '---move file---', ini.log + 'mvFile/info/')

print 'complete'

# !/usr/local/bin python2.7

'read and display file text'

import os

fname=raw_input('enter want read file name:')

try:
    fname=open(fname,'r')
    for line in fname:
        print line
    fname.close()
except IOError,e:
    print 'open file error:',e
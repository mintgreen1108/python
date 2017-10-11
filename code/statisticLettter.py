# !/usr/local/bin  python2.7

'statisticLetter.py--count text file letter'

import os
import string

fname=raw_input('enter file name:')
letter=raw_input('enter letter:')

try:
    fobj = open(fname, 'r')

    fobj.close()
except IOError,e:
    print 'open file error:',e

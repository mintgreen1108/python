# !/usr/local/bin  python2.7

'statisticLetter.py--count text file letter'

import os
import string

fname=raw_input('enter want read file name:')
letters=string.letters
result=[]

try:
    fname=open(fname,'r')
    print str(fname)
    fname.close()
except IOError,e:
    print 'open file error:',e
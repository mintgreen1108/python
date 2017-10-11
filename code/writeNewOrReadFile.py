# !/usr/local/bin python2.7

'read and display file text'

import os

ls=os.linesep

fname = raw_input('enter want read file name:')

action = raw_input('enter action w/r:')


def read(fname):
    try:
        fname = open(fname, 'r')
        for line in fname:
            print line
        fname.close()
    except IOError, e:
        print 'open file error:', e


def write(fname):
    while True:
        if os.path.exists(fname):
            print 'file already existed'
        else:
            break

    all = []
    print 'enter text'

    while True:
        entry = raw_input('> ')
        if entry == '.':
            break
        else:
            all.append(entry)

    file = open(fname, 'w')

    file.writelines(['%s %s' % (x, ls) for x in all])

    file.close()

    print 'complete'

if action == 'w':
    write(fname)
elif action == 'r':
    read(fname)
else:
    print 'enter action error'

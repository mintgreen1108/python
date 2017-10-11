# !usr/local/bin python2.7

"create a new text file and write"

import os

ls=os.linesep

fname=raw_input('enter file name:')

while True:
    if os.path.exists(fname):
        print 'file already existed'
    else:
        break

all=[]
print 'enter text'

while True:
    entry=raw_input('> ')
    if entry=='.':
        break
    else:
        all.append(entry)

file=open(fname,'w')

file.writelines(['%s %s'%(x,ls) for x in all])

file.close()

print 'complete'
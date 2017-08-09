# -*- coding: utf-8 -*-

#BE 00

from sys import argv
from os.path import exists

script,from_file,to_file = argv

print "Copying from %s to %s" % (from_file,to_file)

# we could do these two on one line too,how?

indata = open(from_file).read()

#in_file = open(from_file)
#indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

if exists(to_file) != 1:
    print(" Sorry,the input file is not exists ")
else:

    out_file = open(to_file,'w')
    out_file.write(indata)

    print "Alrigt,all done."

    out_file.close()
    open(from_file).close()

# DK

# 01 研究import

# 02 改写脚本,使其更友好:没必要复制前提示,没必要输出那么多内容

# 03 改短

# 04 cat 的作用:man cat

# 05 为什么要写 output.close()?

    # read() 可以自动 close, 但是 write()不可以


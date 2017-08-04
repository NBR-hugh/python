# -*- coding:utf-8 -*-

# BE 00
from sys import argv     # import：将python特性引入脚本的方法，特性的真正名称：模块（module)/库（library）

script,first,second,third = argv    # argv 即参数变量（argumengt variable）；把argv中的东西解包，将所有参数依次赋值给左边的变量;定义有效地参数输入形式

name = raw_input("what's your name?")

print "The script is called:",script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "your name is",name

# python ex13.py 1 2 3


# DK 

# 01 错误信息:
    #ValueError: need more than 3 values to unpack
    #这是变量定义时的形式决定的

# 02 更多/更少的参数脚本

# 更少
#    script,first,second = argv 

#    print "The script is called:",script
#    print "Your first variable is:", first
#    print "Your second variable is:", second


# 更多
#   script,first,second,third,fourth = argv 

#   print "The script is called:",script
#   print "Your first variable is:", first
#   print "Your second variable is:", second
#   print "Your third variable is:", third
#   print "Your fourth variable is:", fourth


# 03 混用 argv 与 raw_input():如上

    # raw_input("what's your name?")

# -*- coding:utf-8 -*-

# BE 00


print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weight?",
weight = raw_input()

print "So,you're %r old, %r tall and %r heavy. " % (
      age,height,weight)


# DK

# 01 raw_input() 实现什么功能?:
    # 接受用户输入信息

# 02 raw_input() 别的用法?
try_demo = raw_input("How old are you?")
print try_demo

# 03 仿写

print "when are you come here?",
book = raw_input()
print "How long have you stay here?",
time = raw_input()

print "So, the time is %r,and you stay here %r." % (
      book,time)

# 04 '6\'2"' :字符串内有\,'','"" 都要\转义,以防识别错误
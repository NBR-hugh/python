# -*- coding: utf-8 -*-

## BE 00

people = 20
cats =30
dogs = 15

if people < cats:
    print "Too many cats! The world is doomed!"

if people > cats:
    print "Not many cats! The world is saved."

if people < dogs:
    print "The world is drooled on!"

if people > dogs:
    print"The world is dry!"

dogs += 5

if people >= dogs:
    print "people are greater than or equal to dogs."

if people <= dogs:
    print "people are less than or equal to dogs."

if people == dogs:
    print "people are dogs."


# DK

# 01 if 对其下一行代码做什么?
    #结果为真则运行,为假则跳过

# 02 为什么 if 语句下一行需要4 个空格的缩进?
    # python 的语法要求,表示从属于该 if

# 03 不缩进会怎么样?
    # 报错 缩进错误

# 04 任何布尔表达式都行,只要有 真 or 假 输出就可以.

# 05 初始值改变,判定结果就可能变化, print 出来的结果也就不同. 

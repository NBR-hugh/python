# -*- coding: utf-8 -*-

## ex38 列表的操作

# BE 00

ten_things = "Apples Orange Crows Telephone Light Suger"

print "Wait there's not 10 things in that list,let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day","Night","Song","Frisbee","Corn","Banana","Girl","Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding:",next_one
    stuff.append(next_one)
    print "There's %d iterms now." % len(stuff)

print "There we go: ",stuff

print "Let's do some things with stuff."

print stuff[1]   pytjon
print stuff[-1] # whoa! fancy
print stuff.pop()
print ' '.join(stuff) # what?cool!
print '#'.join(stuff[3:5]) # super stellar


#DK

# 01 
#   将字符串 ten_things 用 " "分开
#   将列表 stuff 中的元素用 ' ' 连接起来
#   将列表 stuff 中的3位到5位的元素(包含3位,不包含5位) 用'#'连接起来

# 03 面向对象编程
    # - 分装
    # - 继承
    # - 多态

    把一组数据结构和处理它们的方法组成对象,

# 04 python class 是什么?
# 类（Class）：定义了一件事物的抽象特点。类的定义包含了数据的形式以及对数据的操作。

# 05 dir(something)
     # the default dir() logic is used and returns:
     #      for a module object: the module's attributes.
     #      for a class object:  its attributes, and recursively the attributes
     #        of its bases.
     #      for any other object: its attributes, its class's attributes, and
     #        recursively the attributes of its class's base classes.

# 06 函数式编程(function progming)

     # 函数式编程（英语：functional programming）或称函数程序设计，又称泛函编程，是一种编程范型，
     # 它将电脑运算视为数学上的函数计算，并且避免使用程序状态以及易变对象。
     # 函数编程语言最重要的基础是λ演算（lambda calculus）。而且λ演算的函数可以接受函数
     # 当作输入（引数）和输出（传出值）。

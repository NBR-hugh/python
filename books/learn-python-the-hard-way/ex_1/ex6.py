# -*- coding:utf-8 -*-

# BE 00

#赋予各个变量不同的值,值为""内的字符串
x = "There are %d types of people." % 10     
binary = "binary"                            
do_not = "don't"
y = "Those who know %s and those who %s." % (binary,do_not)
# 打印 变量x,y 的值
print x
print y
# 将变量以格式化字符串形式打印出来
print "I said: %r." % x
print "I also said: '%s'." % y
#变量赋值
hilarious = False
joke_evaluation = "Isn't that jokes so funny?! %r"
# 将变量以格式化字符串形式打印出来
print joke_evaluation % hilarious
# 变量赋值
w = "This is the left side of..."
e = "a string with a right side."
# 变量赋值,值得类型为字符串,可以通过+连接打印出来
print w + e


# DK
# 01 注释作用

# 02 找到所有"把一个字符串放进另一个字符串的地方"
y = "Those who know %s and those who %s." % (binary,do_not)
print "I said: %r." % x
print "I also said: '%s'." % y
print joke_evaluation % hilarious

# 03 如何得知02的答案:先看%符号, s%,r% 或者% 变量名均满足要求

# 04 为什么 w+e 就可以生成一个更长的字符串?:w 和 e都是字符串,用+连接变可生成更长的字符串,若是数字便是加法运算的结果. 

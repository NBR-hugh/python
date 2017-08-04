# -*- coding:utf-8 -*-


# BE 00

name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He is %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that not too heavy."
print "He's got %s eyes and %s hair." % (eyes,hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is  tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
     age, height, weight, age + height + weight )

#DK

#01:修改变量名,去掉 my_,如上

#02:试着使用更多的格式化符号:s% 显示字符串,%d 显示数字,%r 显示任何字符

#03:搜索所有的 py 格式化字符(format string)
    #- 使用%操作符。2.6版以后提供了format方法

#04:变量将英寸和磅转化成厘米和千克

print "单位换算:1英寸（in）=2.54厘米（cm）,1磅（lb）=0.454千克（kg）"

in0 = 10
lb0 = 10
cm0 = in0 * 2.54
kg0 = lb0 * 0.454

print cm0,kg0 




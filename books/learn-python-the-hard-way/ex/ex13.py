# -*- coding: utf-8 -*-

from sys import argv     # import：将python特性引入脚本的方法，特性的真正名称：模块（module），也有人称为“库”（library）

script,first,second,third = argv    # argv 即参数变量（argumengt variable）；把argv中的东西解包，将所有参数依次赋值给左边的变量

print "The script is called:",script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third


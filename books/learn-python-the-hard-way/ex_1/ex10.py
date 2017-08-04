# -*- coding:utf-8 -*-

# BE 00

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll ao a list:
\t* cat food
\t* FIshises
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat


#DK 

# 02 什么时候用''',不用""":
    #当字符串中含有""

# 03 将转义字符和格式化字符串组合在一起,创建一种更复杂的形式:
try_cat = "I'm \\ a \\ %s cat." % ("blue")
print try_cat

# 04 %s 与 %r 的区别:
    #前者是用户看到的东西,后者是程序员写在脚本里的东西,利于调试

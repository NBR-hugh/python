# -*- coding:utf-8 -*-

# BE 00

# 将四个格式化字符(字符串)赋予变量 'fomatter'
fomatter = "%r %r %r %r"
# 给变量'fomatter'的4个格式化字符填充内容:数字,单词,布尔值,长句
print fomatter % (1,2,3,4)
print fomatter % ("one","two","three","four")
print fomatter % (True,False,False,True)
print fomatter % (fomatter,fomatter,fomatter,fomatter)
print fomatter % (
                  "I had this thing.",
                  "That you could tpye up right.",
                  "But it didn't sing.",
                  "So I said goodnight."
)

#DK 
#01 记录错误

#02输出结果既有""又有'',它是如何工作的?:默认添加的引号为'',但当字符串中有"",那么外围的引号便是''以区别
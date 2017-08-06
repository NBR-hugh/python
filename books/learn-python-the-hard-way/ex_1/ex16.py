# -*- coding: utf-8 -*-

#BE 00

from  sys import argv
# 定义参数
script,filename = argv   
# 打印引导语
print "We're going to erase %r." % filename
print "If you don't want that,hit CTRL-C(ˆC)"
print "If you do want that, hit RETURN."
# 等待用户输入
raw_input("?")
# 以写入模式打开文件
print "Open the file..."
target = open(filename,'w')
# 清空文件原先内容
print "Truncating the file.Goodbye!"
target.truncate()
# 输入三行文字,将文字赋予变量
print "Now I'm going to ask you for three lines."

line1 = raw_input("line1:")
line2 = raw_input("line2:")
line3 = raw_input("line3:")

text = line1 + "\n" + line2 + "\n" +line3 + "\n"

print "I'm going to write these to the file."

# 变量写入文档
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

target.write(text)

# 关闭文档
print "And finally,We close it."
target.close()




# DK 

# 01 写注释弄明白

# 02 用 read 与 argv 读取刚写的文档

    #--> 见 16_DK02.py

# 03 用一个 target.write 将 line 123写出来

    # text = line1 + "\n" + line2 + "\n" +line3 + "\n"
    # target.write(text)

# 04 "w"?

    # 文件打开的访问模式,"w"代表写入模式,根据安全第一的原则,只有特殊制定
    # 才能够实现"写入"的操作, 比如" a"

# 05 "w" 与 truncate
    # 'w' for writing (truncating the file if it already exists)


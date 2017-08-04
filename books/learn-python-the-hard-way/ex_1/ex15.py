# -*- coding:utf-8 -*-

# BE 00

from sys import argv     # get arguments of modul

script,filename = argv    #  arguments contain two parts: py and  txt

txt = open(filename)      # txt is variaty:open() get the filename and point to this file

print "Here's your file %r:" % filename  # print strings
print txt.read()                     # print the centent of txt（the pointed file）

txt.close()

print "Type the filename again:"     # print strings
file_again = raw_input(">")         # variaty file_again:remind user to input as required with "<"

txt_again = open(file_again)       # txt_again is variaty:open() get the filename and point to this file

print txt_again.read()        # print the centent of txt（the pointed file）

txt_again.close()

# DK 
# 01 注释


# 05 只用 raw_input 改写脚本:

    # 5,7行删去,改成 filename = raw_input("what's your file name?")

# 06 raw_input 与 argv 哪个好?
    # raw_input(),有提示用语,用户有操作依据

# 07 IDLE open 与 read

# 08 关闭文件 colse()

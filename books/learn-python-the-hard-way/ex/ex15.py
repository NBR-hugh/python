# -*- coding: utf-8 -*-

from sys import argv     # get arguments of modul

script,filename = argv    #  grguments contain two parts: py and  txt

txt = open(filename)      # txt is variaty:open() get the filename and point to this file

print "Here's your file %r:" % filename  # print strings
print txt.read()                     # print the centent of txt（the pointed file）

#print "Type the filename again:"     # print strings
#file_again = raw_input(">")         # variaty file_again:remind user to input as required with "<"

#txt_again = open(file_again)       # txt_again is variaty:open() get the filename and point to this file

#print txt_again.read()        # print the centent of txt（the pointed file）


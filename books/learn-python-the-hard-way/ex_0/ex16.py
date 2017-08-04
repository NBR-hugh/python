# -*- coding: utf-8 -*-

from sys import argv      # call system for the moudul:argv

script,filename = argv     # set two arguments for argv

print "We're going to erase %r." % filename    # output string
print "If you don't want that, hit CTRL-C (ˆC)."  # output string
print "If you do want that, hit RETURN."   # output string

raw_input("?")            # get the response of user

print "Opening the file..."  # output string
target = open(filename,'w')    # variaty target: open file and ready to write

print "Truncating the file. Goodbye!"  # output string
target.truncate()             # delete all content of file pointed by target

print "Now I'm going to ask you for three lines." # output string

line1 = raw_input("line 1:")     # deliver response of user to variaty line1/2/3
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")

print "I'm going to write these to the file."    # output string

#target.write(line1)          # deliver variaty line1/2/3 and \n to file
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

# n = line1 + "\n" + line2 + "\n" + line3 + "\n"
# target.write(n)

n = "%r\n%r\n%r\n" % (line1,line2,line3)
target.write(n)

print "And finally,we close it."  # output string
target.close()         # cloed and save target

# -*- coding: utf-8 -*-

from sys import argv  # argv:arguments variables

script, input_file = argv # 2 varieties:script,input_file

def print_all(f):         # deliver f as argument for function print_all
    print f.read()        # print the content readed from file"f"

def rewind(f):            # deliver f as argument for function remind
    f.seek(0)             # on file "f" seeking "0"？

def print_a_line(line_count,f):       # deliver variaties the number of line and the file "f"
    print line_count, f.readline()  # print the number of line ,and print the centent of file"f" on that nunmu

current_file = open(input_file)  # varriaty "opne_file" to open the "input_file"

print "First let's print the whole file:\n"

print_all(current_file)          # run function peint_all

print "Now let's rewind,kind of like a tape."

rewind(current_file)# print first line

print "Let's print three lines:"
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1               # print second line
print_a_line(current_line,current_file)

current_line = current_line + 1              # print third line
print_a_line(current_line,current_file)


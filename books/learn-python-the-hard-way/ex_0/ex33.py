
#1.while function
#numbers = []

#def numbers_group(max,gap):
#    i = 0
#   while i < max:
#       print "At the top i is %d" % i
#       numbers.append(i)
#       i = i + gap
#       print "Number now:",numbers
#       print "At the bottom i is %d" % i
#
#numbers_group(20,2)
#print "The number:"

#for num in numbers:
#    print num

#2.for function

numbers = []

def numbers_group(max,gap):
    for i in range(0,6):
        print "At the top i is %d" % i
        numbers.append(i)
        print "Number now:",numbers
        print "At the bottom i is %d" % i

numbers_group(20,2)
print "The number:"

for num in numbers:
    print num

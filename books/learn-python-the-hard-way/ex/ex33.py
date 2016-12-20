
numbers = []

def numbers_group(max):
    i = 0
    while i < max:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + 1
        print "Number now:",numbers
        print "At the bottom i is %d" % i

numbers_group(6)
print "The number:"

for num in numbers:
    print num


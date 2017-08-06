from sys import argv

script,filename = argv

print "the %s showed here:" % filename
f = open(filename)
print f.read()

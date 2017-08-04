from sys import argv

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)
indata = open(from_file).read()
print "Ready,hit RERURN to continue,CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright,all done."

out_file.close()


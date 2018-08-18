from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

lin1 = raw_input("line 1:")
lin2 = raw_input("line 2:")
lin3 = raw_input("line 3:")

print "I'm going to write these to the file."

target.write(lin1)
target.write("\n")
target.write(lin2)
target.write("\n")
target.write(lin3)
target.write("\n")

print "And finally, we close it."
target.close()
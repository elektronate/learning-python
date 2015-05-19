# "Reading Files"
# open() [opens file]
# x.read() [prints file content]
# x.close() [closes file]

from sys import argv # imports argv module

script, filename = argv # defines argv variables

txt = open(filename) # gets file

print "Here's your file %r:" % filename # prints string w/filename
print txt.read() # displays file

txt.close() # closes file

txt = open(filename) # opens file again

raw_input("Want to read it again? Hit RETURN!")
print txt.read()
# same as print open(filename).read()

txt.close()

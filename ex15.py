# "Reading Files"
# open() [opens file]
# x.read() [prints file content]
# x.close() [closes file]

from sys import argv # imports argv module

script, filename = argv # defines argv variables

txt = open(filename) # gets file

print "Here's your file %r:" % filename # prints string w/filename
print txt.read() # displays file

print txt.close() # closes file

txt = open(filename) # opens file again

file_again = raw_input("Type the filename again: ")
print txt.read()

print txt.close()

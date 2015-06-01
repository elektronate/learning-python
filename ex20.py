# "Functions and Files"
# .seek() for operating in open file; removes the pointer to other part of the file
# .seek(0) moves to the beginning of the file, to first byte (not line)
# += adds another value with the variable's value and assigns the new value to the variable
# readline() stops at each \n inside a file

from sys import argv

script, input_file = argv

def print_all(f): # f = file
    print f.read()

def rewind(f):
    f.seek(0)
    
def print_a_line(line_count, f):
# comma avoids adding double \n to every line
    print line_count, f.readline(), 

# opens file and assigns it to the current_file variable
current_file = open(input_file)

print "First let's print the whole file:\n"
# calls function print_all
print_all(current_file)

print "Now let's rewind, kind of like a tape.\n"
# calls function rewind
rewind(current_file)

print "Let's print three lines:\n"

# defines current_line variable
current_line = 1
# calls print_a_line function
print_a_line(current_line, current_file)

# redefines current_line variable by adding one line, jumping to line 2
#current_line = current_line + 1
current_line += 1
print_a_line(current_line, current_file)

#current_line = current_line + 1
current_line += 1
print_a_line(current_line, current_file)

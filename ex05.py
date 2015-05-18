# "More Variables and Printing"
# "strings" are for humans

# variable = 'format string' OR variable = integer

name = 'Bruce Wayne'
age = 32
inch = 0.393701 # conversion factor centimeters to inch
lbs = 2.20462262185 # conversion factor kg to lbs
height = 189.0  # centimeters
weight = 120.0 # kilogram 
eyes = 'green'
teeth = 'white'
hair = 'dark'

# format characters: %s (for strings), %d (for integers), %f (for float),
# %r (for debugging; prints out raw data)

print "Let's talk about %s." % name
print "He's %d inches tall." % (height * inch)
print "He's %d lbs heavy." % (weight * lbs)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

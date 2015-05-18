# "What was That?"
# Escape Sequences
# \ (backslash) encodes difficult-to-type characters into a string
# \\  \'  \"  \a  \b  \n  \N{name}  \r  \t
# \f (form-feed) moves printing position to next logical page
# \v (vertical-tab) moves printing position to next vt position

tabby_cat = "\tI'm tabbed in."
persian_cat = "\vI'm split\non a line."
claustro_cat = "\fI need air."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* "Fishies"
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print claustro_cat
print backslash_cat
print fat_cat

print "The cat says: \"%s\"" % tabby_cat
print "The cat says: \"%r\"" % tabby_cat

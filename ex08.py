# "Printing, Printing"
# "%r %r %r %r" is a string containing format characters
# each %r is demanding arguments [% (x, y, z, x)]
# else: "TypeError: not all arguments converted during string formatting"

formatter = "%r %r %r %r"

print formatter % ("Because", 7, "ate", 9)
print formatter % ('one', "two", "three", "four")
print formatter % (True, "love", "is", False)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didnt't sing.",
    "So I said..."
)

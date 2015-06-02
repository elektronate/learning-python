print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "--------------"
print poem
print "--------------"

# five = 10 - 2 + 3 - 6
# print "This should be five: %s" % five

def secret_formula(amount):
    gem = amount * 500
    boxes = gem / 1000
    crates = boxes / 100
    return gem, boxes, crates
    
what_gem = raw_input("What kind of gemstone do you have? ") 

pieces = int(raw_input("How many %ss do you have? " % 
    what_gem 
    )) 

stone, boxes, suitcases = secret_formula(pieces)

print "So you have %d %ss." % (pieces, what_gem)
print "You'll need %d boxes, and %d suitcases for that.\n" % (
    boxes, suitcases
    )

pieces = pieces / 10

print "We can also do that this way:",
print """
If you had %d gems, you would need %d boxes, 
and %d suitcases.
""" % secret_formula(pieces)
  

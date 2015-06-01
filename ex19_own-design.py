# "Functions and Variables"
# Different ways to run a function

def meetup(confirmed, declined, indecisive):
    print "These are the responses to our invitation:"
    print "%d people will attend." % confirmed
    print "%d people declined the invitation." % declined
    print "%d people are still indecisive.\n" % indecisive
    
# 1
meetup(221, 45, 189)

# 2
yes = 221
no = 45
maybe = 189

meetup(yes, no, maybe)

# 3
meetup(190 + 31, 5 + 4 * 10, 200 / 2 + 89)

# 4
print "Number of attendees updated:"
meetup(yes + 11, no + 46, maybe + 120)

# 5
y = int(raw_input("How many people will attend? "))
n = int(raw_input("How many have declined? "))
m = int(raw_input("How many are indecisive? "))

invited = y + n + m
print "We have invited %d people." % invited

meetup(y, n, m)




# "Asking Questions"
# raw_input() demands input from user (always string)
# int(raw-input()) gets number as string, converting it to integer


name = raw_input("Hi! What's your name? ")
print "So glad I found you, %s! I wanna know everything about you." % name

print "How old are you?",
age = int(raw_input())
print "Where do you live?",
location = raw_input()
print "What's your favorite dish?",
dish = raw_input()

print "So, you're %r, huh?" % age
print "I love %r! We should have some %r when I come visit." % (
    location, dish
    )

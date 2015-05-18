# "Asking Questions" & "Prompting People"
# raw_input() demands input from user (always string)
# int(raw-input()) gets number as string, converting it to integer


name = raw_input("Hi! What's your name? ")
print "So glad I found you, %s! I wanna know everything about you." % name

age = int(raw_input("How old are you?"))
location = raw_input("Where do you live?")
dish = raw_input("What's your favorite dish?")

print "So, you're %r, huh?" % age
print "I love %r! We should have some %r when I come visit." % (
    location, dish
    )

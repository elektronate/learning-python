# "Parameters, Unpacking, Variables"
# import; modules, also called libraries
# eg. argv (argument variable)

from sys import argv

script, getting, things, done = argv

# print "The script is called:", script
# print "Your first variable is:", getting
# print "Your second variable is:", things
# print "Your third variable is:", done

goal = raw_input("Good Morning! What is your goal for today? ")
print "You should think this through. You look tired."
sleep = int(raw_input("How many hours of sleep did you get tonight? "))
print "Only %d hours of well-deserved sleep?" % sleep
print "As your health-advisor I recommend you lie down again."

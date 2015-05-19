# "Prompting and Passing"
# arguments for terminal input: python ex14.py [your name]
# variable prompt

from sys import argv

script, user_name = argv
prompt = '>'

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."

print "Where do you live?"
lives = raw_input(prompt)

print "What do you do there, %s?"  % (user_name)
does = raw_input(prompt)

print "What's the name of your favorite person?"
loves = raw_input('<3')

print """
Alright %r, so you just told me you live in %r. 
I know your occupation. I even know %r to be 
the person most precious to you. 
How does that make you feel?
""" % (user_name, lives, loves)

from sys import argv

script, user_name = argv
print ("Hi %s, I'm the %s script." % (user_name, script))
print ("I'd like to ask you a few uestions.")
print ("Do you like me %s?" %user_name)
likes = input(">")
print ("Where do you live %s？" %user_name)
lives = input(">")
print ("What kind of computeer do you have?")
computer = input(">")

print ("""
Alright, so you said %r about liking me.
you live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)) 

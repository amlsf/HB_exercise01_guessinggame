#greet player, get player name
name = raw_input("Howdy, what's your name?")

print "%s, I'm thinking of a number between 1 and 100." % (name),
print "Try to guess my number."

#choose random number between 1 to 100
answer = randomint(1,100)
print randomint

#while True: 
#    get guess
#    if guess is incorrect: 
#        give hint
#    else: congratulate player
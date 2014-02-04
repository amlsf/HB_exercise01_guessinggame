from random import randint

#greet player, get player name
name = raw_input("Howdy, what's your name?")

print "%s, I'm thinking of a number between 1 and 100." % (name),
print "Try to guess my number."

#choose random number between 1 to 100
answer = randint(1,100) #randint is inclusive of 1 to 100
print answer

#while True: 
#    get guess
#    if guess is incorrect: 
#        give hint
#    else: congratulate player
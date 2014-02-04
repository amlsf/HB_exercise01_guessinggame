from random import randint

#greet player, get player name
name = raw_input("Howdy, what's your name?")

print "%s, I'm thinking of a number between 1 and 100." % name,
print "Try to guess my number."

#choose random number between 1 to 100
answer = randint(1,100) #randint is inclusive of 1 to 100
print answer

while guess != answer:
    guess = raw_input("Your guess?")

    if guess < answer:
        print "Your guess is too low, try again"
    elif guess > answer:
        print "Your guess is too high, try again"
    else: 
        print "Well done, %s" % name,
        print "You found my number in x tries!"
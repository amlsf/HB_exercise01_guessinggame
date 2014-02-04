from random import randint

#greet player, get player name
name = raw_input("Howdy, what's your name?")

print "%s, I'm thinking of an integer between 1 and 100." % name,
print "Try to guess my number."

#choose random number between 1 to 100
answer = randint(1,100) #randint is inclusive of 1 to 100
print answer

x = 0

while True:
    guess = raw_input("Your guess?")
# Need to figure out how to check for valid input, 
# error if int cast non-int then can't check with isinstance
    if guess.isdigit() != True:
        print "invalid input"
        guess = raw_input("Your guess?")
    elif int(guess) < answer:
        print "Your guess is too low, try again"
        x += 1
    elif int(guess) > answer:
        print "Your guess is too high, try again"
        x += 1
    else: 
        print "Well done, %s" % name,
        print "You found my number in %d tries!" % x
        break
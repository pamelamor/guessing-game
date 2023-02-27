import random
"""A number-guessing game."""

# Put your code here
print("Howdy, what's your name?")
print("(type in your name)")

userName = input()

print(userName + ", I'm thinking of a number between 1 and 100.")
print("Try to guess my number.")
print("Your guess?")
userGuess = int(input())

randomNumber = random.randint(0, 100)
tries = 0

while userGuess != randomNumber: 
    if userGuess > randomNumber:
        tries += 1
        print("Your guess is too high, try again.")
    elif userGuess < randomNumber:
        tries += 1
        print("Your guess is too low, try again.")
    userGuess = int(input())
        
if userGuess == randomNumber: 
    print("Well done, " + userName + "! You found my number in " + str(tries) + " tries!")



import random
"""A number-guessing game."""

# Prompt the user
print("Howdy, what's your name?")
# Get user name
userName = input("(type in your name) ")
# Prompt the user to pick a number between 1 and 100
print(userName + ", I'm thinking of a number between 1 and 100.")
print("Try to guess my number.")
# Get user guess
userGuess = int(input("Your guess? "))
# Choose a random number
randomNumber = random.randint(0, 100)
tries = 0

while userGuess != randomNumber: 
    
    if userGuess > randomNumber:
        tries += 1
        print("Your guess is too high, try again.")
    elif userGuess < randomNumber:
        tries += 1
        print("Your guess is too low, try again.")
    userGuess = int(input("Your guess? "))
        
if userGuess == randomNumber: 
    print("Well done, " + userName + "! You found my number in " + str(tries) + " tries!")



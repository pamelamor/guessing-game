import random
"""A number-guessing game."""

def play_game():
    # Prompt the user for their name and store it
    userName = input("Howdy, what's your name? (Type in your name) ")
    # Allow user to chose the numerical range of the game
    lowerBound, higherBound = input("Enter a numerical range to play for: "). split()
    randomNumber = random.randint(int(lowerBound), int(higherBound))
    # Prompt the user to make a guess
    print(userName + ", I'm thinking of a number between " + lowerBound  + " and "  + higherBound  + ". Try to guess my number.")
    userGuess = int(input("Your guess? "))
    tries = 0
    
    while userGuess != randomNumber: 
        print(randomNumber)
        print(tries)
        if tries == 10:
            print("Too many tries!")
            break
        # Evaluate guess
        elif userGuess > randomNumber:
            tries += 1
            print("Your guess is too high, try again.")
        elif userGuess < randomNumber:
            tries += 1
            print("Your guess is too low, try again.")
        userGuess = int(input("Your guess? "))

        
    if userGuess == randomNumber:
        print("Well done, " + userName + "! You found my number in " + str(tries) + " tries!")
    
    # Restart or start a new guessing round
    anotherRound = input("Would you like to pay another round (Type 'Yes' or 'No')? ")
    if anotherRound == "Yes":
        play_game()
    else:
        return
 
play_game()

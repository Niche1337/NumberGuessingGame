"""
Number Guessing Game
--------------------------------
"""

import random




def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    


    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    randNumber = random.randint(1,10)
    name = input("What is your name? ").capitalize()
    print("Hello {}, and welcome to the number guessing game".format(name))
    print("I am thinking of a number between 1 and 10, what is it?")
    
    while True:
        attempts = 1
        guess = int(input("What is my number? ")
        if guess == randNumber:
            print("You guessed correctly, it took {} attempts, thanks playing!!! The Game will end".format(attempts))
            break
        elif guess < randNumber:
            print("The number is higher, try again")
        elif guess > randNumber:
            print("The number is lower, try again")

        attempts += 1
        



if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()

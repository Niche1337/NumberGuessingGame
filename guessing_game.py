"""
Number Guessing Game
--------------------------------
"""

import random




def start_game():
    highScore = 100
    attempts = 0
    randNumber = random.randint(1,10)
    name = input("What is your name? ").capitalize()
    print("Hello {}, and welcome to the number guessing game".format(name))
   
    print("I am thinking of a number between 1 and 10, what is it?")
    
    while True:
        attempts += 1
        try:
            guess = int(input("What is my number? "))
            if guess > 10 or guess < 0:
                raise ValueError("Enter a value within the range 1 - 10")
            if guess == randNumber:
                print("You guessed correctly, it took {} attempt/s, thanks playing!".format(attempts))    
                if attempts < highScore:
                    highScore = attempts    
                if input("Would you like to play again? y/n? ").upper() == "Y":
                    print("The current highscore/least number of attempts is {}".format(highScore))
                    randNumber = random.randint(1,10)
                    continue
                else:
                    print("Thank for playing the 'Number Guessing Game', goodbye")
                    break
            elif guess < randNumber:
                print("The number is higher, try again")
            elif guess > randNumber:
                print("The number is lower, try again")
        except ValueError as err:
            print("{}".format(err))
            print("Please enter a correct value")

        
        



if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()

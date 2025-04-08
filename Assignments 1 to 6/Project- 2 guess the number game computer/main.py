import random

def guess_the_number():
    """ Guess The Number Game By Computer """
    number_to_guess = random.randint(1, 100)
    guesses_left = 7

    # Welcome message
    print("Welcome to Guess The Number Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Loop to handle the guessing attempts
    while guesses_left > 0:
        print(f"\nYou have {guesses_left} guesses left.")
        try:
            guess = int(input("Take a guess: "))
        except ValueError:
            print("Invalid input: Please enter a number.")
            continue
        
        # Compare the guessed number with the actual number
        if guess < number_to_guess:
            print("Too low! Try a higher number.")
        elif guess > number_to_guess:
            print("Too high! Try a lower number.")
        else:
            print(f"Congratulations! You guessed the correct number in {7 - guesses_left + 1} tries.")
            return
        
        guesses_left -= 1
    
    # If all guesses are used up
    print(f"\nYou've run out of guesses. The correct number was {number_to_guess}.")

# Run the game
guess_the_number()

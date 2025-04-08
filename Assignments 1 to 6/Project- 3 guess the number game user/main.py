import random
print("Guess a number between 1 and 100! ")

#generate random number

number = random.randint(1, 100)

while True:
    guess = int(input("Enter your guess number: "))
    if guess < number:
        print("Too Low, try again!")
    elif guess > number:
        print("Too High, try again!")
    else:
        print("You guessed it! The number was " + str(number))
        break

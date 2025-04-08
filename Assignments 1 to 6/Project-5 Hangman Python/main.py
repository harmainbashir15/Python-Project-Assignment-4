import random

words = ['Python' , 'Visual Studio Code' , 'Enum' , 'Game' , 'Colab']
word = random.choice(words)
guessed_letters = []
attempts = 6
print("Welcome to Hangman Game!")
print("_" * len(words))


while attempts > 0:
    guess = input("\n Guess the letters: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter only!")
        continue
    if guess in guessed_letters:
        print("You already guessed this letter, try another one!")
        continue
    guessed_letters.append(guess)
    if guess  in word:
        print("Correct guess!")
    else:
        attempts -= 1
        print(f"Wrong {attempts} attempts.")
    displayed_word = " " .join([letter if letter in guessed_letters else "_" for letter in word])
    print(displayed_word)
    
    
    if "_" not in displayed_word:
        print(f"Congratulations! the correct word is: {word}.")
        break
else:
    print(f"Game Over! The correct word is: {word}.")
        




# Write a code to build hangman game 
import random

# List of words for the game
word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

# Select a random word from the list
secret_word = random.choice(word_list)
guessed_letters = []
attempts = 6  # Number of allowed attempts

# Display initial information
print("Welcome to Hangman!")
print(f"You have {attempts} attempts to guess the word.")

# Create a function to display the word with underscores for unknown letters
def display_word(word, guessed_letters):
    result = ""
    for letter in word:
        if letter in guessed_letters:
            result += letter
        else:
            result += "_"
    return result

# Main game loop
while attempts > 0:
    print(display_word(secret_word, guessed_letters))
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Good guess!")
    else:
        print("Wrong guess!")
        attempts -= 1

    if all(letter in guessed_letters for letter in secret_word):
        print("Congratulations! You guessed the word:", secret_word)
        break

if attempts == 0:
    print("Out of attempts! The word was:", secret_word)




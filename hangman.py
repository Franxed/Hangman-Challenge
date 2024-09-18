# Import libraries.
import random

# Created customized list.
list_words = ['hangman', 'apple', 'computer', 'satellite', 'table', 'book', 'happiness']
random_word = random.choice(list_words).upper()  # Randomly picks from the list.
# print(random_word)  # Testing (comment out to try)

count = 0   # Start count for wrong guesses.

# Initialize the blank line.
placeholder = "_" * len(random_word)
print(placeholder)  # Shows the initial blank placeholder.

while True:
    display = ""
    guess = input("Guess : ").upper()

    # Check if the guessed letter is in the word and update the placeholder.
    for letter in range(len(random_word)):
        if random_word[letter] == guess:
            display += random_word[letter]  # Add guessed letter at the correct position.
        else:
            display += placeholder[letter]

    placeholder = display        # Update the placeholder with the new display.
    print(placeholder)           # Display the updated word with guessed letters.

    # Checks if the guess is wrong.
    if guess not in random_word:
        count += 1
        print("Wrong guess. You have ", 6 - count, " tries left.")

    # Checks if all letter have been guessed.
    if "_" not in placeholder:
        print("Congratulations! You won!")
        break

    # Gives 6 chances.
    if count >= 6:
        print(f"Hanged! The word was {random_word}.\n Better luck next time!")
        break

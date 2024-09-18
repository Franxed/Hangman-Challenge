import random

list_words = ['hangman', 'apple', 'computer', 'satellite', 'table', 'book', 'happiness']
random_word = random.choice(list_words).upper()
print(random_word)
random_word = "_" * len(random_word)
count = 0

for letter in random_word:
    print(letter, end=" ")

while True:
    guess = input("\nGuess:").upper()

    if guess == random_word:
        pass

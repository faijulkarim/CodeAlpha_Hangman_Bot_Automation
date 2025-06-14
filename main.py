import random

words = ["apple", "grape", "mango", "peach", "people"]
chosen_word = random.choice(words)
display = ["_"] * len(chosen_word)
lives = 6

print("Welcome to Hangman!")
print("Guess the word, one letter at a time.")

while lives>0 and "_" in display:
    guess = input("Welcome a letter: ").lower()
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                display[index] = guess
    else:
        lives -= 1
        print(f"wrrong! Lives left: {lives}")
    print("Current word: ", "".join(display))

if "_" not in display:
    print("Congratulations! You guessed the word: ", chosen_word)
else:
    print("Game Over! The word was: ", chosen_word)

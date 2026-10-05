import random

# List of predefined words
words = ["python", "computer", "program", "coding", "developer"]

# Select a random word
word = random.choice(words)

# Game variables
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

# Display hidden word
display_word = ["_"] * len(word)

print("================================")
print("       HANGMAN GAME")
print("================================")
print("Guess the word one letter at a time!")
print("You have 6 wrong guesses.")

# Main game loop
while wrong_guesses < max_wrong_guesses and "_" in display_word:

    print("\nWord:", " ".join(display_word))
    print("Wrong guesses:", wrong_guesses)
    
    guess = input("Enter a letter: ").lower()

    # Check valid input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    # Add letter to guessed letters
    guessed_letters.append(guess)

    # Check whether guess is correct
    if guess in word:
        print("Correct guess!")

        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess

    else:
        wrong_guesses += 1
        print("Wrong guess!")

# Final result
print("\n================================")

if "_" not in display_word:
    print("Congratulations! 🎉")
    print("You guessed the word:", word)
else:
    print("Game Over! 😔")
    print("The correct word was:", word)

print("================================")
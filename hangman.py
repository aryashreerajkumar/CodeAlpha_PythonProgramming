import random

# List of words
words = ["python", "computer", "program", "science", "gaming"]

# Select a random word
secret_word = random.choice(words)

# Create empty list to store guessed letters
guessed_letters = []

# Number of wrong attempts
wrong_guesses = 0

# Maximum wrong guesses allowed
max_wrong = 6


print("====== HANGMAN GAME ======")
print("Guess the word one letter at a time!")

# Create hidden word
display_word = ["_"] * len(secret_word)


# Game loop
while wrong_guesses < max_wrong:

    print("\nWord:", " ".join(display_word))
    print("Wrong guesses:", wrong_guesses, "/", max_wrong)

    # User input
    guess = input("Enter a letter: ").lower()


    # Check input
    if len(guess) != 1:
        print("Please enter only one letter!")
        continue


    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed this letter!")
        continue


    # Store guessed letter
    guessed_letters.append(guess)


    # Correct guess
    if guess in secret_word:

        print("Correct guess!")

        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess


    # Wrong guess
    else:

        print("Wrong guess!")
        wrong_guesses += 1



    # Check winning condition
    if "_" not in display_word:

        print("\nCongratulations!")
        print("You guessed the word:", secret_word)
        break



# Game over condition
if wrong_guesses == max_wrong:

    print("\nGame Over!")
    print("The word was:", secret_word)
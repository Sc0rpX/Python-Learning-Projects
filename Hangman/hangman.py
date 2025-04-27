import os
from wordlist import random_word    # Import function to get a random word
from art import stage, logo         # Import ASCII art for stages and logo

# Display the game logo
print(logo)

# Choose a random word for the game
choosen_word = random_word()

# Create a display list with underscores for each letter
display = []
for char in choosen_word:
    display += "_"

# Initialize game variables
lives = 6
end_of_game = False

# Main game loop
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Clear the screen after each guess
    os.system('cls' if os.name == 'nt' else 'clear')

    # Check if the letter was already guessed
    if guess in display:
            print(f"You have already guessed '{guess}'!")

    # Reveal guessed letters in their correct positions
    for i in range(len(choosen_word)):
        if guess == choosen_word[i]:
            display[i] = guess

    # If guess not in word, lose a life
    if guess not in display:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

    # Check if player lost all lives
    if lives == 0:
        end_of_game = True
        print("You Lose!")

    # Show the current state of guessed word
    print(f"{' '.join(display)}")

    # Check if player has guessed all letters
    if "_" not in display:
        end_of_game = True
        print("You Win!")

    # Display the current hangman stage 
    print(stage(lives))

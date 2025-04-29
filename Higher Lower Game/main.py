from random import choice
import os

from ascii_art import *
from game_data import data

def clear():
    """Clear the terminal screen for both Windows and Unix-based systems."""
    os.system('cls' if os.name == 'nt' else 'clear')

# Initialize game state
score = 0
compare_b = ""

# Main game loop
while True:
    # First round setup
    if score == 0:
        clear()
        print(logo)
        compare_a = choice(data)
    else:
        # Continue from previous correct guess
        clear()
        print(logo)
        print(f"✅ Correct! Current Score: {score}")
        compare_a = compare_b

    # Ensure compare_b is different from compare_a
    while True:
        compare_b = choice(data)
        if compare_b != compare_a:
            break

    # Display comparison
    print(f"🔹 Compare A: {compare_a['name']}, {compare_a['description']}, from {compare_a['country']}.")
    print(vs)
    print(f"🔸 Compare B: {compare_b['name']}, {compare_b['description']}, from {compare_b['country']}.\n")

    # Take player input
    player_input = input("👉 Who has more followers? Type 'A' or 'B': ").upper()

    # Determine which has more followers
    if compare_a['follower_count'] > compare_b['follower_count']:
        correct_answer = 'A'
    else:
        correct_answer = 'B'

    # Check if the player's answer is correct
    if player_input == correct_answer:
        score += 1
        continue    # Go to next round
    else:
        break   # End the game

# Game over screen
clear()
print(logo)
print(f"❌ Wrong Answer! Final Score: {score}")
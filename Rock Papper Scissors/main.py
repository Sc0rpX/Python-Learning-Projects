import random
import os
from ascii_arts import *

# List of Rock, Papper and Scissor's ascii art
img = [rock, paper, scissors]

# Main game loop
should_continue = True
while should_continue:
    # Check if the player want to play again
    want_to_play = input("Do you want to play Rock Papper Scissors? 'y' or 'n': ").lower()
    if want_to_play == 'n':
        should_continue = False
        break
    elif want_to_play not in ['y', 'n']:
        print("Please enter a valid input, 'y' or 'n'")
        break

    # Clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)

    # Players input
    print("Choose your move: 0 for Rock, 1 for Paper and 2 for Scissors")
    player_move = int(input("> "))
    if player_move < 0 or player_move > 2:
        print("Wrong move. You Lose!")
        exit(1)
        
    print("You choose: " + img[player_move])

    # Computer's move
    computer_move = random.randint(0, 2)
    print("Computer choose: " + img[computer_move])

    # Determine and display the game result
    if player_move == 0 and computer_move == 2:
        print("You Win!")
    elif player_move == 2 and computer_move == 0:
        print("You Lose!")
    elif player_move > computer_move:
        print("You Win!")
    elif player_move < computer_move:
        print("You Lose!")
    else:
        print("It's a Draw!")

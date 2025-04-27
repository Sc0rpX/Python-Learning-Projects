from ascii_art import logo
from functions import *

should_continue = True

# Main game loop
while should_continue:
    want_to_play = input("Do you want to play BlackJack? 'y' or 'n': ").lower()

    if want_to_play == 'n':
        should_continue = False
        break
    elif want_to_play not in ['y', 'n']:
        print("Please enter a valid input, 'y' or 'n'")
        break

    clear()
    print(logo)

    # Get computer's cards and score
    computer_cards, computer_score = computer_draw_cards()
    print(f"Computer's first card: {computer_cards[0]}")

    # Deal player's cards
    player_cards = []
    for i in range(2):
        player_cards.append(deal_card())

    player_score = calculate_score(player_cards)
    player_turn = True if player_score != 0 else False

    print(f"Your cards: {player_cards}, current score: {player_score}")

    # Player chooses to hit or stand
    while player_turn:
        draw_more = input("Do you want another card? 'y' on 'n': ").lower()

        if draw_more == 'y':
            player_cards.append(deal_card())
            player_score = calculate_score(player_cards)
            print(f"Your cards: {player_cards}, current score: {player_score}")

            if player_score >= 21:
                player_turn = False

        elif draw_more == 'n':
            player_turn = False

        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    clear()
    print(logo)
    
    # Show final results and determine winner
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(f"Your final hand: {player_cards}, final score: {player_score}")
    choose_winner(computer_score, player_score)
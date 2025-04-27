from random import choice
import os

def clear():
    """Clear the terminal screen for both Windows and Unix-based systems."""
    os.system('cls' if os.name == 'nt' else 'clear')

def deal_card():
    """Return a randomly selected card value from a standard deck.
    
    Note: 11 represents Ace, and 10 appears four times to account for face cards.
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return choice(cards)

def calculate_score(cards):
    """Calculate and return the total score for a given list of cards.
    
    Special Rules:
    - A hand with two cards that sum up to 21 is considered a Blackjack (score = 0).
    - If score is over 21 and there's an Ace (11), convert it to 1.
    """
    score = sum(cards)
    
    if score == 21 and len(cards) == 2:
        return 0 # Blackjack
    
    if 11 in cards and score > 21:
        cards.append(1)
        cards.remove(11)

    return sum(cards)

def computer_draw_cards():
    """Automate computer's card drawing logic.

    The computer will continue drawing cards until the score exceeds 17.
    Returns:
        Tuple: (computer's cards list, final score)
    """
    computer_cards = []

    while True:
        computer_cards.append(deal_card())
        score = calculate_score(computer_cards)

        if score > 17:
            break

    return computer_cards, score

def choose_winner(computer_score, player_score):
    """Determine and display the game result."""
    if player_score == 0:
        print("Blackjack! 🎉\nYou win! 😽")

    elif computer_score > 21:
        print("Opponent busted! 🎉\nYou win! 😽")

    elif player_score > 21:
        print("You busted! 😿\nYou lose!")

    elif player_score == computer_score:
        print("It's a Draw! 🐱")

    else:
        computer_diff = 21 - computer_score
        player_diff = 21 - player_score

        if computer_diff < player_diff:
            print("You lose! 😿")
        else:
            print("You win! 😽")
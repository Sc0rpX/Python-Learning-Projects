from ascii_art import logo
import os

# Bids Dictionary to store the bids with bidders
bids_dictionary = {}

# Loop to take the bids
bidding_over = False
while not bidding_over:
    # Clear the screen after each bid to keep the bids secrate
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)

    # Input bidder name
    name = input("Enter your name: ")

    # Input valid bids
    valid_bid = False
    while not valid_bid:
        bid =  input("Enter your bid: $")

        # Bids validity check
        if not bid.isnumeric():
            print("Invalid Bid. Please Enter A Valid Bid!")
        else:
            valid_bid = True

    # Add the bids into the dictionary
    bids_dictionary[name] = int(bid)

    # Check is there any other bidder 
    valid_bidder_input = False
    while not valid_bidder_input:
        other_bidder = input("Is there any other bidder? 'yes' or 'no': ").lower()

        # Inputs validity check
        if other_bidder not in ['yes', 'no']:
            print("Invalid Input. Please Enter 'yes' or 'no'.")
        else:
            valid_bidder_input = True

    # If there is'nt any other bidder then break the loop
    if other_bidder == "no":
        bidding_over = True

# Keep track of Highest bidder and Highest bid
highest_bider = ""
highest_bid = 0

# Find out Highest bidder and Highest bid
for bider in bids_dictionary:
    if highest_bid < bids_dictionary[bider]:
        highest_bid = bids_dictionary[bider]
        highest_bider = bider

# Print out the winner
os.system('cls' if os.name == 'nt' else 'clear')
print(logo)
print(f"The winner is {highest_bider} with a bid of ${highest_bid}")
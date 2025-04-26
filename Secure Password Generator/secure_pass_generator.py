import random

# Lists of characters to use in the password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'w', 'x', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to Secure Password Generator!\n")

# Ask user for password character counts
no_letters = int(input("How many letters would you like in your password? "))
no_numbers = int(input("How many numbers would you like? "))
no_symbols = int(input("How many symbols would you like? "))

# Initialize the password character list
pass_list = []

# Add random letters, numbers and symbols to the password list
for letter in range(0, no_letters):
    pass_list.append(random.choice(letters))

for number in range(0, no_numbers):
    pass_list.append(random.choice(numbers))

for symbol in range(0, no_symbols):
    pass_list.append(random.choice(symbols))

# Shuffle the characters to make the password more secure
random.shuffle(pass_list)

# Join the characters into a single string
password = ""
for char in pass_list:
    password += char

# Display the final password
print(f"Your most secure password is: {password}")
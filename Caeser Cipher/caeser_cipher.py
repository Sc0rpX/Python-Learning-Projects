from ascii_art import logo

# Display the logo art
print(logo)

# List of lowercase letters for the Caesar cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caeser(dir, input_text, shift_amount):
    """Encrypts or decrypts a message using Caesar cipher based on user input."""
    final_text = ""

    if dir == "encode":
        # Shift letters forward
        for letter in text:
            if letter not in alphabet:
                final_text += letter  # Keep non-letter characters unchanged
            else:
                enc_position = alphabet.index(letter) + shift
                if enc_position > 25:
                    enc_position = enc_position % 26  # Wrap around alphabet
                final_text += alphabet[enc_position]
        
    elif dir == "decode":
        # Shift letters backward
        for letter in text:
            if letter not in alphabet:
                final_text += letter
            else:
                dec_position = alphabet.index(letter) - shift
                if dec_position < 0:
                    dec_position = 26 + dec_position # Wrap around
                final_text += alphabet[dec_position]

    print(f"The {dir}d text is {final_text}")

# Loop to allow repeated encryption/decryption
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caeser(direction, text, shift)
    
    again = input("Type 'y' if you want to go again. Otherwise type 'n'\n").lower()
    if again == 'n':
        print("Good bye!")
        break

    
    

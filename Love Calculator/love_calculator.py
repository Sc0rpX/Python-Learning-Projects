print("Welcome to Love Calculator!")

# Input names
name1 = input("What is your name?\n")
name2 = input("What is your partner's name?\n")

names = name1.lower() + name2.lower()

# Count the letters for "TRUE"
t = names.count("t")
r = names.count("r")
u = names.count("u")
e = names.count("e")

true = t + r + u + e

# Count the letters for "LOVE"
l = names.count("l")
o = names.count("o")
v = names.count("v")
e = names.count("e")

love = l + o + v + e

# Combine the scores
score = int(str(true) + str(love))

# Fun messages based on score ranges
if score < 10 or score > 90:
    print(f"Your score is {score} — You go together like Coke and Mentos! 🧨💖")

elif 70 <= score <= 90:
    print(f"Your score is {score} — A perfect match! Cupid would be proud! 🏹❤️")

elif 50 <= score < 70:
    print(f"Your score is {score} — You're a strong duo! 💪💑")

elif 40 <= score < 50:
    print(f"Your score is {score} — You are alright together. Not bad! 😺")

elif 20 <= score < 40:
    print(f"Your score is {score} — There's potential! Keep nurturing it. 🌱✨")

else:
    print(f"Your score is {score} — Well... opposites do attract sometimes! 😅💔")

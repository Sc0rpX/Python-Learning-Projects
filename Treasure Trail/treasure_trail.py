print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."_` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
''')

print("Welcome to Treasure Trail.")
print("Your mission is to find the treasure.\n") 

print("You wake up in a dense forest. The air is damp, and you can hear the faint sound of water flowing nearby. In front of you is a path that splits into two. Where do you want to go? Type 'left' or 'right'.")
choice11 = input(">").lower()
print()

if choice11 == "left":
    print("You walk down the left path, and it leads to a raging river. The current looks strong, but you notice a rickety old bridge nearby. Do you want to 'cross' the bridge or 'follow' the riverbank?")
    choice12 = input(">").lower()
    print()

    if choice12 == "follow":
        print("You follow the riverbank and spot a small boat tied to a tree. You use it to cross the river safely. On the other side, you see a cave entrance. Do you want to 'enter' the cave or 'explore' the forest around it?")
        choice13 = input(">").lower()
        print()

        if choice13 == "enter":
            print("Inside the cave, you find a chest filled with gold and jewels. Congratulations! You found the treasure! You Win!")
        elif choice13 == "explore":
            print("As you wander the forest, you hear growls behind you. A pack of wolves emerges from the trees. You try to run, but they catch up. Game Over.")    
        else:
            print("You typed something that doesn't make sense. Lost in thought, you trip over a rock and fall into a ditch. Game Over.")

    elif choice12 == "cross":
        print("As you step onto the bridge, it creaks loudly. Halfway across, the wood snaps, and you fall into the river. You get swept away by the current. Game Over.")
    else:
        print("You typed something that doesn't make sense. Lost in thought, you trip over a rock and fall into a ditch. Game Over.")

elif choice11 == "right":
    print("You head down the right path and come to an open clearing with a mysterious hut in the middle. Smoke rises from its chimney. Do you want to 'knock' on the door or 'sneak' around the back?") 
    choice22 = input(">").lower()
    print()

    if choice22 == "knock":
        print("The door creaks open, and an old woman appears. She offers you two potions: one red and one green. Which do you choose? Type 'red' or 'green'.")
        choice23 = input(">").lower()
        print()

        if choice23 == "green":
            print("The green potion heals your body and sharpens your senses. The old woman tells you about a hidden treasure deep in the forest. You follow her directions and find a chest full of gold. You Win!")
        elif choice23 == "red":
            print("The red potion burns your throat as you drink it. Suddenly, you feel dizzy and collapse. Game Over.")
        else:
            print("You typed something that doesn't make sense. Lost in thought, you trip over a rock and fall into a ditch. Game Over.")
    
    elif choice22 == "sneak":
        print("You sneak around the back of the hut and see a trapdoor partially hidden under leaves. You open it and climb down into a dark tunnel. At the end of the tunnel, you find a treasure chest. But as you approach, the floor crumbles beneath you, and you fall into a pit. Game Over.")
    else:
        print("You typed something that doesn't make sense. Lost in thought, you trip over a rock and fall into a ditch. Game Over.")

else:
        print("You typed something that doesn't make sense. Lost in thought, you trip over a rock and fall into a ditch. Game Over.")

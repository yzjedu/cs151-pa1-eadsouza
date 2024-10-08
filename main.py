# Introduction
print("Welcome, brave adventurer!")
name = input("What is your name, adventurer? ")

print("Hello,", name,"! You find yourself standing at the entrance of a mysterious jungle. Your mission is to recover the lost artifact known as the 'Crystal of Eternity'. As you step forward, you realize there are two paths ahead of you: one leads to a dense forest, while the other heads toward a dark cave.")

# First Decision: Path Choice
path_choice = input("Which path will you take? Enter 'forest' to go through the dense forest or 'cave' to explore the dark cave: ").lower()
while path_choice != "forest" and path_choice != "cave":
    print("That's not a valid choice. Please choose 'forest' or 'cave'.")
    path_choice = input("Which path will you take? Enter 'forest' to go through the dense forest or 'cave' to explore the dark cave: ").lower()

# If player chooses forest
if path_choice == "forest":
    print(name,"you venture into the dense forest, surrounded by towering trees and the sounds of wildlife. The journey will not be easy.")

    door_choice = int(input("You come across three doors. Enter 1 for the red door, 2 for the blue door, or 3 for the green door: "))

    while door_choice != 1 and door_choice != 2 and door_choice != 3:
        print("That's not a valid door. Please select 1, 2, or 3.")
        door_choice = int(input("Enter 1 for the red door, 2 for the blue door, or 3 for the green door: "))

    if door_choice == 1:
        print("You enter a peaceful clearing. The air is calm, and you feel at ease.")
        potion = input("You find three potions on a table: 'red', 'blue', and 'green'. Which one will you drink? ").lower()

        while potion != "red" and potion != "blue" and potion != "green":
            print("That's not a valid potion choice. Please choose 'red', 'blue', or 'green'.")
            potion = input("You find three potions on a table: 'red', 'blue', and 'green'. Which one will you drink? ").lower()

        if potion == "red":
            print("The red potion grants you immense strength!")
        elif potion == "blue":
            print("The blue potion grants you invisibility, allowing you to sneak past enemies.")
        elif potion == "green":
            print("The green potion heals you from your injuries.")

    elif door_choice == 2:
        print("You encounter a pack of wild animals. You need to be prepared to handle them.")
        has_equipment = True
        if has_equipment:
            print("You successfully fend off the animals and proceed further.")
        else:
            print("Without proper equipment, you retreat to find another path.")
    elif door_choice == 3:
        open_chest = input("You find a treasure chest in the middle of the room. Do you want to open it? (yes/no): ").lower()
        if open_chest == "yes":
            print("You open the chest and find a magical shield.")
        else:
            print("You decide to leave the chest untouched.")

# If player chooses cave
elif path_choice == "cave":
    print(name,"you cautiously enter the dark cave, your footsteps echoing off the stone walls. You can barely see ahead, but you press forward.")
    jump_distance = float(input("You come across a gap. How many meters will you jump across (e.g., 5.5)? "))
    while jump_distance < 0:
        print("Please enter a valid positive distance to jump across.")
        jump_distance = float(input("You come across a gap. How many meters will you jump across (e.g., 5.5)? "))
    if jump_distance < 5:
        print("You fall short of the gap and need to find another way around.")
    elif 5 <= jump_distance <= 10:
        print("You make it across the gap successfully!")
    elif jump_distance > 10:
        print("You overshoot the jump and land in a dangerous spot.")
        escape_danger = True
        if escape_danger:
            print("You manage to escape safely.")
        else:
            print("You're caught in a difficult situation and must retreat.")

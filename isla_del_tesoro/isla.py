import time

# Introduction
print("Welcome to Treasure Island!")
time.sleep(1)
print("Your mission is to find the treasure hidden on the island.")
time.sleep(1)
print("You arrive on the island and find yourself at a crossroads.")
time.sleep(1)

# First decision
print("You come across a signpost. Which way do you go?")
time.sleep(1)
print("A. Left")
print("B. Right")
choice1 = input("Enter A or B: ").lower()

if choice1 == "a":
    print("You come across a river. What do you do?")
    time.sleep(1)
    print("A. Swim across")
    print("B. Look for a bridge")
    choice2 = input("Enter A or B: ").lower()
    
    if choice2 == "a":
        print("You get swept away by the current and drown. Game over.")
    elif choice2 == "b":
        print("You find a bridge and cross safely.")
        time.sleep(1)
        print("You come across a cave. What do you do?")
        time.sleep(1)
        print("A. Enter the cave")
        print("B. Keep walking")
        choice3 = input("Enter A or B: ").lower()
        
        if choice3 == "a":
            print("You find the treasure! Congratulations, you win!")
        elif choice3 == "b":
            print("You keep walking and get lost in the jungle. Game over.")
        else:
            print("Invalid input. Game over.")
    else:
        print("Invalid input. Game over.")
        
elif choice1 == "b":
    print("You come across a group of pirates. What do you do?")
    time.sleep(1)
    print("A. Fight the pirates")
    print("B. Try to sneak past them")
    choice4 = input("Enter A or B: ").lower()
    
    if choice4 == "a":
        print("You fight bravely, but are outnumbered. Game over.")
    elif choice4 == "b":
        print("You sneak past the pirates and find a treasure map.")
        time.sleep(1)
        print("You follow the map and come across a cave. What do you do?")
        time.sleep(1)
        print("A. Enter the cave")
        print("B. Keep walking")
        choice5 = input("Enter A or B: ").lower()
        
        if choice5 == "a":
            print("You find the treasure! Congratulations, you win!")
        elif choice5 == "b":
            print("You keep walking and get lost in the jungle. Game over.")
        else:
            print("Invalid input. Game over.")
    else:
        print("Invalid input. Game over.")
        
else:
    print("Invalid input. Game over.")
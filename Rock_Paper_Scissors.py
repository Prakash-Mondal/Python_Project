

import random
import os

# Creating a function to clear output screen...


def clear(): return os.system("cls")


# Creating game images...

rock = '''
     _______  
----'   ____)
       (_____)
       (_____)
       (____)
---.__(__)
'''

paper = '''
     _______
----'   ____)____
            _____)
            ______)
          ______)
---._________)
'''

scissors = '''
     _______
----'   ____)____
            _____)
        __________)
        (____)
---.____(___)
'''
game_images = [rock, paper, scissors]

end_of_game = False

while not end_of_game:

    print("\n\nWelcome to Rock Paper Scissors Game ...\n")
    print("rules : \n"
          + "1. Rocks wins against scissors\n"
          + "2. Scissors wins against paper\n"
          + "3. Paper wins against rock\n\n\n")

    # Taking input from user...
    player_choice = int(
        input("What do you choose ? Type 1 for Rock, 2 for Paper or 3 for Scissors : "))

    print(f"\nYou Choose : {player_choice}")

    if (player_choice <= 3) and (player_choice >= 1):
        print(game_images[player_choice-1])

    # Generating random number ...
    Computer_choice = random.randint(1, 3)

    print(f"\nComputer choose : {Computer_choice}")

    print(game_images[Computer_choice-1])

    # Game logic ...

    if (player_choice > 3) or (player_choice < 1):
        print("You typed an invalid number, you lose!")
    elif (player_choice == Computer_choice):
        print("Match Draw!")
    elif (player_choice == 1) and (Computer_choice == 3):
        print("You win!")
    elif (player_choice == 3) and (Computer_choice == 1):
        print("You lose!")
    elif (player_choice > Computer_choice):
        print("You win!")
    elif (Computer_choice > player_choice):
        print("You lose!")

    # Checking if player want to play again or not...

    should_continue = input(
        "\nType 'yes' to play again or 'no' to stop : ").lower()
    if should_continue == 'no' or should_continue == 'n':
        end_of_game = True
    elif should_continue == 'yes' or should_continue == 'y':
        end_of_game = False
        clear()
    else:
        print("Invalid input!")
        end_of_game = True
print("\n\n")


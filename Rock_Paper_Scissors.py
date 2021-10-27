
import random

print("\n\nWelcome to Rock Paper Scissors Game ...\n")
print("rules : \n"
      + "1. Rocks wins against scissors\n"
      + "2. Scissors wins against paper\n"
      + "3. Paper wins against rock\n\n\n")


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

player_choise = int(
    input("What do you choose ? Type 1 for Rock, 2 for Paper or 3 for Scissors : "))


print(f"\nYou Choose : {player_choise}")

if (player_choise <= 3) and (player_choise >= 1):
    print(game_images[player_choise-1])

# Generating random number ...
Computer_choise = random.randint(1, 3)

print(f"\nComputer choose : {Computer_choise}")

print(game_images[Computer_choise-1])


# Game logic ...

if (player_choise > 3) or (player_choise < 1):
    print("You typed an invalid number, you lose!")
elif (player_choise == Computer_choise):
    print("Match Draw!")
elif (player_choise == 1) and (Computer_choise == 3):
    print("You win!")
elif (player_choise == 3) and (Computer_choise == 1):
    print("You lose!")
elif (player_choise > Computer_choise):
    print("You win!")
elif (Computer_choise > player_choise):
    print("You lose!")

print("\n\n")

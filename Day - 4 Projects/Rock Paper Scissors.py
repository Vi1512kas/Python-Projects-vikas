import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
choice = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors\n"))
computer_choice = random.randint(0, 2)
if choice == 0:
    if computer_choice == 1:
        print("You choose : rock")
        print(rock)
        print("computer choose : paper")
        print(paper)
        print("You loose against computer....")
    elif computer_choice == 2:
        print("You choose : rock")
        print(rock)
        print("computer choose : scissors")
        print(scissors)
        print("You Won against computer....")
    else:
        print("You choose : rock")
        print(rock)
        print("computer choose : rock")
        print(rock)
        print("Match Draws...")
elif choice == 1:
    if computer_choice == 0:
        print("You choose : paper")
        print(paper)
        print("computer choose : rock")
        print(rock)
        print("You Won against computer....")
    elif computer_choice == 2:
        print("You choose : paper")
        print(paper)
        print("computer choose : scissors")
        print(scissors)
        print("You loose against computer....")
    else:
        print("You choose : paper")
        print(paper)
        print("computer choose : paper")
        print(paper)
        print("Match Draws...")
else:  # scissors
    if computer_choice == 0:
        print("You choose : scissors")
        print(scissors)
        print("computer choose : rock")
        print(rock)
        print("You loose against computer....")
    elif computer_choice == 1:
        print("You choose : scissors")
        print(scissors)
        print("computer choose : paper")
        print(paper)
        print("You won against computer....")
    else:
        print("You choose : scissors")
        print(scissors)
        print("computer choose : scissors")
        print(scissors)
        print("Match Draws...")







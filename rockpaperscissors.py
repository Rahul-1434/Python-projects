import random

rock =rock = """
     _______
---'   ____ )
       (_____)
       (_____)
       (____)
---.__(___)
"""

paper = """
      _______
---'    ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
     _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

l=[rock,paper,scissors]

user_choice=int(input("Enter your choice: Type 0 for Rock, 1 for Paper, 2 for Scissors."))
if 3<=user_choice or user_choice<0:
    print("You entered invalid number, You Lose.")
else:
    print(l[user_choice])
    computer_choice=random.randint(0,2)
    print("computer choice:")
    print(l[computer_choice])
    if computer_choice==user_choice:
        print("It's a draw.")
    elif computer_choice == 0 and user_choice == 2:
        print("you Lose.")
    elif computer_choice == 2 and user_choice == 0:
        print("you win.")
    elif user_choice < computer_choice:
        print("you Lose.")
    elif computer_choice < user_choice:
        print("You win.")

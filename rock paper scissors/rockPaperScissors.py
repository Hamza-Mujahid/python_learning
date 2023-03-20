import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)_____
           _______)
          ________)
         ________)
---.___________)
"""

scissors ="""
    _______
---'   ____)_____
          _______)
       ___________)
      (____)
---.__(___)
"""

ans = [rock, paper, scissors]  

userAns = input("Enter Rock(0), Paper(1) or Scissors(2) then hit Enter to play \n")
# computer_choice = random.randint(0,2)
computer_choice = 2

if int(userAns) == computer_choice:
    print("OH snap It's a draw let's go again")
    userAns = input("Enter Rock(0), Paper(1) or Scissors(2) then hit Enter to  \n")
    
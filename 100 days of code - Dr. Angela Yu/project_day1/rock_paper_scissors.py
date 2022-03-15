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

#Write your code below this line 👇
user_input = int(input("What do you choose? Typer 0 for Rock, 1 for Paper or 2 for Scissors. \n"))

if user_input == 0:
  print(rock)
if user_input == 1:
  print(paper)
if user_input == 2:
  print(scissors)

computer_choice = random.randint(0, 2)
print("Computer choice: ")

if computer_choice == 0:
  print(rock)
if computer_choice == 1:
  print(paper)
if computer_choice == 2:
  print(scissors)

if user_input == 0 and computer_choice == 0 :
  print("Draw")
if user_input == 0 and computer_choice == 1:
  print("You lose")
if user_input == 0 and computer_choice == 2:
  print("You win")

if user_input == 1 and computer_choice == 0 :
  print("You win")
if user_input == 1 and computer_choice == 1:
  print("Draw")
if user_input == 1 and computer_choice == 2:
  print("You lose")

if user_input == 2 and computer_choice == 0 :
  print("You lose")
if user_input == 2 and computer_choice == 1:
  print("You win")
if user_input == 2 and computer_choice == 2:
  print("Draw")
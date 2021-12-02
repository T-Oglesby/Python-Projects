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

game_images = [rock, paper, scissors]


choice = input('What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors \n')
user_choice = int(choice)
computer_choice = random.randint(0,2)

#if user_choice == 0:
#  print(rock)
#elif user_choice == 1:
#  print(paper)
#else:
#  print(scissors)    */

if user_choice < 3:
  print(game_images[user_choice])
else:
  print("You have entered an invalid number.")

print("Computer chose: \n")

print(game_images[computer_choice])
#if computer_choice == 0:
#  print(rock)
#elif computer_choice == 1:
#  print(paper)
#else:
#  print(scissors)

if user_choice == 0 and computer_choice == 1:
  print("Paper covers Rock, you lose.")
elif user_choice == 0 and computer_choice == 2:
  print("Rock smashes Scissors, you win!")
elif user_choice == 1 and computer_choice == 0:
  print("Paper covers Rock, you win!")
elif user_choice == 1 and computer_choice == 2:
  print("Scissors cuts Paper, you lose.")
elif user_choice == 2 and computer_choice == 0:
  print("Rock smashes Scissors, you lose.")
elif user_choice == 2 and computer_choice == 1:
  print("Scissors cuts Paper, you win!")        
elif user_choice == computer_choice:
  print("Draw Game, play again.")

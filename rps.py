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

import random

game_images = {1:rock, 2:paper, 3:scissors }

print("What do you choose?")
your_choice = int(input("Type 1 for Rock, 2 for Paper or 3 for Scissors."))
print(game_images[your_choice])


comp_choice = random.randint(1,3)
print(f"Computer chose:{comp_choice}")
print(game_images[comp_choice])



if your_choice >= 4 or your_choice < 0:
    print("invalid number") 
elif your_choice == 1 and comp_choice == 3:
    print("You Win")
elif comp_choice == 1 and your_choice == 3:
    print("You lose")        
elif comp_choice > your_choice:
    print("You lose")
elif your_choice > comp_choice:
    print("You win")    
elif your_choice == comp_choice:
    print("Its a tie")   
   


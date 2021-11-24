import random
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
dice = input("roll a d10 to begin. Luck will play a roll in your future. Please enter roll \n")
ran_num = random.randint(1,10)
dice_roll = ran_num
print(f"Your dice roll is {dice_roll}. Good or bad, this will help determine your future. \n")
crossroad = input("After a long night at the local tavern, you awaken on the road. Tired, hungover, hungry, and unsure of where you are. One thing is certain however. You remember being told of a treasure by an old pirate in the bar. You boasted you could find it yourself. Do you go left, or right at the crossroad? \n")

crossroad_lower = crossroad.lower()

if crossroad_lower == 'right':
  river = input('You take the path on the right. The sun rises higher in the sky and begins to obscure your vision. The hangover, taking its toll on your mind and your eyesight. You stumble down the path and come to a river. You can attempt to swim across the river or search to see if there\'s something that can help you get across. Swim, or search? \n')
else:
  print("You take the path to the left. Your drunken stumbling causing you to lose your balance and you fall off the road, tumbling down the side of a hill to your demise. You have died. Maybe drunken bragging about your treasure hunting skills wasn't the best choice?")  

river_lower = river.lower()
if river_lower == 'search':
  houses = input("\n After searching you find a small rowboat. It's seen better days, but it looks like it has enough life in it for one more adventure. You make your way across the river to a small island. The island has 3 houses, a house with a Red door, a house with a blue door, and a house with a green door. You can feel it. The treasure is here somehwere. Which house do you want to go to? Red, Green, or Blue? \n")
else:
  print('\n You decide to swim across the river. Given your current state, some would say its unwise, but you push on. As you enter the river, the current is stronger than you anticipated. You struggle to maintain your momentum, but ultimately the river claims another victim. You have died.\n ')

houses_lower = houses.lower
if houses_lower == 'red' and dice_roll >= 4 and dice_roll <=7:
  print('\n You approach the house with the red door. The smell of something burning fills your nostrils. You are overtaken by an impending sense of doom. As you turn the knob to open the door, you are engulfed in flames. Your ashes spread across the doorway, a warning for the next treasure hunters.')
elif houses_lower == 'red' and dice_roll >= 1 and dice_roll <= 3:
  print("\n You turn the knob on the door. The sense of excitement at the possibility has cleared you of your drunken stupor. You've seen a lot today, and are sure about your success. As you enter the house, you find a chest, tucked into the corner of a bedroom. You have found the treasure! Congratulations")
elif houses_lower == 'red' and dice_roll >=8:
  houses = input('The house is empty. It was left abandoned, lost to time as the previous owners seem to have moved on. There is nothing of value or substance in this house. You decide to check either the Green or Blue house next. Which will it be? Green or Blue? \n ')
  houses = houses
  houses_lower = houses.lower() 

if houses_lower == 'green' and dice_roll >= 1 and dice_roll <=4:
  print('\n You approach the house with the green door. You feel calm as you begin to approach. As you turn the knob to open the door, you hear a loud "click" and are sure you have set off a trap. You attempt to look around as the house explodes with you at the doorway. You have perished.')
elif houses_lower == 'green' and dice_roll >=7 and dice_roll <=10:
  print("\n You turn the knob on the door. The sense of excitement at the possibility has cleared you of your drunken stupor. You've seen a lot today, and are sure about your success. As you enter the house, you find a chest, tucked into the corner of a bedroom. You have found the treasure! Congratulations")
elif houses_lower == 'green' and dice_roll == 5 or dice_roll == 6:
  houses = input('The house is empty. It was left abandoned, lost to time as the previous owners seem to have moved on. There is nothing of value or substance in this house. You decide to check either the Red or Blue house next. Which will it be? Red or Blue? \n')
  houses = houses
  houses_lower = houses.lower() 

if houses_lower == 'blue' and dice_roll >= 1 and dice_roll <=3:
  print('\n You approach the house with the blue door. You feel calm as you begin to approach. You enter the house and begin to search around. You step into the bedroom, and onto the carpet. You have fallen into a boobytrap and are locked in a cage beneth the floor. Left for dead locked in a cage under the floor in an abandoned house with no one searching for you, you perish.')
elif houses_lower == 'blue' and dice_roll >=4 and dice_roll <=6:
  print("\n You turn the knob on the door. The sense of excitement at the possibility has cleared you of your drunken stupor. You've seen a lot today, and are sure about your success. As you enter the house, you find a chest, tucked into the corner of a bedroom. You have found the treasure! Congratulations")
elif houses_lower == 'blue' and dice_roll >= 7:
  houses = input('The house is empty. It was left abandoned, lost to time as the previous owners seem to have moved on. There is nothing of value or substance in this house. You decide to check either the Red or Green house next. Which will it be? Red or Green? \n')
  houses = houses
  houses_lower = houses.lower()         

decision = input("Welcome to Treasure Island. Your mission is to find the treasure. \n First off, choose 'left' or 'right'. No punctuation, so, no periods or commas\n")

if decision == 'right':
  print('Game Over.')
if decision == 'left':
    decision = input("Nice job! You survived. Now, decide: 'swim' or 'wait'?\n")

if decision == 'wait':
  print('Attacked by trout.\nGame Over.')
if decision == 'swim':
  decision = input("Nice job! You survived. Now, decide which door: 'red' or 'blue'?\n")

if decision == 'red':
  print('Burned by fire. Game Over.')
elif decision == 'blue':
  print('Eaten by beasts. Game Over.')
elif decision == 'yellow':
  print('You Win!')
else:
  print('Game Over.')


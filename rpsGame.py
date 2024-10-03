#Ramie Mosely Rock Papers Scissors In Python
#Importing Modules
import random
import math

#Getting user input and computer choice
def playGame():
    user = input("Choose Your Weapon: 'r' for ROCKZ! - 'p' for PAPERZ! - 's' for SCISSORZ!")
    user = user.lowerr()

    computerChoice = range(1,4)

    computerRange = random.choice(computerChoice)

    if computerRange == 1:
        compFinal = 'r'
    elif computerRange == 2:
        compFinal = 'p'
    else:
        compFinal = 's'

    if user == compFinal:
        return "You and the computer have both chosen {}. It is a tie".format(compFinal) 
    
    if win(user,compFinal):
        return "You have chosen {} and the computer has chosen {}. You won!".format(user, compFinal)



#Check if the player won
def win(player, enemy):



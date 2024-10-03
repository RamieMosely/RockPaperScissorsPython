#Ramie Mosely Rock Papers Scissors In Python
#Importing Modules
import random
import math





#Getting user input and computer choice
def playGame():
    user = input("Choose Your Weapon: 'r' for ROCKZ! - 'p' for PAPERZ! - 's' for SCISSORZ!\n")
    user = user.lower()


    #Computer Choice
    computerChoice = range(1,4)
    computerRange = random.choice(computerChoice)
    if computerRange == 1:
        compFinal = 'r'
    elif computerRange == 2:
        compFinal = 'p'
    elif computerRange == 3:
        compFinal = 's'

    
    #Check if tie
    if user == compFinal:
        return "You and the computer have both chosen {}. It is a tie".format(compFinal) 
    
    if win(user,compFinal):
        return "You have chosen {} and the computer has chosen {}. You won!".format(user, compFinal)
    
    return "You chose {} and the computer chose {}. You lose!".format(user, compFinal)



#Check if the player won
def win(player, enemy):

    if player == 'r' and enemy == 's':
        return True
    elif player == 's' and enemy == 'p':
        return True
    elif player == 'p' and enemy == 'r':
        return True
    
    else:
        return False


#Welcome Message
print("Welcome to Ramies Python Rock Paper Scissors Game!\n")

mainGame = playGame()

print(mainGame)


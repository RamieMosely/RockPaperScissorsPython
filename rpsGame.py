#Ramie Mosely Rock Papers Scissors In Python
#Importing Modules
import random
import math





#Getting user input and computer choice
def playGame():
    user = str(input("Choose Your Weapon: 'r' for ROCK! - 'p' for PAPER! - 's' for SCISSOR!\n"))
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
        return (0, user, compFinal) 
    
    if win(user,compFinal):
        return (1, user, compFinal) 
    
    return (-1, user, compFinal) 



#Check if the player won
def win(player, enemy):

    if player == 'r' or player == 'rock' and enemy == 's':
        return True
    elif player == 's' or player =='scissors' and enemy == 'p':
        return True
    elif player == 'p' or player == 'paper' and enemy == 'r':
        return True
    
    return False

#Game Rounds To Win
def bestOf(x):
    winsPlayer = 0
    winsComputer = 0
    necWin = math.ceil(x/2)
    print(necWin)
    while winsPlayer < necWin and winsComputer < necWin:
        result, user, compFinal = playGame()
        #Its a tie
        if result == 0:
            print('It is a tie. You and the computer both chose {}.\n'.format(user))
        elif result == 1:
            winsPlayer +=1
            print('You chose {} and the computer chose {} ! You won!\n'.format(user, compFinal))
        else:
            winsComputer +=1
            print('You chose {} and the computer chose {} ! You lost!\n'.format(user, compFinal))
        
        if winsPlayer > winsComputer:
            print("You have won!")
            print(f"Your Score is {winsPlayer}!")
            print(f"The computers score is {winsComputer}!")
   
        elif winsComputer > winsPlayer:
            print("You have lost!")
            print(f"Your Score is {winsPlayer}!")
            print(f"The computers score is {winsComputer}!")
    
        else:
            print("It is a tie!")
    

            


#Welcome Message
print("####################################################")
print("Welcome to Ramies Python Rock Paper Scissors Game!")
print("####################################################")
print()

numOfRounds = int(input("How many rounds would you like to play?\n"))

bestOf(numOfRounds)



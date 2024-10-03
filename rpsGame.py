#Ramie Mosely Rock Papers Scissors In Python
#Importing Modules
import random
import math



#Getting user input and computer choice
def playGame():
    #Input Validation Loop
    while True:
        user = ''
        print("###################################################################################")
        user = str(input("Choose Your Weapon: 'r' for ROCK! - 'p' for PAPER! - 's' for SCISSOR!\n###################################################################################\n"))

        user = user.lower()

        if user == 'quit':
            while True:
                isQuit = str(input("Are you sure? Would you like to play another round?"))

                if isQuit == 'no' or isQuit == 'n':
                    print("You chose to quit the game. Goodbye!")
                    return None, None, None
                elif isQuit == 'yes' or 'yes':
                    print("Enjoy The Game!")
                    break

    
        # Check if user input is correct
        if user == 'r' or user == 'p' or user == 's' or user == 'rock' or user == 'paper' or user == 'scissor':
            break  
        else:
            print("Please enter 'r', 'p', or 's'. Or Rock Paper Scissor")





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
    print(f"You must win {necWin} rounds to beat the computer!\n")
    while winsPlayer < necWin and winsComputer < necWin:
        result, user, compFinal = playGame()


        # Check if user quit the game
        if result is None:
            return 


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
while numOfRounds < 1:
    print("Please enter a valid number of rounds!")
    numOfRounds = int(input("How many rounds would you like to play?\n"))


bestOf(numOfRounds)
print('Thanks for playing!')



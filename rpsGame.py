#Ramie Mosely Rock Papers Scissors In Python

import random

def play():
    user = input("Choose Your Weapon: 'r' for ROCKZ! - 'p' for PAPERZ! - 's' for SCISSORZ!")
    user = user.lowerr()

    computer = random.choice(['r', 'p', 's'])


'''NIM Version 1

    The game starts with 21 sticks. Players must choose either 1, 2 or 3 sticks. This continues until all sticks are gone and the 
    player that selects the last stick is the loser.

    Created by Liam Brew on 03.31.19'''

import sys

def NIM(player, sticks):
    choice = int(input("Player {}, how many would you like to draw?: ".format(player)))
    if choice not in (1, 2, 3): 
        print("Error: {} is not an accepted choice (only select 1, 2 or 3 sticks please).".format(choice))
        NIM(player, sticks)
    sticks -= choice
    if sticks <= 0: 
        print("Player {} lost!".format(player))
        return
    NIM(3-player, sticks)

def play():
    while True:
        print("Welcome to NIM! Draw your sticks.")
        NIM(1, 21)
        rematch = str(input("Would you like a rematch?"))
        if rematch.lower() == "yes":
            play()
        sys.exit()
            
play()
    
    

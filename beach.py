# SKULL ISLAND BEACH
from vod import *

def goto_beach():
    print("welcome to skull island beach.")
    print ("your mission is to escape from the zombies.")
    phase1 =input("You're at a skull island. where do you want to go? 'left' or 'right' \n").lower()
    if phase1 =="left":
        phase2 = input("You've come to the beach. There is ship in the middle there. "wait" for a boat. Swim across.\n').lower()
    if phase2 == "wait":
        phase3 = input("You arrive at the canoe side. There are 3 houses there with diffrent color.one blue, one grey and one red. which color do you choose? \n").lower()
    if phase3 == "blue":
        print(" it is a room full of fire.Game over.")
        goto_death()
    elif phase3 == "grey":
        print("you found the way out! you manage to escape the zombies and run for safety.")
        goto_lagoon()
    elif phase3 == "red":
        print("you enter a house of zombies. Game over.")
        goto_death()
    elif phase3 =="jungle":
        print("you get ambush by diferrent animals. Game over.")
        goto_death()
    else:
        print(" you choose a house that does open again. Game over.")
        goto_death()

goto_beach()








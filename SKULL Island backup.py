# Voyage of the Damned adventure game
# CodeNation Sep 2021
# QA, AB, KO
import sys, datetime, time, random, os


# Define colors and cursor handling as constants
# """ ANSI color codes """
BLACK = "\033[0;30m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BROWN = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
LIGHT_GRAY = "\033[0;37m"
DARK_GRAY = "\033[1;30m"
LIGHT_RED = "\033[1;31m"
LIGHT_GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
LIGHT_BLUE = "\033[1;34m"
LIGHT_PURPLE = "\033[1;35m"
LIGHT_CYAN = "\033[1;36m"
LIGHT_WHITE = "\033[1;37m"
BOLD = "\033[1m"
FAINT = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"
NEGATIVE = "\033[7m"
CROSSED = "\033[9m"
RESET = "\033[0m"
UP = "\033[A"
LEFT = "\033[D"
CLEAR_SCREEN = "\033[2J"

# Global Variables
inventory = []
name = "Jack Sparrow"
age = 0
where_from = "Timbuktu"
stress_level = 0

def vod():
    global inventory
    game_intro()
    print('(Enter a "0" at any input to exit the game)\n')
    board_check()

#   -------------  Common functions declared here   ------------------

def goto_death(string):
    global inventory
    game_over()
    print(PURPLE + f"{string} " + LIGHT_RED + UNDERLINE + "YOU HAVE DIED!!" + RESET)
    print(f"You had {inventory} in your possesion.")
    # <exit program>
    quit()

def get_input(choices):
    # Prints coloured numbered list of choices and choose one of them.
    # returns the number chosen as an int.
    
    print("")
    number = 1
    for question in choices:
        # only 5 colours in a row are useful. Use the first 5 colours and then switch to LIGHT versions of them
        num_colour = "\033[1;"+str(31+number)+"m"    
        if number > 5:  num_colour = "\033[0;"+str(31+number-5)+"m"  # first 5 colours used, switch to 2nd set
        print(f"{num_colour}{number}.{RESET}  {question}")
        number += 1
    choice = input("What are you going to do? ")
    
    # Input validation - make sure they entered a single digit
    if len(choice) > 1 or not choice.isdigit():  
        print("Please choose a single NUMBER from the choices")
        choice = get_input(choices)
    else: choice = int(choice) # now we are sure it is a single digit.
    if choice == 0:
        goto_death(
            "You have quit the island and will never now discover it's mysteries..")
    if choice > number - 1:
        print("I didn't know that was an option, please choose a number from the choices")
        choice = get_input(choices)
    
    return(choice)

def qprint(string, delaytime = 0.00001):
    # prints a string slowly in typewriter effect. delaytime is delay time is seconds
    # the   ,end=''  parameter to print() stops it printing newline, so everything prints on same line
    for char in string:
        print(char, end='')
        sys.stdout.flush()
        time.sleep(delaytime)

def print_big_ascii_gameposter():
    pass
    # qprint(RESET + CLEAR_SCREEN + 
    #        "Welcome to The Voyage of the Damned\n\nA game of mystery and terror\nAre you ready?")
    # # time.sleep(1)
    # print(UP+UP+UP+UP+"\nWelcome to "+RED + UNDERLINE+"The Voyage of the Damned", end='')
    # qprint("!!!!!!\n\n"+RESET)
    # qprint("A game of "+LIGHT_GREEN+"mystery"+LIGHT_WHITE+" and " +
    #        LIGHT_CYAN+"terror\n"+PURPLE + "Are you ready?"+RESET+"\n")

# ------------ All locations defined here ----------------

# -----------------------------------------------------------------

def goto_beach():  # just a dummy location now.
    # Kafila:
    # Called by SHIP.  Goes to ...
    print("On the beach.. You see a magnificant ruined temple to your left and a blue lagoon to your right.")

    choices = [
        "Go to the Temple on the left",
        "Stagger to the Lagoon"
    ]
    choice = get_input(choices)
    if choice == 1:
        print("Temple")
        goto_temple()
    elif choice == 2:
        goto_lagoon()
        quit()
    else:  # should never get a choice this high..
        goto_death("SYSTEM ERROR #zzzzzz")
# -----------------------------------------------------------------

def goto_temple():
    # TEMPLE location in skull island
    # Qaiser:
    # Comes from LAGOON.  Goes to TOMB, BEACH
    global inventory
    print("""                              ஜ۩۞۩ஜ 
🌴🌴🌴🌴 You stumble into a clearing, before you are the overgrown remains of an exotic temple 🌴
Glints of gold remain on the statues. Lured by the promise of treasure and shelter you enter...
Further on you can see what looks like the entrance to a tomb.
""")
    choices = ["Lets explore that tomb."]
    if ("DIAMOND" not in inventory) and ("STATUE" not in inventory): # Havent already got it or swapped with statue
        choices.append("That diamond looks interesting!  Try and pick it up.")
        print("There is a large stone statue of a Sphinx here. Nestled within its paws is a massive Diamond.")  

    choice = get_input(choices) # only need to check for 1st choice. 2nd choice (if there) will run be default.
    if choice == 1:
        goto_tomb()

    print("The Sphinx stirs itself to life with the deep rumble of living stone and intones:")
    print('"I am the guardian of this gem and I despise ignorance in all beings."')
    print('"You must answer three questions correctly to win the gem. and '+RED+'SURVIVE"'+RESET)
    print("First question:")

    question1 = CYAN+"What goes on four feet in the morning, two feet at noon, and three feet in the evening?"+RESET
    question2 = CYAN+"What is the output of this Python program:\n\n" + \
        LIGHT_WHITE+"   def func1():\n    x = 50\n    return x\n    func1()\n   print(x)"+RESET
    question3 = CYAN+"What is the airspeed velocity of an unladen swallow?"+RESET

    print(question1)
    choices = [
        "Woman (and man of course)",
        "Elephants",
        "Fishes"
    ]
    choice = get_input(choices)
    if choice == 1:
        print("The Sphinx shuffles uneasily and mumbles 'lucky guess'")
        print(question2)
        choices = ['""  (Blank string)', "NameError:", "50","None"]
        choice = get_input(choices)
        if choice == 2:
            print('"Well, I didn' + "'" +'t think you were going to get that one!" - the Sphinx exclaims')
            print(question3)
            choices = ["73mph", "20.1mph", "58mph",'Do you mean the African or the European Swallow?']
            choice = get_input(choices)
            if choice == 4:
                qprint("A startled look crosses the Sphinx face:\n")
                qprint('"Huh? I... I dont know that..\n"')
                qprint('"ARRGGH! I cannot answer my own question - I am defeated!!"\n')
                qprint("The Sphinx slinks away leaving the glittering diamond, shooting you a dirty look.\n", 0.1)
                if "DIAMOND" in inventory:
                    print("You already have a Diamond!")
                else:
                    inventory.append("DIAMOND")
                qprint(f"You have acquired a Diamond. You now possess {inventory}. You head deeper into the temple tomb...")
                goto_tomb()   # Passed the Sphinx, go to next room
            else:
                print("You dont watch much Monty Python do you...")
                goto_death("The Sphinx gently blows on you, and you are carried away by a great wind - straight into the volcano!")
        else:
            print("And I thought you were a Python whizz!")
            goto_death("The giant Sphinx, boring of this game, simply sits on you...")
    else:
        print("A riddle as old as the ages. And you got it wrong.")
        goto_death("The giant Sphinx pounces on you and eats you up as a teatime snack!")

# ------------------------ tomb -----------------------------------------
def animate_ball():
    ball = """
        ,o888888o.     
    . 8888     `88.   
    ,8 8888       `8b  
    88 888888888888`8b 
    88 888888888888888 
    88 888888888888888 
    88 888888888888,8P 
    `8 88888888888,8P  
    ` 888888888,88'   
        `8888888P'     
    ˚ ༘✶ ⋆｡˚ ⁀➷
    """

    me = """
            ___
    ARRGGH  (._.)
            <|>
            _/\_
    """
    termx, termy = os.get_terminal_size()
    ball_lines = ball.count("\n")  # count number of lines (\n is newline) in ball so know how far to go UP
    UP = "\033[A"

    print(LIGHT_RED)
    for y in me.split("\n"):
        print(" " * (termx - 28), y)
    print(UP * 12)
    time.sleep(1)
    for i in range(1, termx - 40):    # roll to end of screen - 40 chars
        for y in ball.split("\n"):
            print(" " * i, y)
        time.sleep(0.014)
        print(UP * (ball_lines+2))
    print("\n" * ball_lines)

def roller_ball(delay=0.0):
    # times how long it takes to enter the response with extra or minus time according to previous choices and stats.
    amount_time = 5.0  # default time, when just take statue.
    amount_time += delay
    qprint(f"\n\n\n{LIGHT_RED}With a loud 'thunk' an ancient intricate mechanism is set in motion.\n")
    qprint("At the head of tomb a massive round stone marble drops down\n")
    time.sleep(0.25)
    qprint("...and starts to roll towards you. At the same time the door in the chamber starts opening\n")
    print("If your reactions are quick enough you might reach the door before it crushes you")
    animate_ball()

    print(f"{RED}{NEGATIVE}PLEASE ENTER THE {LIGHT_PURPLE}{UNDERLINE}True{RED}{NEGATIVE} ANSWER IN UNDER {amount_time} SECONDS TO DODGE THE ",end='')
    print(f"{ITALIC}BALL OF DOOM {RESET}{LIGHT_CYAN}")
    choices = [
        "2 + 2 = 4",
        "Garfield the cat hates lasagne",
        "The Python expression:    "+LIGHT_WHITE+"'x = 21; x % 7 == 1'"+LIGHT_CYAN,
        "I love the songs of James Blunt",
        "Trump is still President",
        "The Elephant is the only creature that cannot jump",
        "Lightning never strikes twice"
        ]
    # need to randomise the choices...
    random.shuffle(choices)

    now = time.time()
    choice = get_input(choices)
    elapsed = time.time() - now
    print(RESET)
    if elapsed > amount_time:
        print("Didnt make it, you took","{:.3f}".format(elapsed),"seconds instead of",amount_time)
        goto_death("Crushed by a huge ball - what a way to go!")
    if choices.index("2 + 2 = 4") + 1 != choice:
        print("Oooh, wrong answer. You meet the same fate as the last hat-wearing, whip-bearing adventurer")
        goto_death("Just like this rolling stone, you gathered no moss.")
    qprint("You leap through the door with the merest whisker to spare!. ")
    print(f"You took","{:.3f}".format(elapsed),"seconds out of", amount_time)
    print("YOU MADE IT")
    goto_lagoon()

def goto_tomb():
    # Qaiser:
    # Called by TEMPLE.  Goes to ESCAPE, BEACH
    global stress_level, inventory

    print("                        ▂▃▅▇█▓▒░۩۞۩ ۩۞۩░▒▓█▇▅▃▂")
    print(f"{DARK_GRAY}In the damp gloom of the tomb you feel the hairs on your neck standing up")
    qprint("(maybe you should stop rubbing that balloon you found earlier)", 0.001)
    qprint(f"\n{PURPLE}The atmosphere feels tense, you should be ready to act quickly{DARK_GRAY}\n")
    time.sleep(0.5)
    print("There is a small ornately decorated chamber in the middle of the tunnel with a closed solid stone door",end='')
    if "FEDORA" not in inventory:  print(",and a hat.",end='')
    print("\nThere seems to be a skeletal hand crushed under the door, like it was reaching for the hat at the last moment but missed.. How strange.")
    print(f"On a solid gold pedastal sits a beautiful glowing crystal statue inlaid with gold and silver. {GREEN}It calls to you...{DARK_GRAY}")
    
    choices = [
        "Pick up the hat - it looks kinda cool and he doesn't need it anymore",
        "Continue down the dark tunnel (it's very dark)",
        "Pick up the statue"
    ]
    if "DIAMOND" in inventory:
        choices.append("Carefully replace the statue with the diamond")
    if "FEDORA" in inventory: choices[0] = "Examine your hat again"
    
    choice = get_input(choices)
    if choice == 1:
        print(f"{LIGHT_WHITE}That is one good looking Fedora.{RESET}\nIt fits like a glove and you instantly feel cooler like Hans Solo in that Star Trek movie. ")
        print("(You might react faster with this fine hat. Should keep your head warm as well)")
        if "FEDORA" not in inventory: inventory.append("FEDORA")
        if stress_level > 0: stress_level -= 10
        goto_tomb()
    elif choice == 3:
        qprint("Your hand moves almost of its' own accord and plucks the statue from the plinth.\n")
        qprint(RED+"Of course it's a trap!     "+RESET)
        print("You will have to be quick to escape from here!")
        roller_ball()
    elif choice == 2:
        qprint(f"{DARK_GRAY}As you continue jauntily down the tunnel whistling a happy tune it get darker.. and darker...\n")
        time.sleep(0.25)
        qprint("🌹ڰۣڿڰۣڿஇღԑ̮̑❀ঙ❀ღڰۣڿڰۣڿஇ🌹\nThere are eerie carvings on the wall and what looks like\n")
        qprint("another skeleton squashed flat on the floor.\n")
        qprint("Are you really, really sure you want to do this or would you prefer to do something else..\n")
        x = input("Anything else really. Go back, look at the carvings or skeleton, or continue forward?\n"+LIGHT_CYAN)
        print(f"{RESET}Good choice, too late.. Just as you are about to {x} a 'click' sounds under your foot as a hidden switch activates")
        print("You will have to be much quicker to escape from here..")
        roller_ball(-3.0)  # less chance to dodge in the dark
    elif choice == 4:
        qprint("You carefully replace the glowing statue with the diamond\n")
        time.sleep(1)
        if "FEDORA" in inventory: 
            qprint(GREEN+"With a warm confident hand you switch the treasures, without disturbing anything\n")
            inventory.remove("DIAMOND")
            inventory.append("STATUE")
            qprint("The cave door grinds open as you approach with the mysterious statue.\n")
            qprint("You exit gracefully, stepping over the body. I guess it really was his last crusade in the temple of doom..\n"+RESET)
            goto_lagoon() # next room
        else:    
            qprint(f"{YELLOW}Not quite carefully enough however. A chill wind blows down your neck and you shiver")
            qprint("A slight 'click' sounds out in the still air and the pedastal shakes.")
            print("You should have enough time to dodge the ball from here though..")
            inventory.remove("DIAMOND")
            inventory.append("STATUE")
            roller_ball(+3.0)
    else:  # should never get a choice this high..
        goto_death("SYSTEM ERROR #zzzzzz")
    
# ######################## SHIP ################################################################################
# ###########  Ship intro banner module
#Narrating TEXT PRINT FUNCTION

def narr_print(string, colour = ITALIC + LIGHT_WHITE, delay = 0.09): #! -- Narrator Print
    for letters in string:
        sys.stdout.write(colour +letters + RESET )
        sys.stdout.flush()
        time.sleep(delay)

def delay_intro(string):  #! -- Delayed intro print
    for letters in string:
        sys.stdout.write(letters)
        sys.stdout.flush()
        #time.sleep(0.0001)

########--------------------------
def game_intro():
    print(CLEAR_SCREEN)

    delay_intro("                              Game Project Created by\n                                 Antony Borji, \n                                 Qaiser Adams \n                                 & Kafila Olatinwa")
    time.sleep(2)
    print(CLEAR_SCREEN)

    #! --- White   
    delay_intro("""                                                                
            @@@@@@@@  @@@  @@@  @@@   @@@@@@   @@@                   
            @@@@@@@@  @@@  @@@@ @@@  @@@@@@@@  @@@                   
            @@!       @@!  @@!@!@@@  @@!  @@@  @@!                   
            !@!       !@!  !@!!@!@!  !@!  @!@  !@!                   
            @!!!:!    !!@  @!@ !!@!  @!@!@!@!  @!!                   
            !!!!!:    !!!  !@!  !!!  !!!@!!!!  !!!                   
            !!:       !!:  !!:  !!!  !!:  !!!  !!:                   
            :!:       :!:  :!:  !:!  :!:  !:!   :!:                  
            ::        ::   ::   ::  ::   :::   :: ::::              
            :        :    ::    :    :   : :  : :: : :              
                                                                    
                                                                    
    @@@@@@@    @@@@@@   @@@@@@@@@@   @@@@@@@@@@   @@@@@@@@  @@@@@@@   
    @@@@@@@@  @@@@@@@@  @@@@@@@@@@@  @@@@@@@@@@@  @@@@@@@@  @@@@@@@@  
    @@!  @@@  @@!  @@@  @@! @@! @@!  @@! @@! @@!  @@!       @@!  @@@  
    !@!  @!@  !@!  @!@  !@! !@! !@!  !@! !@! !@!  !@!       !@!  @!@  
    @!@  !@!  @!@!@!@!  @!! !!@ @!@  @!! !!@ @!@  @!!!:!    @!@  !@!  
    !@!  !!!  !!!@!!!!  !@!   ! !@!  !@!   ! !@!  !!!!!:    !@!  !!!  
    !!:  !!!  !!:  !!!  !!:     !!:  !!:     !!:  !!:       !!:  !!!  
    :!:  !:!  :!:  !:!  :!:     :!:  :!:     :!:  :!:       :!:  !:!  
    :::: ::  ::   :::  :::     ::   :::     ::    :: ::::   :::: ::  
    :: :  :    :   : :   :      :     :      :    : :: ::   :: :  :   
                                                                    
                                                                    
    @@@  @@@   @@@@@@   @@@ @@@   @@@@@@    @@@@@@@@  @@@@@@@@     
    @@@  @@@  @@@@@@@@  @@@ @@@  @@@@@@@@  @@@@@@@@@  @@@@@@@@     
    @@!  @@@  @@!  @@@  @@! !@@  @@!  @@@  !@@        @@!          
    !@!  @!@  !@!  @!@  !@! @!!  !@!  @!@  !@!        !@!          
    @!@  !@!  @!@  !@!   !@!@!   @!@!@!@!  !@! @!@!@  @!!!:!       
    !@!  !!!  !@!  !!!    @!!!   !!!@!!!!  !!! !!@!!  !!!!!:       
    :!:  !!:  !!:  !!!    !!:    !!:  !!!  :!!   !!:  !!:          
        ::!!:!   :!:  !:!    :!:    :!:  !:!  :!:   !::  :!:          
        ::::    ::::: ::     ::    ::   :::   ::: ::::   :: ::::     
        :       : :  :      :      :   : :   :: :: :   : :: ::      
    """)

    delay_intro(RED+UP*44+"""                                                                  
            @@@@@@@@  @@@  @@@  @@@   @@@@@@   @@@                   
            @@@@@@@@  @@@  @@@@ @@@  @@@@@@@@  @@@                   
            @@!       @@!  @@!@!@@@  @@!  @@@  @@!                   
            !@!       !@!  !@!!@!@!  !@!  @!@  !@!                   
            @!!!:!    !!@  @!@ !!@!  @!@!@!@!  @!!                   
            !!!!!:    !!!  !@!  !!!  !!!@!!!!  !!!                   
            !!:       !!:  !!:  !!!  !!:  !!!  !!:                   
            :!:       :!:  :!:  !:!  :!:  !:!   :!:                  
            ::        ::   ::   ::  ::   :::   :: ::::              
            :        :    ::    :    :   : :  : :: : :              
                                                                    
                                                                    
    @@@@@@@    @@@@@@   @@@@@@@@@@   @@@@@@@@@@   @@@@@@@@  @@@@@@@   
    @@@@@@@@  @@@@@@@@  @@@@@@@@@@@  @@@@@@@@@@@  @@@@@@@@  @@@@@@@@  
    @@!  @@@  @@!  @@@  @@! @@! @@!  @@! @@! @@!  @@!       @@!  @@@  
    !@!  @!@  !@!  @!@  !@! !@! !@!  !@! !@! !@!  !@!       !@!  @!@  
    @!@  !@!  @!@!@!@!  @!! !!@ @!@  @!! !!@ @!@  @!!!:!    @!@  !@!  
    !@!  !!!  !!!@!!!!  !@!   ! !@!  !@!   ! !@!  !!!!!:    !@!  !!!  
    !!:  !!!  !!:  !!!  !!:     !!:  !!:     !!:  !!:       !!:  !!!  
    :!:  !:!  :!:  !:!  :!:     :!:  :!:     :!:  :!:       :!:  !:!  
    :::: ::  ::   :::  :::     ::   :::     ::    :: ::::   :::: ::  
    :: :  :    :   : :   :      :     :      :    : :: ::   :: :  :   
                                                                    
                                                                    
    @@@  @@@   @@@@@@   @@@ @@@   @@@@@@    @@@@@@@@  @@@@@@@@     
    @@@  @@@  @@@@@@@@  @@@ @@@  @@@@@@@@  @@@@@@@@@  @@@@@@@@     
    @@!  @@@  @@!  @@@  @@! !@@  @@!  @@@  !@@        @@!          
    !@!  @!@  !@!  @!@  !@! @!!  !@!  @!@  !@!        !@!          
    @!@  !@!  @!@  !@!   !@!@!   @!@!@!@!  !@! @!@!@  @!!!:!       
    !@!  !!!  !@!  !!!    @!!!   !!!@!!!!  !!! !!@!!  !!!!!:       
    :!:  !!:  !!:  !!!    !!:    !!:  !!!  :!!   !!:  !!:          
        ::!!:!   :!:  !:!    :!:    :!:  !:!  :!:   !::  :!:          
        ::::    ::::: ::     ::    ::   :::   ::: ::::   :: ::::     
        :       : :  :      :      :   : :   :: :: :   : :: ::      
    """+CLEAR_SCREEN + RESET) 

#      Module Sailing SHip
# -----------------------------------------------------------
def sailing_ship():
    print(LIGHT_GRAY+UP*23+"""
    ▓                                            ░░░░░░░░░░▒▒            ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                                                 
▓                                             ▒▒▒▒▒▒▒▒▒▒▒▒           ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                                                
▓                                               ░▒▒▒▒▒▒▒▒▒▒▒▒░          ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                                                
▓                                                  ░▒▒▒▒▒▒▒▒▒▒            ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                                               
▓                                                   ░▒▒▒▒▒▒▒▒▒▒▒            ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                                              
▓                                                        ▒▒▒▒▒▒▒▒▒              ░▒▒▒▒▒▒▒▒▒▒▒▒▒                                              
▓                                                        ▒▒▒▒▒▒▒▒▒▒▒             ▒▒▒▒▒▒▒▒▒▒▒▒▒▒                                             
▓                                                         ▒▒▒▒▒▒▒▒▒▒▒░             ▒▒▒▒▒▒▒▒▒▒▒                                              
▓                                                             ░▒░▒▒▒▒                ░▒▒▒▒▒▒▒▒                                              
▓                                                                                                                                           
▓                             ░                     ▓▓▓▓▓▓▓     ▓▓▓▓▓▓▓     ▓▓▓▓▓▓▓     ▓▓▓▓▓▓▓                                             
▓                              ░                     ▓▓▓▓▓▓      ▓▓▓▓▓▓      ▓▓▓▓▓▓      ▓▓▓▓▓▓               ▓                             
▓                              ▓                     ▓     ▓     ▓     ▓     ▓     ▓     ▓     ▓              ▒                             
▓                               ▓                     ▓     ▓     ▓     ▓     ▓     ▒     ▓     ▒              ▓                            
▓                               ▓▓                                                                             ▒▓                           
▓                                ▓▓                    ▓     ▓     ▒     ▓           ▓     ▒     ▓              ▓▒                          
▓                                 ▓                                       ▓           ▓           ▓              ▓                          
▓                                 ▓▓              ▓▓▓▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ▓▓           ▓                         
▓                                  ▓▓          ▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒         ▓▓                        
▓                                  ▒▓▓         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓       ▓▓                        
▓                   ▒▒░░░░░░        ▓▓ ▒       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░ ▓▓          ░▒           
▓                    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓            
▓                      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓            
▓                       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒            
▓                      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓             
▓                    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓              
▓                   ▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓               
▓                   ▓                                                                                                     ▓                 
▓                    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                   
                                                                                                                                            
                                                                                                                                            
                                                                                                                                            
""")
    time.sleep(1)
    print(CLEAR_SCREEN)

    print(LIGHT_GRAY+UP*23+ """
    ▓                                                        ▓▓▓▓▓▓▓▓▓▓▓▒                                                                       
▓                                                        ░▓▓▓▓▓▓▓▓▓▓▓▒                                                                      
▓                                                           ▒▓▓▓▓▓▓▓▓▓▓▓                                                                    
▓                                                             ▒▓▓▓▓▓▓▓▓▓▓▓▒                                                                 
▓                                                               ▓▓▓▓▓▓▓▓▓▓▓                                                                 
▓                                                                   ░▓▓▓▓▓▓▓▓▓▓▓▓                                                           
▓                                                                    ▒▓▓▓▓▓▓▓▓▓▓▓                                                           
▓                                                                     ▒▓▓▓▓▓▓▓▓▓▓▓                                                          
▓                                                                         ▒▓▓▓▓▓▓▒                                                          
▓                                                                                                                                           
▓                             ░                     ▓▓▓▓▓▓▓     ▓▓▓▓▓▓▓     ▓▓▓▓▓▓▓     ▓▓▓▓▓▓▓                                             
▓                              ░                     ▓▓▓▓▓▓      ▓▓▓▓▓▓      ▓▓▓▓▓▓      ▓▓▓▓▓▓               ▓                             
▓                              ▓                     ▓     ▓     ▓     ▓     ▓     ▓     ▓     ▓              ▒                             
▓                               ▓                     ▓     ▓     ▓     ▓     ▓     ▒     ▓     ▒              ▓                            
▓                               ▓▓                                                                             ▒▓                           
▓                                ▓▓                    ▓     ▓     ▒     ▓           ▓     ▒     ▓              ▓▒                          
▓                                 ▓                                       ▓           ▓           ▓              ▓                          
▓                                 ▓▓              ▓▓▓▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ▓▓           ▓                         
▓                                  ▓▓          ▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒         ▓▓                        
▓                                  ▒▓▓         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓       ▓▓                        
▓                   ▒▒░░░░░░        ▓▓ ▒       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░ ▓▓          ░▒           
▓                    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓            
▓                      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓            
▓                       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒            
▓                      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓             
▓                    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓              
▓                   ▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓               
▓                   ▓                                                                                                     ▓                 
▓                    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                   
                                                                                                                                            
                                                                                                                                            
                                                                                                                                            
    """)
    time.sleep(1)    
    print(CLEAR_SCREEN)
    print(LIGHT_GRAY+UP*23+ """
    ▓                                            ░░░░░░░░░░▒▒            ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                                                 
▓                                             ▒▒▒▒▒▒▒▒▒▒▒▒           ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                                                
▓                                               ░▒▒▒▒▒▒▒▒▒▒▒▒░          ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                                                
▓                                                  ░▒▒▒▒▒▒▒▒▒▒            ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                                               
▓                                                   ░▒▒▒▒▒▒▒▒▒▒▒            ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                                              
▓                                                        ▒▒▒▒▒▒▒▒▒              ░▒▒▒▒▒▒▒▒▒▒▒▒▒                                              
▓                                                        ▒▒▒▒▒▒▒▒▒▒▒             ▒▒▒▒▒▒▒▒▒▒▒▒▒▒                                             
▓                                                         ▒▒▒▒▒▒▒▒▒▒▒░             ▒▒▒▒▒▒▒▒▒▒▒                                              
▓                                                             ░▒░▒▒▒▒                ░▒▒▒▒▒▒▒▒                                              
▓                                                                                                                                           
▓                             ░                     ▓▓▓▓▓▓▓     ▓▓▓▓▓▓▓     ▓▓▓▓▓▓▓     ▓▓▓▓▓▓▓                                             
▓                              ░                     ▓▓▓▓▓▓      ▓▓▓▓▓▓      ▓▓▓▓▓▓      ▓▓▓▓▓▓               ▓                             
▓                              ▓                     ▓     ▓     ▓     ▓     ▓     ▓     ▓     ▓              ▒                             
▓                               ▓                     ▓     ▓     ▓     ▓     ▓     ▒     ▓     ▒              ▓                            
▓                               ▓▓                                                                             ▒▓                           
▓                                ▓▓                    ▓     ▓     ▒     ▓           ▓     ▒     ▓              ▓▒                          
▓                                 ▓                                       ▓           ▓           ▓              ▓                          
▓                                 ▓▓              ▓▓▓▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ▓▓           ▓                         
▓                                  ▓▓          ▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒         ▓▓                        
▓                                  ▒▓▓         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓       ▓▓                        
▓                   ▒▒░░░░░░        ▓▓ ▒       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░ ▓▓          ░▒           
▓                    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓            
▓                      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓            
▓                       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒            
▓                      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓             
▓                    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓              
▓                   ▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓               
▓                   ▓                                                                                                     ▓                 
▓                    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                   
                                                                                                                                            
                                                                                                                                            
                                                                                                                                            
    """)
    time.sleep(1)    
    print(CLEAR_SCREEN)
    print(LIGHT_GRAY+UP*23+ """
    ▓                                                        ▓▓▓▓▓▓▓▓▓▓▓▒                                                                       
▓                                                        ░▓▓▓▓▓▓▓▓▓▓▓▒                                                                      
▓                                                           ▒▓▓▓▓▓▓▓▓▓▓▓                                                                    
▓                                                             ▒▓▓▓▓▓▓▓▓▓▓▓▒                                                                 
▓                                                               ▓▓▓▓▓▓▓▓▓▓▓                                                                 
▓                                                                   ░▓▓▓▓▓▓▓▓▓▓▓▓                                                           
▓                                                                    ▒▓▓▓▓▓▓▓▓▓▓▓                                                           
▓                                                                     ▒▓▓▓▓▓▓▓▓▓▓▓                                                          
▓                                                                         ▒▓▓▓▓▓▓▒                                                          
▓                                                                                                                                           
▓                             ░                     ▓▓▓▓▓▓▓     ▓▓▓▓▓▓▓     ▓▓▓▓▓▓▓     ▓▓▓▓▓▓▓                                             
▓                              ░                     ▓▓▓▓▓▓      ▓▓▓▓▓▓      ▓▓▓▓▓▓      ▓▓▓▓▓▓               ▓                             
▓                              ▓                     ▓     ▓     ▓     ▓     ▓     ▓     ▓     ▓              ▒                             
▓                               ▓                     ▓     ▓     ▓     ▓     ▓     ▒     ▓     ▒              ▓                            
▓                               ▓▓                                                                             ▒▓                           
▓                                ▓▓                    ▓     ▓     ▒     ▓           ▓     ▒     ▓              ▓▒                          
▓                                 ▓                                       ▓           ▓           ▓              ▓                          
▓                                 ▓▓              ▓▓▓▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ▓▓           ▓                         
▓                                  ▓▓          ▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒         ▓▓                        
▓                                  ▒▓▓         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓       ▓▓                        
▓                   ▒▒░░░░░░        ▓▓ ▒       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░ ▓▓          ░▒           
▓                    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓            
▓                      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓            
▓                       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒            
▓                      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓             
▓                    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓              
▓                   ▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓               
▓                   ▓                                                                                                     ▓                 
▓                    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                   
                                                                                                                                            
                                                                                                                                            
                                                                                                                                            
    """)
    time.sleep(1)
    

# ###########  Game over module
def game_over():

       print(CLEAR_SCREEN)
       #! --- White      
       print("""                                                             
                                                               
              @@@@@@@@   @@@@@@   @@@@@@@@@@   @@@@@@@@     
       @@@@@@@@@  @@@@@@@@  @@@@@@@@@@@  @@@@@@@@     
       !@@        @@!  @@@  @@! @@! @@!  @@!          
       !@!        !@!  @!@  !@! !@! !@!  !@!          
       !@! @!@!@  @!@!@!@!  @!! !!@ @!@  @!!!:!       
       !!! !!@!!  !!!@!!!!  !@!   ! !@!  !!!!!:       
       :!!   !!:  !!:  !!!  !!:     !!:  !!:          
       :!:   !::  :!:  !:!  :!:     :!:  :!:          
              ::: ::::  ::   :::  :::     ::    :: ::::     
              :: :: :    :   : :   :      :    : :: ::      
                                                        
                                                        
              @@@@@@   @@@  @@@  @@@@@@@@  @@@@@@@          
       @@@@@@@@  @@@  @@@  @@@@@@@@  @@@@@@@@         
       @@!  @@@  @@!  @@@  @@!       @@!  @@@         
       !@!  @!@  !@!  @!@  !@!       !@!  @!@         
       @!@  !@!  @!@  !@!  @!!!:!    @!@!!@!          
       !@!  !!!  !@!  !!!  !!!!!:    !!@!@!           
       !!:  !!!  :!:  !!:  !!:       !!: :!!          
       :!:  !:!   ::!!:!   :!:       :!:  !:!         
       ::::: ::    ::::     :: ::::  ::   :::         
              : :  :      :      : :: ::    :   : :                                                                
       """)
       delay_intro(RED+UP*25+"""                                                                  
                                                               
              @@@@@@@@   @@@@@@   @@@@@@@@@@   @@@@@@@@     
       @@@@@@@@@  @@@@@@@@  @@@@@@@@@@@  @@@@@@@@     
       !@@        @@!  @@@  @@! @@! @@!  @@!          
       !@!        !@!  @!@  !@! !@! !@!  !@!          
       !@! @!@!@  @!@!@!@!  @!! !!@ @!@  @!!!:!       
       !!! !!@!!  !!!@!!!!  !@!   ! !@!  !!!!!:       
       :!!   !!:  !!:  !!!  !!:     !!:  !!:          
       :!:   !::  :!:  !:!  :!:     :!:  :!:          
              ::: ::::  ::   :::  :::     ::    :: ::::     
              :: :: :    :   : :   :      :    : :: ::      
                                                        
                                                        
              @@@@@@   @@@  @@@  @@@@@@@@  @@@@@@@          
       @@@@@@@@  @@@  @@@  @@@@@@@@  @@@@@@@@         
       @@!  @@@  @@!  @@@  @@!       @@!  @@@         
       !@!  @!@  !@!  @!@  !@!       !@!  @!@         
       @!@  !@!  @!@  !@!  @!!!:!    @!@!!@!          
       !@!  !!!  !@!  !!!  !!!!!:    !!@!@!           
       !!:  !!!  :!:  !!:  !!:       !!: :!!          
       :!:  !:!   ::!!:!   :!:       :!:  !:!         
       ::::: ::    ::::     :: ::::  ::   :::         
              : :  :      :      : :: ::    :   : :                                                              
       """+ RESET)                                                                                                                                    

def goto_lagoon():
    # Qaiser:
    # Called by BEACH.  Goes to TEMPLE, VOLCANO
    print(GREEN + """
                    *✲*´*。.❄¯*✲。❄。*¨`*✲´*。❄¨`*✲。❄。*`*
                    *╔════════════ ༺❀༻❤༺❀༻ ════════════╗*
                    *♥*❄¯*✲❄♫♪♩░B░E░A░U░T░I░F░U░L░ ♫♫♪❄¯*✲❄
                    *╚════════════ ༺❀༻❤༺❀༻ ════════════╝*
                    *✲*´*。.❄¯*✲。❄。*¨`*✲´*。❄¨`*✲。❄。*`*
You wander by a beautiful blue lagoon; peaceful and tranquil. A place to rest and relax.
From here you can go to a ruined Temple or towards the volcano. Or go back to the beach.
""")
    choices = [
        "Go back to the beach",
        "Go to the Temple",
        "Go to the Volcano",
        "Rest here, maybe have a swim and a siesta"
    ]
    choice = get_input(choices)
    if choice == 1:
        goto_beach()
    elif choice == 2:
        print("You head towards the ruined temple")
        goto_temple()
    elif choice == 3:
        print("A volcano - what fun!")
        # goto_volcano()
    elif choice == 4:
        qprint(GREEN + "A nice relaxing swim - just what you wanted in this tropical paradise")
        goto_lagoon()
    else:  # should never get a choice this high..
        goto_death("SYSTEM ERROR #zzzzzz")

# -----------------------------------------------------------  BOARD_HIP functions  ------------


def narr_print(string, colour = ITALIC + LIGHT_WHITE, delay = 0): #! -- Narrator Print
    for letters in string:
        sys.stdout.write(colour +letters +RESET )
        sys.stdout.flush()
        time.sleep(delay)
    print("")

def delay_talk(string, colour = YELLOW, delay = 0):
    for letters in string:
        sys.stdout.write(colour+letters+RESET)
        sys.stdout.flush()
        time.sleep(delay)


def board_ship():
    narr_print("You walk through the Cunard Building, walking past other guests who are checking in & checking out\n")
    narr_print("You make your way outside to the gand way & see the ship you'll be boarding\n")
    #insert ship image
    narr_print("its bigger than you thought,\nwhich makes you feel safer\nAt the gangway another gentlemen takes your ticket and allows you passage\n you make your way across and now you're finally aboard the ship")
    narr_print("You're finally aboard, you think, whats the first thing to do....[Enter Answer]")
    answer = input()
    narr_print(f"You think about {answer}, but you realise you need to drop off your bags\nyou walk through the grand hall of the ship & head towards your cabin,\nits a windowless inside cabin...not what you requested, but you're too tired to complain\nyou drop off your bags & think about {answer} but realise you can do that later maybe,\nyou head to bed for a quick nap, so you can enjoy your evening better")
    input("Press <enter> to continue")
    sailing_ship()
    print("Suddenly there you uare shipwrecked!! You manage to escape and find an island")
    goto_beach()

def secret_question():
    delay_talk("Ok now that we have everything check, I can see you are on the guest list, but for a security check\ncan you please confirm your occupation")
    narr_print("What is your occupation\n")
    occupation =[ "[1] Engineer", "[2] Doctor", "[3] Retired", "[4] You're actually the captain of the ship"]
    for jobs in occupation:
        print(jobs)
    answer = input()
    answer =int(answer)
    if answer== 1:
        narr_print("You smile & explain you are actually an engineer, who use to work on ships many years ago, the Booth Worker is impressed, that you and ships have a history")
        delay_talk(f"Very instresting {name}, please enjoy your voyage, if there are any issues, we'll know to ask you for help")
        narr_print("His joke was aimed to calm you, but instead the idea of something bad happening, makes you paranoid about the voyage ahead....")
        board_ship()
    elif answer == 2:
        narr_print("Opening up your bag on the desk, you pull out your newly Certified Doctrone identification")
        delay_talk("Oh very nice, another Doctor on the ship, we'll knock on your cabin if your needed")
        narr_print("You think, this isn't going to be a relaxing voyage.....")
        board_ship()
    elif answer == 3:
        narr_print("You explain that you're retired & looking forward to a relaxing cruise, before you start your retirement in the new world")
        global age
        if age <= 55:
            narr_print("As you state your plans the gentlemen, looks suprised, that you have retired at a much younger age than normal, they look enveous")
            delay_talk("Oh...well...welcome aboard & please enjoy your retirement voyage")
            board_ship()
        elif age >=55:
            narr_print("You state your plans and explain abit about your life story....\nThe Booth Worker looks like hes heard it all before...")   
            delay_talk(f"Yes {name}, that is very interesting...")
            narr_print("He wuickly passes you your boarding pass and waves you to move on")
            board_ship()
    elif answer == 4:
        narr_print("You put on your straight face & demand that the worker shows respect to the Captain of this ship\n he laughs")
        delay_talk("Oh yes Sir!!, sorry to not recognise you, your vessel awaits....")
        narr_print("He gives you a sarcastic salute")
        delay_talk("Please answer the question or I won't be able to confirm")
        secret_question()
    else:
        narr_print("Don't think thats an occupation.....Try again")
        secret_question()    

def pass_back_location():
    delay_talk(f"...and last part to check is where are you from, can you confirm you are from {where_from}?[Y/N]")
    answer = input().upper()
    if answer == "Y":
        delay_talk(f"Ok,{name}, so your from {where_from}, never been there myself")
        secret_question()
    elif answer == "N":
        delay_talk("So your not from {where_from}, shame these are filled in with ink & not pen\nbut then again, it stops fake ID checks...\nPlease take another form and fill all sections correctly please")
        narr_print("He passes you another form to fill out again")
        id_form()
    else:
        delay_talk("Pardon me, I asked to confirm where you are from, a simple Yes or No will do?")
        pass_back_name()

def pass_back_age():
    delay_talk(f"Ok and can you confirm you are {age}")
    answer = input().upper()
    if answer == "Y":
        delay_talk(f"Ok,{name}, your age is {age} next question")
        pass_back_location()
    elif answer == "N":
        delay_talk("Well you will have to do another form now sadly, as these ID forms cant be editied\n")
        narr_print("He passes you another form to fill out again")
        id_form()
    else:
        delay_talk("Pardon me, I asked to confirm your age?")
        pass_back_name()

def pass_back_name():
    narr_print("You pass the form back to the gentlmen")
    delay_talk("Ok, everything seems to be in order, I'll just double check with you....\n")
    delay_talk(f"Your name is {name}, is this correct?[Y/N]")
    answer = input().upper()
    if answer == "Y":
        delay_talk(f"Ok, {name}, next question")
        pass_back_age()
    elif answer == "N":
        delay_talk("Well you will have to do another form sadly\n")
        narr_print("He passes you another form to fill out again")
        id_form()
    else:
        delay_talk("Pardon me?")
        pass_back_name()

def id_form():
    global name 
    global age 
    global where_from
    narr_print("You look down at the form, you just want this over with, so you can board....\n")
    print("Please fill your name in below")
    name = input("")
    print("Age")
    age = input("")
    age = int(age)
    print("Place of home")
    where_from=input()
    pass_back_name()

def id_check():
    narr_print("The Booth worker, starts to get impatient....")
    delay_talk("Excuse me, if you can fill in this form, I can see if your on the guest list and we can get you boarded soon\n")
    narr_print("The gentlemen hands you over a form to fill in")
    id_form()

def stress_check():
    global stress_level
    if stress_level <= 2:
        ticket_check()
    elif stress_level >=3:
        id_check()

def ticket_check():
    global stress_level
    narr_print("You think where should you check next...\n")
    ticket_list = ["[1]Check Desk", "[2]Check Bag", "[3]Search Luggage", "[4]Check Coat Pocket"]
    for check in ticket_list:
        print(check)
    answer = input()
    answer =int(answer)
    if answer == 1:
        stress_level += 1
        print("You look down at the desk, you didn't leave it there, 'What did I do with it' you mutter...")
        stress_check()
    elif answer ==2:
        stress_level += 1
        print("You fantactly search your hand luggage, its not there either")
        stress_check()
    elif answer ==3:
        stress_level += 1
        print("After opening your luggage and routing through it for what feels like ages, you realise its not there either")
        stress_check()
    elif answer ==4:
        stress_level += 1
        narr_print("Its not in your pocket, but maybe you put it in another pocket you think to yourself...\n")
        time.sleep(1)
        narr_print("...............")
        narr_print("Do you go to check all the pockets in the coat?[Y/N]")
        pocket_answer = input().upper()
        if pocket_answer == "Y":
            stress_level += 1
            print("You search another pocket, still haven't found it.....")
            stress_check() 
        else:
            narr_print("The Booth Worker looks confused & reminds you, that its your boarding pass he needs....")
            stress_check()


def board_check():
    print(CLEAR_SCREEN)
    narr_print("You've been travelling half way across England, collecting the requested documents to grant you entry into the new world,\n a sea liner is waiting docked in Liverpool, awating to take you across the Alantic")
    time.sleep(1)
    narr_print("The bus stops, you've arrived at the entrace to the Cunard Building,\n you exit the bus, making sure you have all your belongings,\n you look up as the sun hangs high, you make your way to the entrance and join the queue,\n you notice the queue seems exceptionly long, but you don't give it a 2nd thought.......\n you feel like you have been waiting for hours, but notice the midday sun still burning, you check your watch........\n less than half an hour has passed or maybe you forgot to wind your watch again\n You think to yourself, 'How much longer do i have to wait'")
    time.sleep(1)
    narr_print("With your thoughts running away, you don't realise another boarding booth has opened,\n a young gentleman behined the booth whistles for your attention,\n you quickly snap out of your day dream & move ahead of the crowd with your lungage in tow.\n")
    delay_talk("Thank you ladies & gentle, we do apoligise for the delay on checking your boarding passes & are assigning more booth workers\n don't worry the ship will be making up for lost time & you will still make the arrival in 6 days time by 1:00PM\n")
    narr_print("The Booth worker waves you forward.... you approuch & lean on the desk for some purchase & rest\n")
    delay_talk("Hello, welcome to Cunard Cruises, thank you for being patient with us, may I see your boarding pass?\n")
    narr_print("It's been a long day, getting here & you've forgotten where you put it for safe keeping\n")
    ticket_check()

# =====================  Call main game function to start if run from command line  ======================
if __name__ == "__main__":
    vod()

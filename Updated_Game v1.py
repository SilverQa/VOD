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
name = ""
age = 0
where_from = ""
stress_level = 0
life_jacket = 0

def vod():
    global inventory
    game_intro()
    time.sleep(1.5)
    board_check()

#   -------------  Common functions declared here   ------------------

def goto_death_sink(string):
    global inventory
    game_over()
    qprint(PURPLE + f"\n{string} " + LIGHT_RED + UNDERLINE + "YOU HAVE DIED!!" + RESET)
    print(f"\nYou had {inventory} in your possesion.")
    # <exit program>
    time.sleep(1.5)
    sinking_ship()
    quit()



def goto_death(string):
    global inventory
    game_over()
    qprint(PURPLE + f"\n{string} " + LIGHT_RED + UNDERLINE + "YOU HAVE DIED!!" + RESET)
    print(f"\nYou had {inventory} in your possesion.")
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
    print("(Enter 0 to quit)")
    termx, termy = os.get_terminal_size()
    # print '0 to exit' 20 chars from the right of the screen. then linefeed back to start of line and ask question
    choice = input(" " * (termx - 20) + CYAN +"(0 to QUIT)" + LIGHT_WHITE+"\rWhat would you like to do? " )
    
    # Input validation - make sure they entered a single digit
    if len(choice) > 1 or not choice.isdigit():  
        print("Please choose a single NUMBER from the choices\n")
        choice = get_input(choices)
    else: choice = int(choice) # now we are sure it is a single digit.
    if choice == 0:
        goto_death(
            "You have quit the island and will never now discover it's mysteries..\n")
    if choice > number - 1:
        print("I didn't realise that was an option. Please choose a number from the choices\n")
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

def goto_beach():
    print(YELLOW + """
    *✲*´*。.❄¯*✲。❄。*¨`*✲´*。❄¨`*
    *╔═══════ ༺❀༻❤༺❀༻ ═══════╗*
    *♥*❄¯*    THE SHORE     ♪❄¯*✲❄
    *╚═══════ ༺❀༻❤༺❀༻ ═══════╝*
    *✲*´*。.❄¯*✲。❄。*¨`*✲´*。❄¨`*
    """+ RESET)

    print("welcome to skull island beach.\n")
    print ("your mission is to escape from the zombies.\n")
    phase1 =input("You're at a skull island. where do you want to go? 'left' or 'right' \n").lower()
    if phase1 =="left":
        phase2 = input("You've come to the beach. There is ship in the middle there. 'wait' for the boat, 'swim' across.\n").lower()
        if phase2 == "wait":
            print("""
*° ☆ ° ˛*˛☆_Π____*_*˚☆*
*˚ ˛★˛•˚ */______/ ~＼。˚ ˚
*˚ ˛•˛•˚🌈｜ 田田 ｜門｜ ˚*
*🌴╬═🌴╬╬🌴╬╬🌴═╬╬═🌴*╬╬🌴\n""")
            phase3 = input("You arrive at the canoe side. There are 3 houses there with diffrent color.one blue, one grey and one red. which color do you choose? \n").lower()
            if phase3 == "blue":
                print(" it is a room full of fire.Game over.\n")
                goto_death("Not the Bees!!\n")
            elif phase3 == "grey":
                print("you found the way out! you manage to escape the zombies and run for safety.\n")
                goto_lagoon()
            elif phase3 == "red":
                print("you enter a house of zombies. Game over.\n")
                goto_death("Zombie lunchtime!\n")
            elif phase3 =="jungle":
                print("you get ambushed by different animals. Game over.\n")
                goto_death("Eaten as a snack for a tiger\n")
            else:
                print(" you choose a house that does not open again. Game over.\n")
                goto_death("Trapped!\n")
        else:  # swim
            print("You go for a lovely swim, just avoiding the sharks.  You come to a lagoon\n")
            goto_lagoon()
    else:
        print("You go right and come to a lagoon\n")
        goto_lagoon()
# -----------------------------------------------------------------

def goto_temple():
    # TEMPLE location in skull island
    # Qaiser:
    # Comes from LAGOON.  Goes to TOMB, BEACH
    global inventory
    print("""                              ஜ۩۞۩ஜ 
🌴🌴🌴🌴 You stumble into a clearing, before you are the overgrown remains of an exotic temple 🌴
Glints of gold remain on the walls. Lured by the promise of treasure and shelter you enter...
Further on you can see what looks like the entrance to a tomb.\n
""")
    choices = ["Lets explore that tomb."]
    if ("DIAMOND" not in inventory) and ("STATUE" not in inventory): # Havent already got it or swapped with statue
        choices.append("That diamond looks interesting!  Try and pick it up.\n")
        print("There is a large stone statue of a Sphinx here. Nestled within its paws is a massive Diamond.\n")  

    choice = get_input(choices) # only need to check for 1st choice. 2nd choice (if there) will run be default.
    if choice == 1:
        goto_tomb()

    print("The Sphinx stirs itself to life with the deep rumble of living stone and intones:\n")
    print('"I am the guardian of this gem and I despise ignorance in all beings."\n')
    print('"You must answer three questions correctly to win the gem. and '+RED+'SURVIVE"\n'+RESET)
    print("First question:\n")

    question1 = CYAN+"What goes on four feet in the morning, two feet at noon, and three feet in the evening?\n"+RESET
    question2 = CYAN+"What is the output of this Python program:\n\n" + \
        LIGHT_WHITE+"   def func1():\n    x = 50\n    return x\n    func1()\n   print(x)"+RESET
    question3 = CYAN+"What is the airspeed velocity of an unladen swallow?\n"+RESET

    print(question1)
    choices = [
        "Woman (and man of course)",
        "Elephants",
        "Fishes"
    ]
    choice = get_input(choices)
    if choice == 1:
        print("The Sphinx shuffles uneasily and mumbles 'lucky guess'\n")
        print(question2)
        choices = ['""  (Blank string)', "NameError:", "50","None\n"]
        choice = get_input(choices)
        if choice == 2:
            print('"Well, I didn' + "'" +'t think you were going to get that one!" - the Sphinx exclaims\n')
            print(question3)
            choices = ["73mph", "20.1mph", "58mph",'Do you mean the African or the European Swallow?\n']
            choice = get_input(choices)
            if choice == 4:
                qprint("A startled look crosses the Sphinx face:\n")
                qprint('"Huh? I... I dont know that..\n"')
                qprint('"ARRGGH! I cannot answer my own question - I am defeated!!"\n')
                qprint("The Sphinx slinks away leaving the glittering diamond, shooting you a dirty look.\n", 0.1)
                if "DIAMOND" in inventory:
                    print("You already have a Diamond!\n")
                else:
                    inventory.append("DIAMOND")
                qprint(f"You have acquired a Diamond. You now possess {inventory}. You head deeper into the temple tomb...\n")
                goto_tomb()   # Passed the Sphinx, go to next room
            else:
                print("You dont watch much Monty Python do you...\n")
                goto_death("The Sphinx gently blows on you, and you are carried away by a great wind - straight into the volcano!\n")
        else:
            print("And I thought you were a Python whizz!\n")
            goto_death("The giant Sphinx, boring of this game, simply sits on you...\n")
    else:
        print("A riddle as old as the ages. And you got it wrong.\n")
        goto_death("The giant Sphinx pounces on you and eats you up as a teatime snack!\n")

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
    AAARGGHH! (._.)
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
    for i in range(1, termx - 37):    # roll to end of screen - 40 chars
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
    print("If your reactions are quick enough you might reach the door before it crushes you\n\n\n\n")
    animate_ball()

    print(f"{RED}{NEGATIVE}PLEASE ENTER THE {RESET}{LIGHT_CYAN}{UNDERLINE}True{RED}{NEGATIVE} ANSWER IN UNDER  {RESET}{YELLOW} {amount_time} {RED} {NEGATIVE} SECONDS TO DODGE THE ",end='')
    print(f"{ITALIC}BALL OF DOOM {RESET}{LIGHT_CYAN}")
    choices = [
        "2 + 2 = 4",
        "Garfield the cat hates lasagne",
        "The Python expression:    "+LIGHT_WHITE+"'x = 21; x % 7 == 1'"+LIGHT_CYAN,
        "I love the songs of James Blunt",
        "Trump is still President",
        "The Elephant is the only creature that cannot jump",
        "Lightning never strikes twice\n"
        ]
    # need to randomise the choices...
    random.shuffle(choices)

    now = time.time()
    choice = get_input(choices)
    elapsed = time.time() - now
    print(RESET)
    if elapsed > amount_time:
        print("Didnt make it, you took","{:.3f}".format(elapsed),"seconds instead of\n",amount_time)
        goto_death("Crushed by a huge ball - what a way to go!\n")
    if choices.index("2 + 2 = 4") + 1 != choice:
        print("Oooh, wrong answer. You meet the same fate as the last hat-wearing, whip-bearing adventurer\n")
        goto_death("Just like this rolling stone, you gathered no moss.\n")
    qprint("You leap through the door with the merest whisker to spare!.\n ")
    print(f"You took","{:.3f}".format(elapsed),"seconds out of", amount_time)
    print("The stone door slams shut behind you, sending you tumbling down a steep slope towards..\n")
    goto_lagoon()

def goto_tomb():
    # Qaiser:
    # Called by TEMPLE.  Goes to LAGOON
    global stress_level, inventory

    print("                        ▂▃▅▇█▓▒░۩۞۩ ۩۞۩░▒▓█▇▅▃▂")
    print(f"{DARK_GRAY}In the damp gloom of the tomb you feel the hairs on your neck standing up\n")
    qprint("(maybe you should stop rubbing that balloon you found earlier\n)", 0.001)
    if "STATUE" in inventory:
        qprint("You have seen enough of this deathtrap, you swiftly move though the cavern door.")
        goto_lagoon()
    qprint(f"\n{PURPLE}The atmosphere feels tense, you should be ready to act quickly{DARK_GRAY}\n")
    time.sleep(0.5)
    print("There is a small ornately decorated chamber in the middle of the tunnel with a closed solid stone door",end='')
    if "FEDORA" not in inventory:  print(",and a hat.",end='')
    print("\nThere seems to be a skeletal hand crushed under the door, like it was reaching for the hat at the last moment but missed.. How strange.\n")
    print(f"On a solid gold pedastal sits a beautiful glowing crystal statue inlaid with gold and silver. {GREEN}It calls to you...{DARK_GRAY}\n")
    
    choices = [
        "Pick up the hat - it looks kinda cool and he doesn't need it anymore",
        "Continue down the dark tunnel (it's very dark)",
        "Pick up the statue\n"
    ]
    if "DIAMOND" in inventory:
        choices.append("Carefully replace the statue with the diamond\n")
    if "FEDORA" in inventory: choices[0] = "Examine your hat again\n"
    
    choice = get_input(choices)
    if choice == 1:
        print(f"{LIGHT_WHITE}That is one good looking Fedora.{RESET}\nIt fits like a glove and you instantly feel cooler like Hans Solo in that Star Trek movie.\n ")
        print("(You might react faster with this fine hat. Should keep your head warm as well)")
        if "FEDORA" not in inventory: inventory.append("FEDORA")
        if stress_level > 0: stress_level -= 10
        goto_tomb()
    elif choice == 3:
        qprint("Your hand moves almost of its' own accord and plucks the statue from the plinth.\n")
        qprint(RED+"Of course it's a trap!\n     "+RESET)
        print("You will have to be quick to escape from here!\n")
        roller_ball()
    elif choice == 2:
        qprint(f"{DARK_GRAY}As you continue jauntily down the tunnel whistling a happy tune it get darker.. and darker...\n")
        time.sleep(0.25)
        qprint("🌹ڰۣڿڰۣڿஇღԑ̮̑❀ঙ❀ღڰۣڿڰۣڿஇ🌹\nThere are eerie carvings on the wall and what looks like\n")
        qprint("another skeleton squashed flat on the floor.\n")
        qprint("Are you really, really sure you want to do this or would you prefer to do something else..\n")
        x = input("Anything else really. Go back, look at the carvings or skeleton, or continue forward?\n"+LIGHT_CYAN)
        print(f"{RESET}Good choice, too late.. Just as you are about to {x} a 'click' sounds under your foot as a hidden switch activates\n")
        print("You will have to be much quicker to escape from here..\n")
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
            qprint(f"{YELLOW}Not quite carefully enough however. A chill wind blows down your neck and you shiver\n")
            qprint("A slight 'click' sounds out in the still air and the pedastal shakes.\n")
            print("You should have enough time to dodge the ball from here though..\n")
            inventory.remove("DIAMOND")
            inventory.append("STATUE")
            roller_ball(+3.0)
    else:  # should never get a choice this high..
        goto_death("SYSTEM ERROR #zzzzzz\n")

## ------------------------------------------  volcano ----------------------------
def fight_skeletons():
    "Fight against skeletons!\n"
    class Skeleton:
        health = 3

        def __init__(self):
            print("A bony skeleton (is there any other kind) claws it's way out of the ground.\n")

        def hit(self, hits = 1):
            if (random.randint(1,10)) < 8:   # 80%
                self.health -= hits
                print(LIGHT_WHITE + f"You land a hit on the skeleton with the magic dagger. It has {self.health} health left\n"+RESET)
            else: print(PURPLE + "You flail wildly with the dagger and manage to miss a clumsy undead pile of bones\n"+RESET)
            if self.health <= 0: 
                print(LIGHT_BLUE+UNDERLINE+"With a mighty blow you have skilled a kellington!\n"+RESET)

        def attack(self):
            # 50% chance of hitting. could have modifiers later??
            if random.randint(2,3) == 2:
                print(YELLOW+"The skeleton attacks, landing a hit on you. Ouch!\n"+RESET)
                return(1)
            else:
                print("Not all the bones are connected on this one - you easily evade the clumsy stab\n")
                return(0)

    print("You are going to fight 2 skeletons, each with 3 health. You have 5 health\n")
    print("You have a 80% chance to hit the skeletons. They have a 50% chance to hit you. Good luck!\n")
    health = 5
    dexterity = 0

    skel1 = Skeleton()
    skel2 = Skeleton()
    round = 1
    while skel1.health + skel2.health > 0:
        choices = []
        print(LIGHT_CYAN + f"Round {round}:  You have {health} points left. Skeletons points are 1:{skel1.health}  2:{skel2.health}")
        if skel1.health > 0: choices.append(f"First Skeleton ({skel1.health})")
        if skel2.health > 0: choices.append(f"Second Skeleton ({skel2.health})")
        choice=get_input(choices)
        if choice == 1: 
            # hack for changing menu places if killed 1st one first, then 2nd becomes first! Clear as mud eh :)
            if skel1.health <= 0: skel2.hit()
            else: skel1.hit()
        else:
            skel2.hit()
                
        print("The skeletons now attack you!\n")
        if skel1.health > 0: health -= skel1.attack()
        if skel2.health > 0: health -= skel2.attack()
        if health <= 0:
            qprint("The skeletons continue hacking at your lifeless body until the spirits are appeased.\n")
            time.sleep(2)
            goto_death("Soon you will be skeleton yourself...\n")

        round += 1

    print("You have defeated the skeletons and nothing now lies in your path. You take the canoe and ESCAPE!!\n")
    goto_lagoon()  #  goto_escape() 



def goto_volcano():
    # Qaiser:
    # Called by TEMPLE.  Goes to ESCAPE
    print(PURPLE+"""
ڰۣڿڰۣڿஇღԑ̮̑ঙღڰۣڿڰۣڿஇ  💕💕💕 ❉⊱•═•⊰❉⊱•═•⊰❉⊱•═•⊰❉  💕💕💕  ڰۣڿڰۣڿஇღԑ̮̑ঙღڰۣڿڰۣڿஇ
You find yourself at near the stony base of the smoldering volcano.
There is a an ancient stained altar here.  Beyond the altar you can see a good looking Canoe
The stench of sulpher is mixed with old incense and..the greasy smell of evil magic... Obeah!
There is a long dagger inscribed with eldritch runes sitting on the altar.
"""+RESET)
    choices = [
        "I've seen too many films like this - go back to the lagoon and be nice and safe",
        "Pick up the dagger",
        "Examine the altar more closely\n"
    ]
    choice = get_input(choices)
    if choice == 1:
        goto_lagoon()
    elif choice == 2:
        print("""
Picking up the dagger, you sense the anger of the spirits at your desacration of their altar\n
A swirl of magic surrounds the altar shaking the ground. The earth heaves and clawing their way from their resting place:\n
""")
        qprint(LIGHT_RED+"SKELETONS!!!!    \nYou will have to fight these skeletons to get past\n"+RESET)
        print("""
                        .___.
                     ,-^     ^-.
      (@_           /           \
   _   ) \_________/  __     __  \__________________________
(_)@8@8{}<_________| /  \   /  \ |___________________________>
       )_/         | \__/   \__/ |
      (@            \    /|\    /
                     \   \_/   /
                      |       |
                      |+H+H+H+|
                      \       /
                       ^-----^
""")
        if "STATUE" in inventory: 
            qprint("The skeletons notice the glowing statue you hold. The spirits quiet... and depart howling in the wind\n")
            qprint("The way is clear. You can escape this mysterious and cursed isle - you take the canoe and paddle\n")
            qprint(f"away, with an enormously valuable glowing statue.  {LIGHT_CYAN + UNDERLINE} You are rescued and live the rest of your long life happy.\n")
            goto_lagoon()  #   goto_escpae()
        else: fight_skeletons()
    elif choice == 3:
        qprint(f"The altar is stained by time and what looks like..{LIGHT_RED} blood\n"+RESET)
        print("There are some strange writings on the side of the altar\n")
        goto_volcano()        
    else:  # should never get a choice this high..
        goto_death("SYSTEM ERROR #zzzzzz\n")


# ######################## SHIP ################################################################################
# ###########  Ship intro banner module
#Narrating TEXT PRINT FUNCTION

def narr_print(string, colour = ITALIC + LIGHT_WHITE, delay = 0): #! -- Narrator Print
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

    delay_intro("                               Game Project Created by\n                                    Antony Borji, \n                                    Qaiser Adams \n                                         &\n                                  Kafila Olatinwa")
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
            :!:       :!:  :!:  !:!  :!:  !:!  :!:                  
            ::        ::   ::   ::   ::   :::  :: ::::              
            :         :    ::   :    :    : :  : ::: :              
                                                                    
                                                                    
    @@@@@@@    @@@@@@   @@@@@@@@@@   @@@@@@@@@@   @@@@@@@@  @@@@@@@   
    @@@@@@@@  @@@@@@@@  @@@@@@@@@@@  @@@@@@@@@@@  @@@@@@@@  @@@@@@@@  
    @@!  @@@  @@!  @@@  @@! @@! @@!  @@! @@! @@!  @@!       @@!  @@@  
    !@!  @!@  !@!  @!@  !@! !@! !@!  !@! !@! !@!  !@!       !@!  @!@  
    @!@  !@!  @!@!@!@!  @!! !!@ @!@  @!! !!@ @!@  @!!!:!    @!@  !@!  
    !@!  !!!  !!!@!!!!  !@!   ! !@!  !@!   ! !@!  !!!!!:    !@!  !!!  
    !!:  !!!  !!:  !!!  !!:     !!:  !!:     !!:  !!:       !!:  !!!  
    :!:  !:!  :!:  !:!  :!:     :!:  :!:     :!:  :!:       :!:  !:!  
    :::: ::   ::   :::  :::     ::   :::     ::   :: ::::   :::: ::  
    :: : :    :    : :   :      :     :      :    : :: ::   :: : :   
                                                                    
                                                                    
    @@@  @@@   @@@@@@   @@@ @@@   @@@@@@    @@@@@@@@  @@@@@@@@     
    @@@  @@@  @@@@@@@@  @@@ @@@  @@@@@@@@  @@@@@@@@@  @@@@@@@@     
    @@!  @@@  @@!  @@@  @@! !@@  @@!  @@@  !@@        @@!          
    !@!  @!@  !@!  @!@  !@! @!!  !@!  @!@  !@!        !@!          
    @!@  !@!  @!@  !@!   !@!@!   @!@!@!@!  !@! @!@!@  @!!!:!       
    !@!  !!!  !@!  !!!    @!!!   !!!@!!!!  !!! !!@!!  !!!!!:       
    :!:  !!:  !!:  !!!    !!:    !!:  !!!  :!!   !!:  !!:          
    ::!!:!    :!:  !:!    :!:    :!:  !:!  :!:   !::  :!:          
    ::::      ::::: ::     ::    ::   :::   ::: ::::  :: ::::     
    :          : :  :      :     :    : :   :: :: :   : :: ::  
    """)
    delay_intro(RED+UP*35+"""                                                                  
            @@@@@@@@  @@@  @@@  @@@   @@@@@@   @@@                   
            @@@@@@@@  @@@  @@@@ @@@  @@@@@@@@  @@@                   
            @@!       @@!  @@!@!@@@  @@!  @@@  @@!                   
            !@!       !@!  !@!!@!@!  !@!  @!@  !@!                   
            @!!!:!    !!@  @!@ !!@!  @!@!@!@!  @!!                   
            !!!!!:    !!!  !@!  !!!  !!!@!!!!  !!!                   
            !!:       !!:  !!:  !!!  !!:  !!!  !!:                   
            :!:       :!:  :!:  !:!  :!:  !:!  :!:                  
            ::        ::   ::   ::   ::   :::  :: ::::              
            :         :    ::   :    :    : :  : ::: :              
                                                                    
                                                                    
    @@@@@@@    @@@@@@   @@@@@@@@@@   @@@@@@@@@@   @@@@@@@@  @@@@@@@   
    @@@@@@@@  @@@@@@@@  @@@@@@@@@@@  @@@@@@@@@@@  @@@@@@@@  @@@@@@@@  
    @@!  @@@  @@!  @@@  @@! @@! @@!  @@! @@! @@!  @@!       @@!  @@@  
    !@!  @!@  !@!  @!@  !@! !@! !@!  !@! !@! !@!  !@!       !@!  @!@  
    @!@  !@!  @!@!@!@!  @!! !!@ @!@  @!! !!@ @!@  @!!!:!    @!@  !@!  
    !@!  !!!  !!!@!!!!  !@!   ! !@!  !@!   ! !@!  !!!!!:    !@!  !!!  
    !!:  !!!  !!:  !!!  !!:     !!:  !!:     !!:  !!:       !!:  !!!  
    :!:  !:!  :!:  !:!  :!:     :!:  :!:     :!:  :!:       :!:  !:!  
    :::: ::   ::   :::  :::     ::   :::     ::   :: ::::   :::: ::  
    :: : :    :    : :   :      :     :      :    : :: ::   :: : :   
                                                                    
                                                                    
    @@@  @@@   @@@@@@   @@@ @@@   @@@@@@    @@@@@@@@  @@@@@@@@     
    @@@  @@@  @@@@@@@@  @@@ @@@  @@@@@@@@  @@@@@@@@@  @@@@@@@@     
    @@!  @@@  @@!  @@@  @@! !@@  @@!  @@@  !@@        @@!          
    !@!  @!@  !@!  @!@  !@! @!!  !@!  @!@  !@!        !@!          
    @!@  !@!  @!@  !@!   !@!@!   @!@!@!@!  !@! @!@!@  @!!!:!       
    !@!  !!!  !@!  !!!    @!!!   !!!@!!!!  !!! !!@!!  !!!!!:       
    :!:  !!:  !!:  !!!    !!:    !!:  !!!  :!!   !!:  !!:          
    ::!!:!    :!:  !:!    :!:    :!:  !:!  :!:   !::  :!:          
    ::::      ::::: ::     ::    ::   :::   ::: ::::  :: ::::     
    :          : :  :      :     :    : :   :: :: :   : :: ::  
    \n"""+ RESET) 
def docked_ship_pic():
    print(LIGHT_GRAY+"""
                                                            ░                                                              
                                                            ▓                                                              
                                                            ░                                                              
                                                            ▓▓                                                              
                                                    ▓▓░▓▒▓▒▓▓▓▓▓▓▒░░▓                                                     
                                                    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒                                                     
                                                            ▓▓▓▓░                                                           
                                                            ▒▓▓░░                        ▓▓▓                              
                                                            ▒▓▓                          ░▓░                              
                                                            ▒▓▓                          ░▓░                              
                                            ░░▓▓▓           ▒▓▓                          ░▓░                              
                                        ▓▓▓▓▓▓▓▓▓           ▒▓▓                          ░▓░                              
                                        ▓▓▓▓▓▓▓▓▓▓▓▓        ▒▓▓                          ░▓▓                              
                                    ░▓▓▓▓▓▓▓    ▓▓          ▒▓▓                          ░▓▓                              
                                    ░▓▓▓▓▓        ▓         ▒▓▓                          ░▓▓                              
                                    ▓▓▓▓                    ▒▓▓                          ░▓▓                              
                                    ▓▓▓                     ▒▓▓                          ░▓▓                              
                                    ░▓▓                     ▒▓▓                          ░▓▓                              
                                    ░                       ▒▓▓                          ░▓▓                              
                                    ░                       ▒▓▓                          ░▓▓ ▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░       
                                    ░                 ▓▒░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▒▓        ▓░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒    
                                    ░        ▒░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░  
                        ░▓▓▓▓▓▓   ░    ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 
                        ▓▓▓▓▓▓▓▓  ░   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░
                        ▓▓▓▓▓   ▓▓░ ░ ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▒░▓▓▓▓▓▓▓▓
                        ▓▓▓▓      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ▒▓▓▓▓▓
                        ▓▓      ▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓▓▓▓
                    ░▓       ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ▓▓
                                ▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓ 
                    ▒        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒ 
                    ▒      ▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 
                    ▒     ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  
                    ▒   ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   
                    ▒   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓▓░▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    
                    ▒ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ▓▓▓▓▒▓▓░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    
                    ▓▓▓▓▓▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓     
                    ▒▓▓▓▓▓▓▓▓▓▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▒▓▓▓▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      
                    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓       
                ▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓        
                ▓▓▓▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓         
                ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓          
                ▓▓▓▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓            
                ▓▓▓▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓             
            ░▓▒▓▓ ▓▓▓▓▓▓▓▓▓▓▓ ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓               
            ▒▓▓▓ ▓▓▓▓▓▓▓▓▓▓▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                
            ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                  
        ▓▓▓▓▓▓▓▓▓▓▓▓▓▒ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                   
        ▓▓▓▓▓▓▓▓▓▓▓▓▓░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                     
        ▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                      
        ▓▓▓▓▓▓▓▓▓░ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                        
    ▓▓▓▓▓▓▓▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                         
    ▓▓▓▓▓▓▓▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                          
    ░▓▓▓▓▓▓░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                           
    ░▓▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                            
    ▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                             
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                              
        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                              
            ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                               
                ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                                
                ░     ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                                
                    ░              ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                                 
                                                                                                                            
                            ░                                                           ░                                 
                                    ░                                                                                      
                                        ░░░                                                                              
                                                    ░░                                   ░                                  
                                                            ░                          ░                                  
                                                                        ░░              ░                                                
    """+RESET)                                                                            
#      Module Sailing SHip
# -----------------------------------------------------------
def sailing_ship():
    print(LIGHT_GRAY+UP*23+"""
    ▓                                        ░░░░░░░░░░▒▒         ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                                                 
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
    ▓                                                   ▓▓▓▓▓▓▓▓▓▓▓▒                                                                       
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
    ▓                                       ░░░░░░░░░░▒▒          ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                                                 
▓                                            ▒▒▒▒▒▒▒▒▒▒▒▒          ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                                                
▓                                              ░▒▒▒▒▒▒▒▒▒▒▒▒░         ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                                                
▓                                                 ░▒▒▒▒▒▒▒▒▒▒           ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                                               
▓                                                  ░▒▒▒▒▒▒▒▒▒▒▒           ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                                              
▓                                                      ▒▒▒▒▒▒▒▒▒             ░▒▒▒▒▒▒▒▒▒▒▒▒▒                                              
▓                                                       ▒▒▒▒▒▒▒▒▒▒▒            ▒▒▒▒▒▒▒▒▒▒▒▒▒▒                                             
▓                                                        ▒▒▒▒▒▒▒▒▒▒▒░            ▒▒▒▒▒▒▒▒▒▒▒                                              
▓                                                            ░▒░▒▒▒▒                ░▒▒▒▒▒▒▒▒                                              
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
    ▓                                                   ▓▓▓▓▓▓▓▓▓▓▓▒                                                                       
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
    
def sinking_ship():
    print(CLEAR_SCREEN)
    print(LIGHT_GRAY+"""
                                                                                                                                                
                                                                    ▒                                                                           
                                                                    ▒                                                                            
                                                                    ▒▓                                                                             
                                                                    ▓                                                                              
                                                ▓▒                 ▓▒                                                                               
                                                ▓▓▓▓▓             ▓▓                                                                                
                                                ▒▓▓▓▓▓          ░▓░                                                                                 
                                                ▓▓▓▓▓▓▓▓       ▒▓▒                                                                                  
                                    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ▓▓░                                                                                   
                                        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ▒ ▓▓                       ▒▓▓▓                                                          
                                ▒      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                        ▓▓▓▓▓                                                         
                                ▓          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                      ▓ ░▓▓▓▓░                                                        
                                            ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                    ▓     ▓                                                          
                                                ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ▓▓  ▓▓▓                  ▒▒                                                   
                                                ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓ ▓      ▓      ░▓▓▓░                                                 
                                                ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░      ▓      ▓▓▓▓▓▓▓                                                
                                                    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ▓      ▓   ▓▓▓                                                 
                                                    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓             ▓                                                  
                                    ▒                  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ▒      ▓       ▓▒                                          
                                        ▒                 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ▓      ▓      ▓▓▓▓▓                                         
                                        ░                 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓     ▓      ▓░▓▓▓▓▓                                        
                                        ▓                  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ░           ▓▓                                         
                                                                ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓     ▓      ▓                                          
                                            ▒                  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▓      ▓      ▓▓▓                                  
                                                ▒                 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ▓      ▓▓▓▓▓▓                                
                                                                    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░   ▓         ▓▓▓▓                                
                                                                    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓     ▒      ▓                                 
                                                    ▓                  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ▓▓  ▓▓░▓▓▓▓▓▓    ░▒     ▓                                  
                                                                                                                                                    
""")
    time.sleep(1.5)
    print(CLEAR_SCREEN)

    print(LIGHT_GRAY+ """
                                                                                                                                                
                                                                                                                                                
                                                                                                                                                
                                                                                                                                                
                                                                                                                                                
                                                                                                                                                
                                                            ▓                                                                             
                                                            ▓                                                                              
                                                            ░▓                                                                               
                                            ░▓▓               ▒▓                                                                                
                                            ░▓▓▓▓▓           ▓▓                                                                                 
                                            ▓▓▓▓▓▓▓         ▓▓                                                                                  
                                    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ▓▓                                                                                   
                                ▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▓▓▓                       ▓▓                                                           
                                    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                       ▓▓▓▓▓                                                         
                            ▒        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒                     ▒ ▓▓▓▓▓▓                                                        
                                        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                     ▓░   ▓▓▓                                                         
                            ░              ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓       ▓    ▓      ▓      ░                                                          
                                            ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ▓▓▓▒▓▓▓▓▓▓   ▓      ▓      ▓▓▓                                                  
                            ░                  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓       ▒      ▓▓▓▓▓▒                                                
                            ▓                  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓            ▓░ ▓▓▓▓                                                 
                            ▓                  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░       ▓     ▓▓                                                 
                                                    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓     ▓     ░▓      ▒                                           
                                ▒                  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                ▓▓▓▒                                         
                                    ▒                 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓             ▓▓▓▓▓▓▓                                        
                                    ░                 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓          ▓  ░▓▓▓▓                                        
                                                        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ▓      ▒                                         
                                                            ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ▓      ░      ▓▓                                  
                                            ░                  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓               ▓▓▓▓▓                                 
                                                                                                                                                
    """)
    time.sleep(1.5)    
    print(CLEAR_SCREEN)
    print(LIGHT_GRAY+ """
                                                                                                                                                
                                                                                                                                                
                                                                                                                                                
                                                                                                                                                
                                                                                                                                                
                                                                                                                                                
                                                                                                                                                
                                                                                                                                                
                                                                                                                                                
                                                                                                                                                
                                                                                                                                                
                                                                ░                                                                             
                                                                ▓                                                                              
                                                                ▓                                                                               
                                            ▓▓▓                ▓                                                                                
                                            ▓▓▓▓             ▓▓                                                                                 
                                            ▓▓▓▓▓▓▓         ▓▓                                                                                  
                                    ▓▓▓▓▓▓▓▓▓▓▓▓▓       ▓▓                                                                                   
                                ▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ▓▓                        ░                                                           
                                ▓    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓▓▓                       ▓▓▓▓                                                          
                                    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                       ▓▓▓▓▓▓▓                                                        
                            ▒           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒                         ▓▓▓                                                         
                            ▒              ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓       ░    ▒      ▓░     ▓                                                          
                                            ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ▓▓▓▓▓▒▓▒▓    ▒      ▓      ▓▓                                                   
                                            ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓▓      ▓      ▓▓▓▓▓                                                 
                            ▒                  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ░▓        ▓▓▓▓▓                                                
                            ▒                  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▓     ▓     ▓▓                                                 
                                ▒                 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓     ▒      ▓                                                  
                                ░                 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▓     ░▓      ▓▓▓                                          
                                                                                                                                                
                                                                                                                                                
    """)
    time.sleep(1.5)    
    print(CLEAR_SCREEN)
    print(LIGHT_GRAY+ """
                                                                                                                                                
                                                                                                                                                
                                                                                                                                                
                                                                                                                                                
                                                                                                                                                
                                                                                                                                                
                                                                                                                                                
                                                                                                                                                
                                                                                                                                                
                                                                                                                                                
                                                                                                                                                
                                                                                                                                                
                                                                                                                                                
                                                                                                                                                
                                                                                                                                                
                                                                                                                                                
                                                                                                                                                
                                                                    ░                                                                           
                                                                                                                                                
                                                                ▒                                                                             
                                                                ▓▓                                                                              
                                            ▓▓                ▓▓                                                                               
                                            ▓▓▓▓░             ▓▓                                                                                
                                            ▒▓▓▓▓▓           ▓▓                                                                                 
                                        ▒▓▓▓▓▓▓▓▓       ▒▓▓                                                                                  
                                    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒     ▓▓                                                                                   
                                ▒  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ▓▓▒                       ▓▓▒                                                          
                            ▒      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒                      ▓▓▓▓▓▓                                                         
                                        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                      ▓  ▓▓▓▓▓                                                        
                                                                                                                                                
                                                                                                                                                
    """)
    time.sleep(1.5)    

# ###########  Game over module
def game_over():

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
        ::: ::::  ::   :::  :::     ::   :: ::::     
        :: :: :    :   : :   :      :    : :: ::      
                                                        
                                                        
       @@@@@@   @@@  @@@  @@@@@@@@  @@@@@@@          
       @@@@@@@@  @@@  @@@  @@@@@@@@  @@@@@@@@         
       @@!  @@@  @@!  @@@  @@!       @@!  @@@         
       !@!  @!@  !@!  @!@  !@!       !@!  @!@         
       @!@  !@!  @!@  !@!  @!!!:!    @!@!!@!          
       !@!  !!!  !@!  !!!  !!!!!:    !!@!@!           
       !!:  !!!  :!:  !!:  !!:       !!: :!!          
       :!:  !:!   ::!!:!   :!:       :!:  !:!         
       ::::: ::    ::::    :: ::::   ::   :::         
       : :  :       :      : :: ::   :    : :                                                                
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
        ::: ::::  ::   :::  :::     ::   :: ::::     
        :: :: :    :   : :   :      :    : :: ::      
                                                        
                                                        
       @@@@@@   @@@  @@@  @@@@@@@@  @@@@@@@          
       @@@@@@@@  @@@  @@@  @@@@@@@@  @@@@@@@@         
       @@!  @@@  @@!  @@@  @@!       @@!  @@@         
       !@!  @!@  !@!  @!@  !@!       !@!  @!@         
       @!@  !@!  @!@  !@!  @!!!:!    @!@!!@!          
       !@!  !!!  !@!  !!!  !!!!!:    !!@!@!           
       !!:  !!!  :!:  !!:  !!:       !!: :!!          
       :!:  !:!   ::!!:!   :!:       :!:  !:!         
       ::::: ::    ::::    :: ::::   ::   :::         
       : :  :       :      : :: ::   :    : :                                                                  
       """+ RESET)                                                                                                                                    

def goto_lagoon():
    # Qaiser:
    # Called by BEACH.  Goes to TEMPLE, VOLCANO
    # main hub/safe place
    print(GREEN + """
                    *✲*´*。.❄¯*✲。❄。*¨`*✲´*。❄¨`*✲。❄。*`*
                    *╔════════════ ༺❀༻❤༺❀༻ ════════════╗*
                    *♥*❄¯*✲❄♫♪♩░B░E░A░U░T░I░F░U░L░ ♫♫♪❄¯*✲❄
                    *╚════════════ ༺❀༻❤༺❀༻ ════════════╝*
                    *✲*´*。.❄¯*✲。❄。*¨`*✲´*。❄¨`*✲。❄。*`*
You wander by a beautiful blue lagoon; peaceful and tranquil. A place to rest and relax.
From here you can go to a ruined Temple or towards the volcano.\n
""")
    choices = [
        "That Temple looks interesting.",
        "Oooh a volcano! What could possibly go wrong..",
        "Rest here, maybe have a swim and a siesta.\n"
    ]
    choice = get_input(choices)
    if choice == 1:
        print("You head towards the ruined temple\n")
        goto_temple()
    elif choice == 2:
        print("A volcano - what fun!\n")
        goto_volcano()
    elif choice == 3:
        qprint(GREEN + "A nice relaxing swim and a snooze in the sun - just what you wanted in this tropical paradise\n")
        goto_lagoon()
    else:  # should never get a choice this high..
        goto_death("SYSTEM ERROR #zzzzzz\n")

# -----------------------------------------------------------  BOARD_HIP functions  ------------



def delay_talk(string, colour = YELLOW, delay = 0):
    for letters in string:
        sys.stdout.write(colour+letters+RESET)
        sys.stdout.flush()
        time.sleep(delay)


def board_ship():
    narr_print("You walk through the Cunard Building, walking past other guests who are checking in & checking out\n")
    narr_print("You make your way outside to the gang way entrance & see the ship you'll be boarding\n")
    docked_ship_pic()
    narr_print("its bigger than you thought,\nwhich makes you feel safer\nAt the gangway another gentlemen takes your ticket and allows you passage\n you make your way across and now you're finally aboard the ship\n")
    narr_print("You're finally aboard, you think, whats the first thing to do....\n[Enter Answer]\n")
    answer = input()
    narr_print(f"You think about {answer}, but you realise you need to drop off your bags\nyou walk through the grand hall of the ship & head towards your cabin,\nits a windowless inside cabin...not what you requested, but you're too tired to complain\nyou drop off your bags & think about {answer} but realise you can do that later maybe,\nyou head to bed for a quick nap, so you can enjoy your evening better\n")
    input("Press <enter> to continue\n")
    sailing_ship()
    escape_ship()

def secret_question():
    delay_talk("Ok now that we have everything check, I can see you are on the guest list, but for a security check\ncan you please confirm your occupation\n")
    narr_print("What is your occupation\n")
    occupation =[ "[1] Engineer", "[2] Doctor", "[3] Retired", "[4] You're actually the captain of the ship\n"]
    for jobs in occupation:
        print(jobs)
    answer = input()
    answer =int(answer)
    if answer== 1:
        narr_print("You smile & explain you are actually an engineer, who use to work on ships many years ago, \nthe Booth Worker is impressed, that you and ships have a history\n")
        delay_talk(f"Very instresting {name}, please enjoy your voyage, if there are any issues, we'll know to ask you for help\n")
        narr_print("His joke was aimed to calm you, but instead the idea of something bad happening, makes you paranoid about the voyage ahead....\n")
        board_ship()
    elif answer == 2:
        narr_print("Opening up your bag on the desk, you pull out your newly Certified Doctrone identification\n")
        delay_talk("Oh very nice, another Doctor on the ship, we'll knock on your cabin if your needed\n")
        narr_print("You think, this isn't going to be a relaxing voyage.....\n")
        board_ship()
    elif answer == 3:
        narr_print("You explain that you're retired & looking forward to a relaxing cruise, before you start your retirement in the new world\n")
        global age
        if age <= 55:
            narr_print("As you state your plans the gentlemen, looks suprised, that you have retired at a much younger age than normal, they look enveous\n")
            delay_talk("Oh...well...welcome aboard & please enjoy your retirement voyage\n")
            board_ship()
        elif age >=55:
            narr_print("You state your plans and explain abit about your life story....\nThe Booth Worker looks like hes heard it all before...\n")   
            delay_talk(f"Yes {name}, that is very interesting...\n")
            narr_print("He wuickly passes you your boarding pass and waves you to move on\n")
            board_ship()
    elif answer == 4:
        narr_print("You put on your straight face & demand that the worker shows respect to the Captain of this ship\n he laughs\n")
        delay_talk("Oh yes Sir!!, sorry to not recognise you, your vessel awaits....\n")
        narr_print("He gives you a sarcastic salute\n")
        delay_talk("Please answer the question or I won't be able to confirm\n")
        secret_question()
    else:
        narr_print("Don't think thats an occupation.....Try again\n")
        secret_question()    

def pass_back_location():
    global where_from
    delay_talk(f"...and last part to check is where are you from, can you confirm you are from {where_from}?[Y/N]\n")
    answer = input().upper()
    if answer == "Y":
        delay_talk(f"Ok,{name}, so your from {where_from}, never been there myself\n")
        secret_question()
    elif answer == "N":
        delay_talk("So your not from {where_from}, shame these are filled in with ink & not pencil\nbut then again, it stops fake ID checks...\nPlease take another form and fill all sections correctly please\n")
        narr_print("He passes you another form to fill out again\n")
        id_form()
    else:
        delay_talk("Pardon me, I asked to confirm where you are from, a simple Yes or No will do?\n")
        pass_back_name()

def pass_back_age():
    global age
    delay_talk(f"Ok and can you confirm you are {age} [Y/N]\n")
    answer = input().upper()
    if answer == "Y":
        delay_talk(f"Ok,{name}, next question\n")
        pass_back_location()
    elif answer == "N":
        delay_talk("Well you will have to do another form now sadly, as these ID forms cant be editied\n")
        narr_print("He passes you another form to fill out again\n")
        id_form()
    else:
        delay_talk("Pardon me, I asked to confirm your age?\n")
        pass_back_name()

def pass_back_name():
    narr_print("You pass the form back to the gentlmen\n")
    delay_talk("Ok, everything seems to be in order, I'll just double check with you....\n")
    delay_talk(f"Your name is {name}, is this correct?[Y/N]\n")
    answer = input().upper()
    if answer == "Y":
        delay_talk(f"Ok, {name}, next question\n")
        pass_back_age()
    elif answer == "N":
        delay_talk("Well you will have to do another form sadly\n")
        narr_print("He passes you another form to fill out again\n")
        id_form()
    else:
        delay_talk("Pardon me?\n")
        pass_back_name()

def id_form():
    global name 
    global age 
    global where_from
    def location_check():
        global where_from
        print("Place of home")
        where_from=input()
        pass_back_name()
    def age_check():
        print("Please fill in your age")
        age = input("")
        age = int(age)
        try: 
            print(f"Your age is {age}")
            location_check()
        except ValueError:
        # Handle the exception
            print('Please enter a number')
            age_check()
    def name_check():
        global name
        narr_print("You look down at the form, you just want this over with, so you can board....\n")
        print("Please fill your name in below\n")
        name = input("")
        age_check()
    name_check()    
    
    

    


def id_check():
    narr_print("The Booth worker, starts to get impatient....\n")
    delay_talk("Excuse me, if you can fill in this form, I can see if your on the guest list and we can get you boarded soon\n")
    narr_print("The gentlemen hands you over a form to fill in\n")
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
    ticket_list = ["[1]Check Desk", "[2]Check Bag", "[3]Search Luggage", "[4]Check Coat Pocket\n"]
    for check in ticket_list:
        print(check)
    answer = input()
    answer =int(answer)
    if answer == 1:
        stress_level += 1
        print("You look down at the desk, you didn't leave it there, 'What did I do with it' you mutter...\n")
        stress_check()
    elif answer ==2:
        stress_level += 1
        print("You fantactly search your hand luggage, its not there either\n")
        stress_check()
    elif answer ==3:
        stress_level += 1
        print("After opening your luggage and routing through it for what feels like ages, you realise its not there either\n")
        stress_check()
    elif answer ==4:
        stress_level += 1
        narr_print("Its not in your pocket, but maybe you put it in another pocket you think to yourself...\n")
        time.sleep(1)
        narr_print("...............")
        narr_print("Do you go to check all the pockets in the coat?[Y/N]\n")
        pocket_answer = input().upper()
        if pocket_answer == "Y":
            stress_level += 1
            print("You search another pocket, still haven't found it.....\n")
            stress_check() 
        else:
            narr_print("The Booth Worker looks confused & reminds you, that its your boarding pass he needs....\n")
            stress_check()
    else:
        narr_print("Don't think you could of left the ticket there....")
        ticket_check()


def board_check():
    print(CLEAR_SCREEN)
    narr_print("You've been travelling half way across England, collecting the requested documents to grant you entry into the new world,\n a sea liner is waiting docked in Liverpool, awating to take you across the Alantic\n")
    time.sleep(1)
    narr_print("The bus stops, you've arrived at the entrace to the Cunard Building,\n you exit the bus, making sure you have all your belongings,\n you look up as the sun hangs high, you make your way to the entrance and join the queue,\n you notice the queue seems exceptionly long, but you don't give it a 2nd thought.......\n you feel like you have been waiting for hours, but notice the midday sun still burning, you check your watch........\n less than half an hour has passed or maybe you forgot to wind your watch again\n You think to yourself, 'How much longer do i have to wait'")
    time.sleep(1)
    narr_print("With your thoughts running away, you don't realise another boarding booth has opened,\n a young gentleman behined the booth whistles for your attention,\n you quickly snap out of your day dream & move ahead of the crowd with your lungage in tow.\n")
    delay_talk("Thank you ladies & gentle, we do apoligise for the delay on checking your boarding passes & are assigning more booth workers\n don't worry the ship will be making up for lost time & you will still make the arrival in 6 days time by 1:00PM\n")
    narr_print("The Booth worker waves you forward.... you approuch & lean on the desk for some purchase & rest\n")
    delay_talk("Hello, welcome to Cunard Cruises, thank you for being patient with us, may I see your boarding pass?\n")
    narr_print("It's been a long day, getting here & you've forgotten where you put it for safe keeping\n")
    ticket_check()

# --------------------------------------------------- Escape  ship          ---------------
# ---------------------     escape_ship   ------------

def escape_ship():
    print(CLEAR_SCREEN)
    start=random.randint(1,10)
    if start >5:
        fire_ship()
    else:
        posidon()

def open_door_pos():
    global life_jacket
    narr_print("The door handle is cold to the touch, you notice water leaking through the rim of the door\nyou grab the handle and slowly turn it\nopening the door, water starts rushing in, you look through to door gap to gauge how bad the hallway is\nwater seems to be wasit high, you open the door further and start your escape....\n")
    narr_print("..........\nyou make it to the end of the hallway and find a set of stairs,\nUp is down & down is up, you think whats the best way to get out, as you notice a change in the water level\nthe ship must be leaning to one side\nDo you use the stairs & dive further down or Climb up the sloped ceiling and use the next set of stairs\n")
    def pick_react():
        narr_print("You need to keep moving, what do you do?\n")
    react =[ "[1] Dive down into the water & follow the Stairs", "[2] Climb up the hallway to the next set of stairs\n",]
    for pick in react:
        print(pick)
    answer = input()
    answer =int(answer)
    if answer == 1:
        global life_jacket
        if life_jacket ==1:
            narr_print("You won't be able to dive while wearing your life jacket, you quickly remove it & drop it in the water....\n")
            time.sleep(1)
            narr_print("You take one last look of your surroundings & take a deep breath, you drive into the water\ngrabbing onto the rail of the stairs, you use it as a guide, you travel down 2 floors\nfinally at the prominarde deck, you see the a way out into the open water\n you swim for it, once out into the open sea, you look up\nA defeative thought pops into your head, when you realise your too deep & will never make it to the surface..\nbut you swim as quick as you can to the surface, you've not even half way up, before you start to drown\nYour final thoughts are 'Terrible start to retirement'\n")
            narr_print("..........\n")
            goto_death_sink("Your limpless body sinks to the abyss....\n")
            
        else:    
            narr_print("You take one last look of your surroundings & take a deep breath, you drive into the water\ngrabbing onto the rail of the stairs, you use it as a guide, you travel down 2 floors\nfinally at the prominarde deck, you see the a way out into the open water\n you swim for it, once out into the open sea, you look up\nA defeative thought pops into your head, when you realise your too deep & will never make it to the surface....\nbut you swim as quick as you can to the surface, you've not even half way up, before you start to drown\nYour final thoughts are... 'Terrible start to retirement'....\n")
            narr_print("..........\n")
            goto_death_sink("Your limpless body sinks to the abyss....\n")
            
    elif answer ==2:
        narr_print("You slowly climb the ceiling of the hallway.....\nthe water stops after a while & you realise that you must be above sea level, if the water has stopped rising\nas you reach the top of the hallway, you find the next set of stairs\nnow you must climb down the stairs to reach the prominarde\n")
        narr_print("...............\n")
        narr_print("Its 2 decks down, with no water to cushin your fall, if you slip\ntaking your time to get down, you feel the ship tilt more\nthe ship is going to be upright soon like a bottle in the ocean\nyou move quicker, as at this rate you wont be able to get across\nfalling down a hallway is a long way down....\nyou finally make it to the open deck....\nlooking outside you see the sea is chopper, but no storm...\nescapeing is more important now, than trying to figure out what has caused this disaster....\nfinally your outside,\n")
        if life_jacket ==1:
            narr_print("With your life jacket equiped you jump into the sea, hoping that a life boat will find you....\nbut in the back of your mind before you jump, you do think how quiet it has been....\n")
            time.sleep(1)
            narr_print("......\n")
            narr_print("Hopefully there are other survioues who will be able to help you.....\nthe thought of drifting in the sea for days...is not a nice thought\nBut it is a better option that being pulled down by the sinking ship.....\n")
            goto_beach()
        elif life_jacket ==0:
            narr_print("You get ready to jump into the ocean.....\n'That Life Jacket would of been great now, shame you didn't collect it' you think to yourself\n Hopefully there are other survioues who will be able to help you.....\nthe thought of drifting in the sea for days...is not a nice thought\nBut it is a better option that being pulled down by the sinking ship.....\nbut without a life jacket there better be something out there to grab onto that floats....\nwith one look back at the sinking ship, you leap into the ocean........\n")
            goto_beach()
    else:
        narr_print("Don't think thats an option right now....\n")
        pick_react()
    pick_react()


def open_door_fire():
    global life_jacket
    narr_print("The door handle is hot to the touch, nearly burning your hand\ngrabbing a your jacket you use it to grab the handle\nopening the door, intence heat & smoke fills the room\nyou remember your training & get to the floor and crawl as quick as you can\nstaying low you go past other cabins, some doors are open\nothers must of got out too in time, but you don't see anyone else\nyou keep an eye out for people in need\nthe alarms ringing is deafening, you wouldn't be able to hear anyones scream for help\n")
    narr_print("..........\nyou make it to the stairs at the end of the hallway,\nthe stairs look stable, but there feels like there is fire further up on the next floor....\nbut further down the hallway is more smoke....\n")
    def pick_react():
        narr_print("You need to keep moving, what do you do?\n")
    react =[ "[1] Use Stairs", "[2] Walk down hallway to the next set of stairs",]
    for pick in react:
        print(pick)
    answer = input()
    answer =int(answer)
    if answer == 1:
        goto_death_sink("You make your way up the stairs, the smoke filled air blinding you\nthe heat is rising, you realise its worse on this floor & can't go any further....\nlooking back down, you see flames flickering through the smoke.......\nyour trapped, theres nothing you can do, you slowly pass out from the chocking air & heat\n")
    elif answer ==2:
        narr_print("You go past the stairs, staying low and go further through the hallway\n the smoke is thinner here, so you risk getting up to move faster, you rush down the hallway\nsuddenly a large explosion errupts from above and part of the ceiling comes crashing down on top of you\n")
        if life_jacket ==1:
            narr_print("A cabin door rests on you, coughing from the smoke,\n you look up, the door actualy saved you from the weight of the debris, shielding you from the burst pipes\nwhich would of punctured you like a pin cushion\n")
            goto_death_sink("You try and lift the door off you, but its too heavy with everything resting on it\nthe smoke is thicking & its getting hotter\nyou try and squeeze out......\nthe life jacket has you wedged in....\nattempting to pull it off fails...\nyou're stuck.....\nas the smoke thickens you start to loose consciousness....\nyou black out, trapped with no one to save you, your fate is sealed...")
        elif life_jacket ==0:
            print("A cabin door rests on you, coughing from the smoke,\n you look up, the door actualy saved you from the weight of the debris, shielding you from the burst pipes\nwhich would of punctured you like a pin cushion")
            narr_print("You try and lift the door off you, but its too heavy with everything resting on it\nthe smoke is thicking & its getting hotter\nyou try and squeeze out......\nsuccess....you slip out from under the door & debris and finally make it to the next stair case\nthe smoke is not as thick & the heat has dropped,rushing to the next floor, the conditions get better with each floor\nas you reach the next floor that takes you outside another explosion errupts, but this time from below.....\the rupture launchers you, crashing you head first into the ceiling,\n you fall back down, you try & break the fall, but you're too slow\nhitting the floor, you slowly pass out, whether it be from the smoke or the injury to your head......\n")
            goto_beach()
    else:
        narr_print("Don't think thats an option right now....\n")
        pick_react()
    pick_react()

def posidon():
    print(LIGHT_BLUE + """
    *✲*´*。.❄¯*✲。❄。*¨`*✲´*。❄¨`*
    *╔═══════ ༺❀༻❤༺❀༻ ═══════╗*
    *♥*❄¯*  THE QUIET COLD  ♪❄¯*✲❄
    *╚═══════ ༺❀༻❤༺❀༻ ═══════╝*
    *✲*´*。.❄¯*✲。❄。*¨`*✲´*。❄¨`*
    \n \n \n"""+RESET)
    narr_print("Something rocks the ship, you half wake up...You think to yourself, its just the waves.....\nYou wait for the ship to rock in the other direction......\nThe sick feeling you get when on a rollercoaster starts to set in,\nyou sit up & realise the ship isn't rocking back, another large dull thud slams into the ship\n....\n..........\n...........\nWith quick realisation, you brace yoursel for what you know will happen next\nthe ship slowly creaks as it rolls over to one side and crachers into the waves......\n............\nYou black out....\nYou wake up to the alarms ringing, you look up and see your bed is on the ceiling....\nAs you slowly get up, you realise its you who is on the ceiling......\n")
    def pick_react():
        narr_print("You know you need to move quickly, what do you do?\n")
        react =[ "[1] Grab Life Jacket", "[2] Open the Door",]
        for pick in react:
            print(pick)
        answer = input()
        answer =int(answer)
        if answer== 1:
            global life_jacket 
            life_jacket +=1
            narr_print("You quickly search the cabin for the life jacket.....where is it...\nYou remember its normally stored under the bed....and the bed is on the ceiling\n'No time to waste' you think, you make way for the door\n")
            narr_print("..............\n") 
            open_door_pos()
        elif answer == 2:
            narr_print("You havn't got time to to get the life jacket, you need to get off ASAP, you rush for the door...\n")
            open_door_pos()
        else:
            narr_print("Don't think thats an option right now....\n")
            pick_react()
    pick_react()            


def fire_ship():
    print(RED + """
    *✲*´*。.❄¯*✲。❄。*¨`*✲´*。❄¨`*
    *╔═══════ ༺❀༻❤༺❀༻ ═══════╗*
    *♥*❄¯*FIRE IN THE BEAST♪❄¯*✲❄
    *╚═══════ ༺❀༻❤༺❀༻ ═══════╝*
    *✲*´*。.❄¯*✲。❄。*¨`*✲´*。❄¨`*
                        
    \n \n \n"""+RESET)
    narr_print("You wake up to a large explosion...quickly getting up, you hear another one\nthe ships alarms are sounding, you must get off the ship.....\n")
    def pick_react():
        narr_print("You know you need to move quickly, what do you do?\n")
        react =[ "[1] Grab Life Jacket", "[2] Open the Door",]
        for pick in react:
            print(pick)
        answer = input()
        answer =int(answer)
        if answer== 1:
            global life_jacket
            life_jacket +=1
            narr_print("You search franticly for it, you find it lodged under the bed, you quickly pull it over and tie it on & go for the door....\n")
            narr_print("..............\n") 
            open_door_fire()
        elif answer == 2:
            narr_print("Panicing, you ignore looking for the life jacket, there isn't enough time...\nyou rush for the door to escape....\n")
            open_door_fire()
        else:
            narr_print("Don't think thats an option right now....\n")
            pick_react()
    pick_react()            



# =====================  Call main game function to start if run from command line  ======================
if __name__ == "__main__":
    vod()

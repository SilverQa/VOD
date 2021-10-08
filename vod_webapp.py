# Voyage of the Damned adventure game
# CodeNation Sep 2021
# QA, AB, KO
import sys, datetime, time, random, os
from flask import Flask, render_template, request
# Define colors and cursor handling as constants
# """ ANSI color codes """
BLACK = ""
RED = ""
GREEN = ""
BROWN = ""
BLUE = ""
PURPLE = ""
CYAN = ""
LIGHT_GRAY = ""
DARK_GRAY = ""
LIGHT_RED = ""
LIGHT_GREEN = ""
YELLOW = ""
LIGHT_BLUE = ""
LIGHT_PURPLE = ""
LIGHT_CYAN = ""
LIGHT_WHITE = ""
BOLD = ""
FAINT = ""
ITALIC = ""
UNDERLINE = ""
BLINK = ""
NEGATIVE = ""
CROSSED = ""
RESET = ""
UP = ""
LEFT = ""
CLEAR_SCREEN = ""

# Global Variables
inventory = []
name = ""
age = 0
where_from = ""
stress_level = 0
life_jacket = 0
html_string = ""
app = Flask(__name__)
choice = ""
choices = []

def vod():
    global inventory
    # app = Flask(__name__)
    
    print_big_ascii_gameposter()
    # time.sleep(1.5)
    goto_lagoon()
    app.run()

#   -------------  Common functions declared here   ------------------

def goto_death_sink(string):
    global inventory
    goto_lagoon()
    qprint(PURPLE + f"\n{string} " + LIGHT_RED + UNDERLINE + "YOU HAVE DIED!!" + RESET)
    qprint(f"\nYou had {inventory} in your possesion.")
    # <exit program>
    time.sleep(1.5)
    # sinking_ship()
    quit()
# ---------------------
@app.route("/", methods=['GET', 'POST'])
def home():
    global html_string
    start_html = """
<!DOCTYPE html>
<html lang="en">
<head> <!--additional info and links -->
    <link href="main.css" type="text/css" rel="stylesheet"> 
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content = "IE=edge">
    <meta name="viewport" content="width=device-width,initial-scale=1.0">
    <title>Qaiser's Skull Island!</title>
</head>
<body>
<h1>Skull Island</h1>
"""
    end_html = """
</body>
</html>"""
    if request.method == 'POST':
        if request.form.get('action1') == 'VALUE1':
            choice = "1"
            print("choice1") 
            goto_temple()
            return html_string
        elif  request.form.get('action2') == 'VALUE2':
            choice = "2" # do something else
            print("choice2")
            goto_tomb() 
            return html_string
        elif  request.form.get('action3') == 'VALUE3':
            print("choice3") 
            goto_volcano()
            return html_string
        else:
            pass # unknown
    elif request.method == 'GET':
        start_html = """
<!DOCTYPE html>
<html lang="en">
<head> <!--additional info and links -->
    <link href="main.css" type="text/css" rel="stylesheet"> 
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content = "IE=edge">
    <meta name="viewport" content="width=device-width,initial-scale=1.0">
    <title>Qaiser's Skull Island!</title>
</head>
<body>
<h1>Skull Island</h1>
"""
        start_html = ''
        end_html = """
</body>
</html>"""
        return start_html + html_string + end_html
    
    # return render_template("index.html")
    return start_html + html_string + end_html
#----------------------
def goto_death(string):
    global inventory
    goto_lagoon()
    qprint(PURPLE + f"\n{string} " + LIGHT_RED + UNDERLINE + "YOU HAVE DIED!!" + RESET)
    qprint(f"\nYou had {inventory} in your possesion.")
    # <exit program>
    quit()

def get_input(choices):
    # Prints coloured numbered list of choices and choose one of them.
    # returns the number chosen as an int.
    
    number = 1
    qprint('<form method="post" action="/">')
    for question in choices:
        qprint(question)
        qprint(f'<input type="submit" value="VALUE{number}" name="action{number}"/>')
        number += 1
    qprint('</form>')
    qprint("What do you want to do?")
    # app.get()
    return 

def qprint(string, delaytime = 0.00001):
    # prints a string slowly in typewriter effect. delaytime is delay time is seconds
    # the   ,end=''  parameter to qprint() stops it printing newline, so everything prints on same line
    global html_string
    html_string += string

def print_big_ascii_gameposter():
    qprint(RESET + CLEAR_SCREEN + 
           "Welcome to The Voyage of the Damned\n\nA game of mystery and terror\nAre you ready?")
    # time.sleep(1)
    qprint(UP+UP+UP+UP+"\nWelcome to "+RED + UNDERLINE+"The Voyage of the Damned")
    qprint("!!!!!!\n\n"+RESET)
    qprint("A game of "+LIGHT_GREEN+"mystery"+LIGHT_WHITE+" and " +
           LIGHT_CYAN+"terror\n"+PURPLE + "Are you ready?"+RESET+"\n")

# ------------ All locations defined here ----------------

# -----------------------------------------------------------------

def goto_lagoon():
    # Qaiser:
    # Called by BEACH.  Goes to TEMPLE, VOLCANO
    global choices
    qprint("""
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
    get_input(choices)


def game_intro():
    qprint(CLEAR_SCREEN)

# ###########  Game over module
def game_over():
        quit()

# -----------------------------------------------------------------

def goto_temple():
    # TEMPLE location in skull island
    # Qaiser:
    # Comes from LAGOON.  Goes to TOMB, BEACH
    global inventory
    qprint("""                              ஜ۩۞۩ஜ 
🌴🌴🌴🌴 You stumble into a clearing, before you are the overgrown remains of an exotic temple 🌴
Glints of gold remain on the walls. Lured by the promise of treasure and shelter you enter...
Further on you can see what looks like the entrance to a tomb.\n
""")
    choices = ["Lets explore that tomb."]
    if ("DIAMOND" not in inventory) and ("STATUE" not in inventory): # Havent already got it or swapped with statue
        choices.append("That diamond looks interesting!  Try and pick it up.\n")
        qprint("There is a large stone statue of a Sphinx here. Nestled within its paws is a massive Diamond.\n")  

    choice = get_input(choices) # only need to check for 1st choice. 2nd choice (if there) will run be default.
    
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

    qprint(LIGHT_RED)
    for y in me.split("\n"):
        qprint(" " * (termx - 28), y)
    qprint(UP * 12)
    time.sleep(1)
    for i in range(1, termx - 37):    # roll to end of screen - 40 chars
        for y in ball.split("\n"):
            qprint(" " * i, y)
        time.sleep(0.014)
        qprint(UP * (ball_lines+2))
    qprint("\n" * ball_lines)

def roller_ball(delay=0.0):
    # times how long it takes to enter the response with extra or minus time according to previous choices and stats.
    amount_time = 5.0  # default time, when just take statue.
    amount_time += delay
    qprint(f"\n\n\n{LIGHT_RED}With a loud 'thunk' an ancient intricate mechanism is set in motion.\n")
    qprint("At the head of tomb a massive round stone marble drops down\n")
    time.sleep(0.25)
    qprint("...and starts to roll towards you. At the same time the door in the chamber starts opening\n")
    qprint("If your reactions are quick enough you might reach the door before it crushes you\n\n\n\n")
    animate_ball()

    qprint(f"{RED}{NEGATIVE}PLEASE ENTER THE {RESET}{LIGHT_CYAN}{UNDERLINE}True{RED}{NEGATIVE} ANSWER IN UNDER  {RESET}{YELLOW} {amount_time} {RED} {NEGATIVE} SECONDS TO DODGE THE ")
    qprint(f"{ITALIC}BALL OF DOOM {RESET}{LIGHT_CYAN}")
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
    

def goto_tomb():
    # Qaiser:
    # Called by TEMPLE.  Goes to LAGOON
    global stress_level, inventory

    qprint("                        ▂▃▅▇█▓▒░۩۞۩ ۩۞۩░▒▓█▇▅▃▂")
    qprint(f"{DARK_GRAY}In the damp gloom of the tomb you feel the hairs on your neck standing up\n")
    qprint("(maybe you should stop rubbing that balloon you found earlier\n)", 0.001)
    if "STATUE" in inventory:
        qprint("You have seen enough of this deathtrap, you swiftly move though the cavern door.")
        goto_lagoon()
    qprint(f"\n{PURPLE}The atmosphere feels tense, you should be ready to act quickly{DARK_GRAY}\n")
    time.sleep(0.5)
    qprint("There is a small ornately decorated chamber in the middle of the tunnel with a closed solid stone door")
    if "FEDORA" not in inventory:  qprint(",and a hat.")
    qprint("\nThere seems to be a skeletal hand crushed under the door, like it was reaching for the hat at the last moment but missed.. How strange.\n")
    qprint(f"On a solid gold pedastal sits a beautiful glowing crystal statue inlaid with gold and silver. {GREEN}It calls to you...{DARK_GRAY}\n")
    
    choices = [
        "Pick up the hat - it looks kinda cool and he doesn't need it anymore",
        "Continue down the dark tunnel (it's very dark)",
        "Pick up the statue\n"
    ]
    if "DIAMOND" in inventory:
        choices.append("Carefully replace the statue with the diamond\n")
    if "FEDORA" in inventory: choices[0] = "Examine your hat again\n"
    
    choice = get_input(choices)
    

## ------------------------------------------  volcano ----------------------------
def fight_skeletons():
    "Fight against skeletons!"
    class Skeleton:
        health = 3

        def __init__(self):
            qprint("A bony skeleton (is there any other kind) claws it's way out of the ground.\n")

        def hit(self, hits = 1):
            if (random.randint(1,10)) < 8:   # 80%
                self.health -= hits
                qprint(LIGHT_WHITE + f"You land a hit on the skeleton with the magic dagger. It has {self.health} health left\n"+RESET)
            else: qprint(PURPLE + "You flail wildly with the dagger and manage to miss a clumsy undead pile of bones\n"+RESET)
            if self.health <= 0: 
                qprint(LIGHT_BLUE+UNDERLINE+"With a mighty blow you have skilled a kellington!\n"+RESET)

        def attack(self):
            # 50% chance of hitting. could have modifiers later??
            if random.randint(2,3) == 2:
                qprint(YELLOW+"The skeleton attacks, landing a hit on you. Ouch!\n"+RESET)
                return(1)
            else:
                qprint("Not all the bones are connected on this one - you easily evade the clumsy stab\n")
                return(0)

    qprint("You are going to fight 2 skeletons, each with 3 health. You have 5 health\n")
    qprint("You have a 80% chance to hit the skeletons. They have a 50% chance to hit you. Good luck!\n")
    health = 5
    dexterity = 0

    skel1 = Skeleton()
    skel2 = Skeleton()
    round = 1
    while skel1.health + skel2.health > 0:  # logic flaw if one is -1 - to fix..
        choices = []
        qprint(LIGHT_CYAN + f"Round {round}:  You have {health} points left. Skeletons points are 1:{skel1.health}  2:{skel2.health}")
        if skel1.health > 0: choices.append(f"First Skeleton ({skel1.health})")
        if skel2.health > 0: choices.append(f"Second Skeleton ({skel2.health})")
        choice=get_input(choices)
        if choice == 1: 
            # hack for changing menu places if killed 1st one first, then 2nd becomes first! Clear as mud eh :)
            if skel1.health <= 0: skel2.hit()
            else: skel1.hit()
        else:
            skel2.hit()
                
        qprint("The skeletons now attack you!\n")
        if skel1.health > 0: health -= skel1.attack()
        if skel2.health > 0: health -= skel2.attack()
        if health <= 0:
            qprint("The skeletons continue hacking at your lifeless body until the spirits are appeased.\n")
            time.sleep(2)
            goto_death("Soon you will be skeleton yourself...\n")

        round += 1

    qprint("You have defeated the skeletons and nothing now lies in your path. You take the canoe and ESCAPE!!\n")
    escape() 



def goto_volcano():
    # Qaiser:
    # Called by TEMPLE.  Goes to ESCAPE
    qprint(PURPLE+"""
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
#     if choice == 1:
#         goto_lagoon()
#     elif choice == 2:
#         qprint("""
# Picking up the dagger, you sense the anger of the spirits at your desacration of their altar\n
# A swirl of magic surrounds the altar shaking the ground. The earth heaves and clawing their way from their resting place:\n
# """)
#         qprint(LIGHT_RED+"SKELETONS!!!!    \nYou will have to fight these skeletons to get past\n"+RESET)
#         qprint("""
#                         .___.
#                      ,-^     ^-.
#       (@_           /           \
#    _   ) \_________/  __     __  \__________________________
# (_)@8@8{}<_________| /  \   /  \ |___________________________>
#        )_/         | \__/   \__/ |
#       (@            \    /|\    /
#                      \   \_/   /
#                       |       |
#                       |+H+H+H+|
#                       \       /
#                        ^-----^
# """)
#         if "STATUE" in inventory: 
#             qprint("The skeletons notice the glowing statue you hold. The spirits quiet... and depart howling in the wind\n")
#             qprint("The way is clear. You can escape this mysterious and cursed isle - you take the canoe and paddle\n")
#             qprint(f"away, with an enormously valuable glowing statue.  {LIGHT_CYAN + UNDERLINE} You are rescued and live the rest of your long life happy.\n")
#             escape()
#         else: fight_skeletons()
#     elif choice == 3:
#         qprint(f"The altar is stained by time and what looks like..{LIGHT_RED} blood\n"+RESET)
#         qprint("There are some strange writings on the side of the altar\n")
#         goto_volcano()        
#     else:  # should never get a choice this high..
#         goto_death("SYSTEM ERROR #zzzzzz\n")

## ------------------------------------------  volcano ----------------------------

def escape():
    stars = """
★ ° . *　　　°　.　°☆ 　. * ● ¸ 
. 　　　★ 　° :. ★　 * • ○ ° ★　 
.　 * 　.　 　　　　　. 　 
° 　. ● . ★ ° . *　　　°　.　°☆ 
　. * ● ¸ . 　　　★ 　° :●. 　 * 
• ○ ° ★　 .　 * 　.　 　　　　　.
 　 ° 　. ● . ★ ° . *　　　°　.　
°☆ 　. * ● ¸ . 　　　★ 　
° :. 　 * • ○ ° ★　 .　 * 　.　 
　★　　　　. 　 ° 　.  . 　    ★　 　　
° °☆ 　¸. ● . 　　★　★ 
° . *　　　°　.　°☆ 　. * ● ¸ . 
★ ° . *　　　°　.　°☆ 　. * ● ¸ 
. 　　　★ 　° :. 　 * • ○ ° ★　 
.　 * 　.　 　★     ° :.☆    
"""
    qprint(stars * 2)
    qprint(LIGHT_GREEN + f"""\n
┌──❀*̥˚──◌──◌◌──◌◌──◌◌──◌──❀*̥˚─┐
  YOU HAVE ESCAPED THE ISLAND
└◌───❀*̥˚───◌˚───◌˚───◌˚───◌❀*̥˚┘\n\n
You paddle away under the stars glad to be away from this cursed place.
What's that though - you seem to be heading for the Bermuda Triangle!!
What could possibly go wrong.....  Find out in the thrilling sequel out soon!!
""")
    qprint(f"{LIGHT_WHITE}You had {inventory} in your possesion.{LIGHT_CYAN}\n\n")
    quit()

# =====================  Call main game function to start if run from command line  ======================
if __name__ == "__main__":
    vod()
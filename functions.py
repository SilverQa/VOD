# qa = {"STICK":False, "FISH":True, "PEANUTS":False,}
# print(qa)

# names = [ 'Alice', 'Bob', 'Trudy' ]
# hobbies = [ 'painting', 'singing', 'hacking']
# ages = [ 21, 17, 22 ]
# def goto_ship():
#     print("""\n\n\n\n
#         You are on a the majestic liner SS TITANIC II, sailing through the Bermuda Triangle
#         You are on deck by the lifeboats surrounded by lots of people, some food and drink. An orchestra is playing.
#         You can go and talk to people, move about, eat or examine things.
#         There is a lifeboat nearby.
#         """)
#     # This is going to make people think they can do anything in this game. We just ignore this input;)
#     nochoice = input("What would you like to do now?  ")
#     print(f"\n\nJust as you are about to {nochoice} you suddenly hit an iceburg!")
#     print("The ship is sinking, there are not enough rafts or vests. Women and children first to the lifeboats!")
#     print("Please choose from one of the numbered actions")

#     choices = [
#         "Elbow everybody else aside and get in the lifeboat",
#         "Others need it more - let them have it.",
#             "Join the archestra and selflessly play as the ship goes down (unfortunately they only have a bagpipe spare)"
#         ]
#     choice = get_input(choices)
#     if choice == 1:
#             print("You manage to get on the lifeboat - you must be very proud!")
#             print("Your additional weight causes the lifeboat to capsize")
#             goto_death("You cling uselessly to the sinking lifeboat")
#         elif choice == 2:
#             print("You help the women and children all safely to the lifeboat and feel a peace descend on you.")
#             goto_death("You sink under the peaceful green water")
#         elif choice == 3:
#             print("The ship sinks beneath you, but using the bagpipe as a flotation device you escape..the sound of the pipes keep the sharks away\n\n\n\n")
#             print("                     SKULL ISLAND")
#             print("                     ~~~~~~~~~~~~")
#             print("A chilling adventure of mystery into the heart of darkness...")
#             time.sleep(1)
#             print("       (Soon to be a major new DISNEYLAND ride!)\n\n")
#             input("Press <ENTER> to begin.")
#             print_big_ascii_gameposter()
#             goto_beach()
#         else:  # should never get a choice this high..
#             goto_death("SYSTEM ERROR #zzzzzz")

# #combine those list using zip() function
# for person,age, hobby in zip(names,ages,hobbies):
#         print (person+" is "+str(age)+"  years old and his/her hobby is "+hobby)

# for i in range(0, 16): # print all colours
#     for j in range(0, 16):
#         code = str(i * 16 + j)
#         sys.stdout.write(u"\u001b[38;5;" + code + "m " + code.ljust(4))
# print(u"\u001b[0m") 

# print(u"\u001b[2J")   # clear screen

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
import random

symbols = """
˚ ༘✶ ⋆｡˚ ⁀➷

Mᴇʟᴀɴɪᴇ Mᴀʀᴛɪᴇɴᴇᴢ- Dᴇᴛᴇɴᴛɪᴏɴ
0:35 ━❍──────── -5:32
↻     ⊲  Ⅱ  ⊳     ↺
VOLUME: ▁▂▃▄▅▆▇ 100%

*♥.•´¸.•*´✶´♡ ¸.•*´´♡*💚˚*
*_○💙_Good morning 💙*˚*
*💚.•´¸.•*´✶´♡ ¸.•*´´♡⛅*
*° ☆ ° ˛*˛☆_Π____*_*˚☆*
*˚ ˛★˛•˚ */______/ ~＼。˚ ˚
*˚ ˛•˛•˚🌈｜ 田田 ｜門｜ ˚*
*🌴╬═🌴╬╬🌴╬╬🌴═╬╬═🌴*╬╬🌴

▂▃▅▇█▓▒░۩۞۩ ۩۞۩░▒▓█▇▅▃▂

ஜ۩۞۩ஜ ¸¸♪·¯·♫♬♫ℒ♡ⓥℯ🌸

░░▄▀▀▀▄░▄▄░░░░░░╠▓░░░░
░░░▄▀▀▄█▄░▀▄░░░▓╬▓▓▓░░
░░▀░░░░█░▀▄░░░▓▓╬▓▓▓▓░
░░░░░░▐▌░░░░▀▀███████▀
▒▒▄██████▄▒▒▒▒▒▒▒▒▒▒▒▒
≿━━━━༺❀༻━━━━≾

*✲*´*。.❄¯*✲。❄。*¨`*✲´*。❄¨`*✲。❄。*`*
*╔════════════ ༺❀༻❤༺❀༻ ════════════╗*
*♥*❄¯*✲❄♫♪♩░B░E░A░U░T░I░F░U░L░ ♫♫♪❄¯*✲❄
*╚════════════ ༺❀༻❤༺❀༻ ════════════╝*
*✲*´*。.❄¯*✲。❄。*¨`*✲´*。❄¨`*✲。❄。*`*

💕💕
ڰۣڿڰۣڿஇღԑ̮̑ঙღڰۣڿڰۣڿஇ  💕💕 ılıll|̲̅̅●̲̅̅|̲̅̅=̲̅̅|̲̅̅●̲̅̅|llılı  💕💕  ڰۣڿڰۣڿஇღԑ̮̑ঙღڰۣڿڰۣڿஇ

                   ______
                  .-"      "-.
                 /            \
                |              |
                |,  .-.  .-.  ,|
                | )(__/  \__)( |
                |/     /\     \|
      (@_       (_     ^^     _)
 _     ) \_______\__|IIIIII|__/__________________________
(_)@8@8{}<________|-\IIIIII/-|___________________________>
       )_/        \          /
      (@           `--------` jgs
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

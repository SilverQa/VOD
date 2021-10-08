import sys
import flask 
import time

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


def qprint(string):
    for i in string:
        print(i, end='')
        time.sleep(0.1)
        sys.stdout.flush()


qprint(CLEAR_SCREEN + RESET +
       "Welcome to SKULL ISLAND\n\nA game of mystery and terror\nAre you ready?")
time.sleep(1)
print(UP+UP+UP+UP+"\nWelcome to "+RED + UNDERLINE+"SKULL ISLAND", end='')
qprint("!!!!!!\n\n"+RESET)
qprint("A game of "+LIGHT_GREEN+"mystery"+LIGHT_WHITE+" and " +
       LIGHT_CYAN+"terror\n"+PURPLE + "Are you ready?"+RESET)

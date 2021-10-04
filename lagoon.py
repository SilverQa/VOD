from vod import *

def goto_lagoon():
    # Qaiser:
    # Called by BEACH.  Goes to TEMPLE, VOLCANO
    print("""
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
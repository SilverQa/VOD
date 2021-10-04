

def narr_print(string, colour = ITALIC + LIGHT_WHITE, delay = 0): #! -- Narrator Print
    for letters in string:
        sys.stdout.write(colour +letters + RESET )
        sys.stdout.flush()
        time.sleep(delay)


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
    narr_print("")
#animated sailing ship
#Call next chapter
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
board_check()
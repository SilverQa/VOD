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
    narr_print("The door handle is cold to the touch, you notice water leaking through the rim of the door\nyou grab the handle and slowly turn it\nopening the door, water starts rushing in, you look through to door gap to gauge how bad the hallway is\nwater seems to be wasit high, you open the door further and start your escape....")
    narr_print("..........\nyou make it to the end of the hallway and find a set of stairs,\nUp is down & down is up, you think whats the best way to get out, as you notice a change in the water level\nthe ship must be leaning to one side\nDo you use the stairs & dive further down or Climb up the sloped ceiling and use the next set of stairs")
    def pick_react():
        narr_print("You need to keep moving, what do you do?\n")
    react =[ "[1] Dive down into the water & follow the Stairs", "[2] Climb up the hallway to the next set of stairs",]
    for pick in react:
        print(pick)
    answer = input()
    answer =int(answer)
    if answer == 1:
        global life_jacket
        if life_jacket ==1:
            narr_print("You won't be able to dive while wearing your life jacket, you quickly remove it & drop it in the water....\n")
            time.sleep(1)
            narr_print("You take one last look of your surroundings & take a deep breath, you drive into the water\ngrabbing onto the rail of the stairs, you use it as a guide, you travel down 2 floors\nfinally at the prominarde deck, you see the a way out into the open water\n you swim for it, once out into the open sea, you look up\nA defeative thought pops into your head, when you realise your too deep & will never make it to the surface....\nbut you swim as quick as you can to the surface, you've not even half way up, before you start to drown\nYour final thoughts are 'Terrible start to retirement'")
            narr_print("..........")
            narr_print("Your limpless body sinks to the abyss....")
            #INSERT GAME OVER
        else:    
            narr_print("You take one last look of your surroundings & take a deep breath, you drive into the water\ngrabbing onto the rail of the stairs, you use it as a guide, you travel down 2 floors\nfinally at the prominarde deck, you see the a way out into the open water\n you swim for it, once out into the open sea, you look up\nA defeative thought pops into your head, when you realise your too deep & will never make it to the surface....\nbut you swim as quick as you can to the surface, you've not even half way up, before you start to drown\nYour final thoughts are 'Terrible start to retirement'")
            narr_print("..........")
            narr_print("Your limpless body sinks to the abyss....")
            #INSERT GAME OVER
        
    elif answer ==2:
        narr_print("You slowly climb the ceiling of the hallway.....\nthe water stops after a while & you realise that you must be above sea level, if the water has stopped rising\nas you reach the top of the hallway, you find the next set of stairs\nnow you must climb down the stairs to reach the prominarde")
        narr_print("...............")
        narr_print("Its 2 decks down, with no water to cushin your fall, if you slip\ntaking your time to get down, you feel the ship tilt more\nthe ship is going to be upright soon like a bottle in the ocean\nyou move quicker, as at this rate you wont be able to get across\nfalling down a hallway is a long way down....\nyou finally make it to the open deck....\nlooking outside you see the sea is chopper, but no storm...\nescapeing is more important now, than trying to figure out what has caused this disaster....\nfinally your outside,")
        if life_jacket ==1:
            narr_print("With your life jacket equiped you jump into the sea, hoping that a life boat will find you....\nbut in the back of your mind before you jump, you do think how quiet it has been....\n")
            time.sleep(1)
            narr_print("......")
            narr_print("Hopefully there are other survioues who will be able to help you.....\nthe thought of drifting in the sea for days...is not a nice thought\nBut it is a better option that being pulled down by the sinking ship.....")
            #END OF CHAPTER, Wake up on beach insert.
            narr_print("")
        elif life_jacket ==0:
            narr_print("You get ready to jump into the ocean.....\n'That Life Jacket would of been great now, shame you didn't collect it' you think to yourself\n Hopefully there are other survioues who will be able to help you.....\nthe thought of drifting in the sea for days...is not a nice thought\nBut it is a better option that being pulled down by the sinking ship.....\nbut without a life jacket there better be something out there to grab onto that floats....\nwith one look back at the sinking ship, you leap into the ocean........")
            #END OF CHAPTER,WAKE UP ON BEACH  
    else:
        narr_print("Don't think thats an option right now....")
        pick_react()
    pick_react()


def open_door_fire():
    global life_jacket
    narr_print("The door handle is hot to the touch, nearly burning your hand\ngrabbing a your jacket you use it to grab the handle\nopening the door, intence heat & smoke fills the room\nyou remember your training & get to the floor and crawl as quick as you can\nstaying low you go past other cabins, some doors are open\nothers must of got out too in time, but you don't see anyone else\nyou keep an eye out for people in need\nthe alarms ringing is deafening, you wouldn't be able to hear anyones scream for help")
    narr_print("..........\nyou make it to the stairs at the end of the hallway,\nthe stairs look stable, but there feels like there is fire further up on the next floor....\nbut further down the hallway is more smoke....")
    def pick_react():
        narr_print("You need to keep moving, what do you do?\n")
    react =[ "[1] Use Stairs", "[2] Walk down hallway to the next set of stairs",]
    for pick in react:
        print(pick)
    answer = input()
    answer =int(answer)
    if answer == 1:
        narr_print("You make your way up the stairs, the smoke filled air blinding you\nthe heat is rising, you realise its worse on this floor & can't go any further....\nlooking back down, you see flames flickering through the smoke.......\nyour trapped, theres nothing you can do, you slowly pass out from the chocking air & heat")
        #GAME OVER insert
    elif answer ==2:
        narr_print("You go past the stairs, staying low and go further through the hallway\n the smoke is thinner here, so you risk getting up to move faster, you rush down the hallway\nsuddenly a large explosion errupts from above and part of the ceiling comes crashing down on top of you")
        if life_jacket ==1:
            narr_print("A cabin door rests on you, coughing from the smoke,\n you look up, the door actualy saved you from the weight of the debris, shielding you from the burst pipes\nwhich would of punctured you like a pin cushion")
            narr_print("You try and lift the door off you, but its too heavy with everything resting on it\nthe smoke is thicking & its getting hotter\nyou try and squeeze out......\nthe life jacket has you wedged in....\nattempting to pull it off fails...\nyou're stuck.....\nas the smoke thickens you start to loose consciousness....\nyou black out, trapped with no one to save you, your fate is sealed...")
            #GAME OVER insert
        elif life_jacket ==0:
            print("A cabin door rests on you, coughing from the smoke,\n you look up, the door actualy saved you from the weight of the debris, shielding you from the burst pipes\nwhich would of punctured you like a pin cushion")
            narr_print("You try and lift the door off you, but its too heavy with everything resting on it\nthe smoke is thicking & its getting hotter\nyou try and squeeze out......\nsuccess....you slip out from under the door & debris and finally make it to the next stair case\nthe smoke is not as thick & the heat has dropped,rushing to the next floor, the conditions get better with each floor\nas you reach the next floor that takes you outside another explosion errupts, but this time from below.....\the rupture launchers you, crashing you head first into the ceiling,\n you fall back down, you try & break the fall, but you're too slow\nhitting the floor, you slowly pass out, whether it be from the smoke or the injury to your head......")
            #END OF CHAPTER, WAke up on beach insert.   
    else:
        narr_print("Don't think thats an option right now....")
        pick_react()
    pick_react()

def posidon():
    narr_print("Something rocks the ship, you half wake up...You think to yourself, its just the waves.....\nYou wait for the ship to rock in the other direction......\nThe sick feeling you get when on a rollercoaster starts to set in,\nyou sit up & realise the ship isn't rocking back, another large dull thud slams into the ship\n....\n..........\n...........\nWith quick realisation, you brace yoursel for what you know will happen next\nthe ship slowly creaks as it rolls over to one side and crachers into the waves......\n............\nYou black out....\nYou wake up to the alarms ringing, you look up and see your bed is on the ceiling....\nAs you slowly get up, you realise its you who is on the ceiling......")
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
            narr_print("You quickly search the cabin for the life jacket.....where is it...\nYou remember its normally stored under the bed....and the bed is on the ceiling\n'No time to waste' you think, you make way for the door")
            narr_print("..............") 
            open_door_fire()
        elif answer == 2:
            narr_print("You havn't got time to to get the life jacket, you need to get off ASAP, you rush for the door...")
            open_door_fire()
        else:
            narr_print("Don't think thats an option right now....")
            pick_react()
    pick_react()            


def fire_ship():
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
            narr_print("..............") 
            open_door_fire()
        elif answer == 2:
            narr_print("Panicing, you ignore looking for the life jacket, there isn't enough time...\nyou rush for the door to escape....")
            open_door_fire()
        else:
            narr_print("Don't think thats an option right now....")
            pick_react()
    pick_react()            


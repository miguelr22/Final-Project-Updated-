#Section 3
#Miguel Rodriguez
#3.17.2021

import time
from player import main_character
def start():
    #This will welcome to Section 3 of the game and start the section.
    #It will tell Section 3's story.
    print("Welcome to Section 3!")
    print(main_character.CharacterName)
    print("Mario lands in a water land where there is a lake in it")
    time.sleep(3)
    print("Mario is about to hop in the water when he sees sea monsters approaching him slowly")
    time.sleep(3)
    #This will ask the player what do they want to and give the player options, they can decice what to do.
    choice=input("What do you want to do?A.Swim through and automatically pass level, B.Rest for the day, or C. Automatically lose a life")
    #This will tell you how many lives the sea mosnters have.
    seamonsterhealth =5
    #This will ask the player what do they want to and give the player options, they can decice what to do.
    if choice =='A':
        while main_character.Lives >=0 and seamonsterhealth >=0:
            print(main_character.CharacterName, " has ", main_character.Lives, " lives.")
            print("Mario decides to swim through the lake avoiding sea monsters")
            #This will run if the player chooses option A in the choice=input command.
            Choice1=input("A.Mario successfully swims through lake, B. Sea Monsters creep up on Mario when reaching land and try to attack, C. Sea Monsters kills Mario")
            #This will let the player know what will happen when that option is chosen.
            # In this case the main character swims through and passes the level .
            if Choice1=='A':
                print("Mario successfully swims through lake without getting attacked by the sea monsters ")
                #Updates main character lives based on the action that the option was chosen
                main_character.Lives +=1
                #Updates villain's health based on the action of the option chosen.
                seamonsterhealth -=1
            #This will let the player know what will happen when that option is chosen.
            #In this case the sea monster want to attack Mario.
            elif Choice1=='B':
                print("Sea Monster creep up on Mario, when he is reaching the land and they try to attack Mario")
            #This will let the player know what will happen when that option is chosen.
            #In this case the main character escapes the villain's
            elif Choice1=='C':
                print("Sea Monster try and and kill Mario but Mario eventually escapes them and goes to safety")
                main_character.Lives +=4
                seamonsterhealth -=4
            #This will print if player doesn't choose any of the option above and doesn't type any options above.
            else:
                print("Invalid input")
    #This will let the player know what will happen when the main character lives less than or equal to zero
    if main_character.Lives >=0:
        print("Congratulations! You have completed the game.")
    #This will let the player know what will happen when sea monster's health is less than or equal to zero.
    if seamonsterhealth >=0:
        print("You have been defeated. Try again!")
    #This will tell the player what happened when option B is chosen.
    elif choice=='B':
        print("Rest for the day")
    #This will tell the player what happened when option C is chosen.
    elif choice=='C':
        print("Automatically lose a life")
    #This will run when the player doesn't choose an option.
    #else:
        #print("Game Over! Try again")



#print("Mario lands in a water land")
#print("Mario sees sea monster approaching him")
#print("Mario decides to jump in the water")
#print("What do you want to do? Swim through, pass the level, rest for the day, continue later, or you can automatically lose a life and move on:)
#print("Mario swims througly avoiding the sea monsters")
#print("Sea Monsters creep up on Mario when he is reaching land to escape them")
#print("Sea Monster try and kill Mario but he eventually escapes ")


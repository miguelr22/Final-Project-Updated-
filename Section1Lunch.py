#Section 1
#Miguel Rodriguez
#3.10.21
#This file includes all the code for the first section of my game.

import Section2Goomba
import time
from player import main_character
#This function will welcome the player into the first section and ask for their name.
def name():
   print("Welcome to Section 1!")
   print("What is your name?")

def start():
    #This function will the main character's name and will ask for the player's name.
    #This function will start telling the story of the game
    global main_character
    main_character.CharacterName = input("What is your name?")
    print(main_character.CharacterName)
    print(main_character.PowerUps)
    print("It was a nice sunny day at 'Mario Park.'")
    #This function will add a delay to the execution of the program.
    time.sleep(3)
    print("Mario and Peach are enjoying a lunch at the park, when they suddenly feel they are being watched.")
    time.sleep(3)
    print("They both turn around and see Bowser hiding in the bushes")
    time.sleep(3)
    print("Bowser approaches them in a very sneaky way that makes Mario and Peach feel uncomfortable")
    time.sleep(3)
    print("Bowser finally approaches Mario and Peach and without saying anything he grabs Peach and takes her away, kidnapps Peach")
    time.sleep(3)
    # This will ask the player what do they want to and give the player options, they can decide what to do.
    choice = input("What do you want to do? A. Fight Bowser, or B. Let Bowser kidnap Peach?")
    #This will run if the player chooses option A in the choice=input function.
    bowserhealth = 5
    if choice == "A":

        while main_character.Lives >= 0 and bowserhealth >= 0:
            print(main_character.CharacterName, " has ", main_character.Lives, " lives.")
            print("Bowser has", bowserhealth, "health remaining")
            print("Bowser jumps up and comes dropping down,What do you do?")
            Choice1 = input(
                "A:Let Bowser knock you out , B:Use a PowerUp, or C: Move out of Bowser's way and let him hurt himself when falling down")
            #This will let the player know what will happen when that option is chosen.
            if Choice1 == 'A':
                print("Let Bowser knock you out")
                #This will update the player's lives and Bowser health.
                main_character.Lives -= 1
                bowserhealth += 1
           #This will let the player use a powerup to fight Bowser, it also explains how the power up is being used.
           #It also removes the powerup when used.
            elif Choice1 == 'B' :
                print("You will use the Star by distracting Bowser")
                if 'Star' in main_character.PowerUps:
                    main_character.PowerUps.remove('Star')
                    main_character.Lives += 1
                    bowserhealth -= 2
                #This will print when the player wants to choose this powerup but is taken and can't be used anymore.
                else:
                    print("You don't have any more Stars!")
           #This will run if player chooses option C and will update them on their Lives.
            elif Choice1 == 'C':
                print("Move out of Bowser's way and let him hurt himself when falling down")
                main_character.Lives += 1
                bowserhealth -= 3
    #This will print if player doesn't choose any of the option above and doesn't type any options above.
        else:
            print("Invalid input")
    #This will let the player know what will happen when the main character lives are greater or equal to zero.
    if main_character.Lives <= 0:
        print("Mario loses all his lives and starts over")
    #This will let the player know what will happen when Bowser health is greater or equal to zero.
    if bowserhealth <= 0:
        print("Bowser escapes!")
    #This will tell the player what happened when option B is chosen.
    elif choice == "B" :
            print("Peach is kidnapped by Bowser and is taken away")
    #This will run when the player doesn't choose an option.
    else:
        print("Moves on to next level")

#This will ask to start Section 2 of the game.

#start()



#print("Mario"")
#print("Princess Peach)
#print("Bowser")
#print("Mario and Peach are enjoying lunch")
#print("Bowser approaches them"
#print("Bowser kidnapps Peach"
#print("What do you want to do ? Fight Bowser or Let Bowser kidnapp Peach?")

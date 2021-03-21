#Section 2
#Miguel Rodriguez
#3.17.21


import time
from player import main_character
def start():
    #This function will welcome you and start Section 2 of the game.
    #It will also tell the story of Section 2.
    print("Welome to Section 2!")
    print(main_character.CharacterName)
    print("Mario lands in a mushroom land")
    time.sleep(3)
    print("Mario looks around and notices a lot of mushrooms")
    time.sleep(3)
    print("The mushrooms don't notice Mario at all,because they are having a gathering.")
    time.sleep(3)
    print("Mario tries to walk by silently, but steps on a rock and gets the mushrooms attention")
    time.sleep(3)
    print("The mushrooms start running towards Mario")
    time.sleep(3)
    #This will ask the player what do they want to and give the player options, they can decice what to do.
    choice=input("What do you want to do?A.Jump on the mushrooms,B.Avoid mushrooms, collect stars and coins, or C. Pass the level once landing in land")
    goombahealth=5
    #This will run if the player chooses option A in the choice=input command.
    if choice=='A':
        #This loop is letting you know while the main character's lives and the villain health is smaller or equal to zero,
        #It will do the following..
        while  main_character.Lives >= 0 and goombahealth >= 0:
            print(main_character.CharacterName, " has ", main_character.Lives, " lives.")
            print("Mario want to fight the mushrooms, he jumps up and comes dropping down")
            #This will give the player 3 options based on the option they chose in the choice=input command.
            Choice1 = input("A. Mario kills all mushrooms, B.Mushrooms kill Mario, or C. Mario and the mushrooms kill each other")
            #This will let the player know what will happen when that option is chosen.
            #In this case main character kills all the mushrooms.
            if Choice1 == 'A':
                print("Mario kills all mushrooms")
                #Updates main character lives based on option
                main_character.Lives += 1
                #Updates villain's health based on the option chosen.
                goombahealth -= 1
            #This will let the player know what will happen when that option is chosen.
            #In this case mushrooms kill the main character
            elif choice =='B':
                print("Mushrooms kill you")
                main_character.Lives -=1
                goombahealth +=1
            #This will let the player know what happens if that option is chosen.
            #In this case the main character and mushrooms kill each other.
            elif Choice1 =='C':
                print("Mushrooms and Mario kills each other")
                main_character.Lives -=3
                goombahealth -=3
            #This will print if player doesn't choose any of the option above and doesn't type any options above.
            else:
                print("Invalid Input")

    #This will let the player know what will happen when the main character lives are greater or equal to zero.
    if main_character.Lives <= 0:
        print("Game Over")
    #This will let the player know what will happen when goomba health is greater or equal to zero.
    if goombahealth <= 0:
        print("Defeated")
    #This will tell the player what happened when option B is chosen.
    elif choice=='B':
        print("You avoid all mushrooms,and collect powerups")
   #This will tell the player what happened when option C is chosen.
    elif choice == 'C':
        print("Level Passed")
    #This will run when the player doesn't choose an option.
    else:
         print("Move on to next level")
    #This will import Section 3 and ask to start Section 3 of the game.
    import Section3Lake

#start()





#print(Goomba)
#print("Mario lands in a mushroom land")
#print("Mario sees that there is a bunch of mushrooms there")
#print("The mushrooms don't notice Mario at all. They are minding their own business.")
#print("Mario tries to walk by silently, but steps on a rock and gets the mushrooms attention")
#print("The mushrooms start to run towards Mario angrily")
#print("What do you want to do? Jump on mushrooms, Avoid muhsrooms and collect coins, or pass level once landing on land")

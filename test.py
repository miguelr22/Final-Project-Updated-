from player import main_character

def name():
   print("Welcome to Section 1!")
   print("What is your name?")
def start():

    main_character.CharacterName = 'Rock'
    print(main_character.CharacterName)
    main_character.CharacterName = input("Enter name")
    print(main_character.CharacterName)
    print(main_character.PowerUps)
start()

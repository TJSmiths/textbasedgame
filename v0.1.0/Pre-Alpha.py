import time
import sys
import random

# Global Variables

hpnum = ""
strnum = ""
magnum = ""
dexnum = ""
fainum = ""
playerclass = ""
charname = ""

def textbox(text):
    for x in text:
        print(x, end='')
        sys.stdout.flush()
        time.sleep(0.05)
    print("")
    return text

def startmenu():
    print("==================================================")
    print("                Placeholder Name")
    print("==================================================")
    print("")

    start_menu = ["1) New Game", "2) Exit"]

    for x in start_menu:
        print(x)

    start_options = input("Welcome to Placeholder, please pick an option: ")

    if start_options == "1":
        class_select()
    elif start_options == "2":
        exit

def class_select():
    classes = ["1) Warrior", "2) Mage", "3) Rogue", "4) Priest", "5) Go Back: "]
    
    warrior_stats = ["STATS", "HP - 120", "Strength - 110", "Magic - 0", "Dexterity - 50", "Faith - 0"]
    mage_stats = ["STATS", "HP - 100", "Strength - 60", "Magic - 100", "Dexterity - 60", "Faith - 0"]
    rogue_stats = ["STATS", "HP - 100", "Strength - 60", "Magic - 0", "Dexterity - 100", "Faith - 20"]
    priest_stats = ["STATS", "HP - 100", "Strength - 40", "Magic - 60", "Dexterity - 60", "Faith - 100"]
    
    for x in classes:
        print(x)
    
    select_class = input("Please pick a class:" )
    
    if select_class == "1":
        for wstats in warrior_stats:
            print(wstats)
        confirm = input("Are you sure? Y/N: ").lower()
        if confirm == "y":
            hpnum = 120
            strnum = 110
            magnum = 0
            dexnum = 50
            fainum = 0
            playerclass = "warrior"
            charname = input("You have selected the Warrior class. Please enter your name to continue: ")
            return hpnum, strnum, magnum, dexnum, fainum, charname, playerclass
        else:
            class_select()
    elif select_class == "2":
        for mstats in mage_stats:
            print(mstats)
        confirm = input("Are you sure? Y/N: ").lower()
        if confirm == "y":
            hpnum = 100
            strnum = 60
            magnum = 100
            dexnum = 60
            fainum = 0
            playerclass = "mage"
            charname = input("You have selected the Mage class. Please enter your name to continue: ")
            return hpnum, strnum, magnum, dexnum, fainum, charname, playerclass
        else:
            class_select()
    elif select_class == "3":
        for rstats in rogue_stats:
            print(rstats)
        confirm = input("Are you sure? Y/N: ").lower()
        if confirm == "y":
            hpnum = 100
            strnum = 60
            magnum = 0
            dexnum = 100
            fainum = 20
            playerclass = "rogue"
            charname = input("You have selected the Rogue class. Please enter your name to continue: ")
            return hpnum, strnum, magnum, dexnum, fainum, charname, playerclass
        else:
            class_select()
    elif select_class == "4":
        for pstats in priest_stats:
            print(pstats)
        confirm = input("Are you sure? Y/N: ").lower()
        if confirm == "y":
            hpnum = 100
            strnum = 50
            magnum = 60
            dexnum = 60
            fainum = 100
            playerclass = "priest"
            charname = input("You have selected the Priest class. Please enter your name to continue: ")
            return hpnum, strnum, magnum, dexnum, fainum, charname, playerclass
        else:
            class_select()
    elif select_class == "5":
        startmenu()

roomsnotvisited = []
roomvisitcounter = 0
boss_time = 10

for i in range(1,51):
    roomsnotvisited.append("room"+str(i))
print(roomsnotvisited)



startmenu()

# Make attack power based off 2 main stats
# Items can be found and add to total attack power meaning I can introduce stat requirements into the game without having to do individual maps per character
# Make 50 rooms for variation, boss is in the 10th room
# Consider making rooms as image assets to load once you have started the game
# create events in the rooms that can influence attack power, then do some maths in the boss room to see if your health goes below 0 and if it does, lose game

import random
import time
import sys

def textbox(text):
    for x in text:
        print(x, end='')
        sys.stdout.flush()
        time.sleep(0.04)
    print(f"")
    return text

roomsnotvisited = []
roomvisitcounter = 0
boss_time = 10

for i in range(1,51):
    roomsnotvisited.append("room"+str(i))

def room1():
    text = "Upon entering the doorway, you notice that the roof has collapsed and blocked off all exits except the one in front of you. Seeing as you can only go forward, you push through"
    textbox(text)
    roomsnotvisited.remove("room1")
    randomroom()

def room2():
    text = ""
    textbox(text)
    roomsnotvisited.remove("room2")
    randomroom()
    
def randomroom():
    global roomvisitcounter, boss_time
    if roomvisitcounter < boss_time:
        roomvisitcounter += 1
        randomiserooms = random.choice(roomsnotvisited)
        goto = globals().get(randomiserooms)
        goto()
    else:
        exit

randomroom()
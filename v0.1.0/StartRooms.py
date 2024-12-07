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

startroom = ["start1", "start2", "start3", "start4", "start5"]

def StartRooms():
    randomisestart = random.choice(startroom)
    goto = globals().get(randomisestart)
    goto()

def start1():
    text = "The sound of lapping waves and noisy seagulls jolts you awake. With no recollection of how you got here, you look around and notice a small cove."
    textbox(text)
    time.sleep(1)
    text = "Hoping that there might be some clues inside the cove you stand up, brushing sand off your arms, then walk towards it in a daze."
    textbox(text)
    time.sleep(1)
    text = "As you approach the entrance, you realise the cove is much deeper than you initially thought and"
    textbox(text)
    time.sleep(0.5)
    text = "."
    textbox(text)
    time.sleep(0.5)
    text = "."
    textbox(text)
    time.sleep(0.5)
    text = "."
    textbox(text)
    time.sleep(0.5)
    text = "is that a door?"
    textbox(text)
    print("")
    print("")
    time.sleep(1)
    text = "You proceed through the door, hoping that what is beyond it will provide answers."
    textbox(text)

def start2():
    text = "You wake to the smell of burning and a thick smoke hangs in the air. Jumping up out of your bed, you make it to the window and assess the drop."
    textbox(text)
    time.sleep(1)
    text = "Wasting no time, you grab your satchel from the other side of the room before hanging out of the window and letting yourself drop."
    textbox(text)
    time.sleep(0.5)
    text = "."
    textbox(text)
    time.sleep(0.5)
    text = "."
    textbox(text)
    time.sleep(0.5)
    text = "."
    textbox(text)
    time.sleep(1)
    text = "Feeling your feet momentarily hit something solid, it is quickly ripped away as you realise you have fallen through the cellar door!"
    textbox(text)
    time.sleep(1)
    text = "Looking up, you see the roaring blaze of what was once an inn above you and, despite the fact the ladder is still intact you decide not to risk going up near the flames."
    textbox(text)
    time.sleep(1)
    print("")
    print("")
    text = "You glance around the cellar and notice a door that seems to lead away from the inn. Knowing that you can't get back up out of the entrance, you decide to push forward."
    textbox(text)

def start3():
    text = "The rumbling of the carriage cart grinds to a halt and you are lifted from the floor of it by your arms."
    textbox(text)
    time.sleep(1)
    text = "With the sack over your head you find it impossible to see. All you can smell is musty cloth, all you can hear are the clanking of chains as other people in the carriage are moved."
    textbox(text)
    time.sleep(1)
    text = "As your are lifted from the carriage, you feel the tight grips on your arms slacken suddenly and a wet dripping noise begins on each side."
    textbox(text)
    time.sleep(1)
    text = "Without warning, the sack over your head is thrown upwards to reveal the night sky, full of stars, above. You glance around."
    textbox(text)
    time.sleep(0.5)
    text = "."
    textbox(text)
    time.sleep(0.5)
    text = "."
    textbox(text)
    time.sleep(0.5)
    text = "."
    textbox(text)
    time.sleep(1)
    text = "You notice you are in a gorge - the arms holding you moments ago severed at the elbows and the bodies nowhere to be found."
    textbox(text)
    time.sleep(1)
    text = "Unlike the others there are no chains on your legs athough... you can't seem to see anyone at all."
    textbox(text)
    time.sleep(1)
    text = "As wet crunching sounds begin above you, you shudder and notice a doorframe in the side of the gorge. Wasting no time, you rush towards it."
    textbox(text)
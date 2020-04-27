
import random
from random import randint
done = False
import time


FUCKFUCKFUCKFUCK = ["I'll fuckin' do it!", "I'll do it!", "I won't puss out this time!", "I can't take it no more." ]


while not done:
    f= open("nuuse.txt", "r")
    if f.mode =="r":
        contents = f.read()

        print(contents)
        print("")
        print(random.choice(FUCKFUCKFUCKFUCK))
        print("")
        time.sleep(0.2)
        


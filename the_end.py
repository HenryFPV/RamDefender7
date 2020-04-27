

done = False
import time

while not done:
    f= open("nuuse.txt", "r")
    if f.mode =="r":
        contents = f.read()


        print(contents)
        print("")
        print("imma hang myself")
        time.sleep(0.2)
        


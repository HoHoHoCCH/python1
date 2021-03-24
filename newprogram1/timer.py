
# This is my first python program, hope you enjoy!
import time
import random

print("Python Program Started.")


def start():
    stop: str = "3"
    time.sleep(1)
    print("`")
    print("`")
    print("`")
    value = float(input("Please enter your time (in seconds, also add .0 at the end.):\n"))
    if type(value) == float:
        anc = "2"
    else:
        start()
    sec = (float(value))
    a = (float(1))
    stop = "1"
    while True:
        if stop == "1":
            print(sec)
            sec = sec - a
            time.sleep(1)
            if sec <= (float(0)):
                sec = (float(0))
                stop = "0"
                if stop >= "0":
                    stop = "2"
                    print("Times Up!")
                    if stop >= "2":
                        Question = input("Again? (yes or no)")
                        if Question == ("yes"):
                            print("Great!")
                            print("**RESTARTING TIMER**")
                            time.sleep(0.5)
                            start()
                        elif Question == ("no"):
                            exit()



start()


































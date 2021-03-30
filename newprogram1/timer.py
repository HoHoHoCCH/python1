
# This is my first python program, hope you enjoy!
import time
import random

print("Python Program Started.")


def start():
    # What is stop, why is it being defined now?
    stop: str = "3"
    # Why are we sleeping?
    time.sleep(1)
    print("`")
    print("`")
    print("`")
    ## What happens if I want a 10 hour timer? 
    ## WHat happens if I enter a string here?
    value = float(input("Please enter your time (in seconds, also add .0 at the end.):\n"))
    if type(value) == float:
        ## what is this variable?
        anc = "2"
    else:
        ## Dont do this. Instead, throw an error and let the program handle this however it wants
        start()

    # Why are you refloating value? its already a float?
    sec = (float(value))
    # Why are you storing float(1)
    a = (float(1))
    # you defined this as 3 earlyer
    #Sorry! In this variable, you can think of each number as a type.
    #                                            -Ching Ho
    stop = "1"
    while True:
        # could we simplify this logic?
        #I don't know how.
        #        - Ching Ho
        if stop == "1":
            print(sec)
            sec = sec - a
            ## Could we get greater resolution here somehow?
            ## What do you mean resolution?
            ##     = Ching Ho
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




## This is a very basic timer implementation. 
## Are there other ways could we do this so we're not locking a cpu thread the entire time?
## What is a CPU
#     - Ching Ho





























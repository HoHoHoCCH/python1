import time
import random

def game2():
    print("`")
    print("`")
    print("`")
    print("Welecome To TimeNumber! Type out the SUM of the numbers within 6 seconds, try beating MY high score! Mine Is 37")
    time.sleep(1)
    rst2 = input("Are You Ready? (yes or no)")
    if rst2 == "yes":
        print("Great! The Game Will Begin Now!")
        time.sleep(1)
        game2ques1()
    else:
         exit()



def game2ques1():
    score = 0
    while True:
        tn1 = random.randint(0, 10)
        tn2 = random.randint(0, 10)
        tn3 = random.randint(0, 10)
        print(tn1, tn2, tn3)
        from threading import Thread

        answer: None = None
        a = 1
        sch = 0

        def check():
            time.sleep(3)
            if answer != None:
                return
            print("Too Slow! You Lose!")
            score = 0
            tryagain123 = input("Try Again?")
            if tryagain123 == "yes":
                game2ques1()
            else:
                exit()



        Thread(target=check).start()

        answer = int(input("Input the answer!"))
        if answer == (tn1 + tn2 + tn3):
            print("Your Answer Was CORRECT. Good Job!")
            # Why are we sleeping?
            time.sleep(1)
            print("Moving On To Next Question!")
            time.sleep(1)
            sch = 1
            game2ques1()
        else:
            print("Wrong Answer")
            score = 0
            # Why is this named tryagain123?
            tryagain123 = input("Try Again?")
            if tryagain123 == "yes":
                game2ques1()
            else:
                exit()

game2()
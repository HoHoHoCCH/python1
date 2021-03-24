# This is my first python program, hope you enjoy!
import time
import random

print("Python Program Started.")


def start():
    import time
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
                            qwe = input(
                                "Selecting No Will Go Back To The Main Screen, are you sure that you want to exit?")
                            if qwe == ("yes"):
                                lobby()
                            elif qwe == ("no"):
                                print("Ok! Then The Timer Will Restart!")
                                print("**RESTARTING TIMER**")
                                time.sleep(0.5)
                                start()
                                break


def  cal():
    print("`")
    print("`")
    print("`")
    final: float = 0
    num: float = 0
    nsm: float = 0
    q: float = 0
    w: float = 0
    print("Welecome To Calculator")
    final: float = 0
    num: float = 0
    nsm: float = 0
    q: float = 0
    w: float = 0
    num = float(input("Enter First Number"))
    q = num
    nsm = float(input("Enter Second Number"))
    w = nsm
    nam = input("add (enter 1), minus (enter 2), multiplication (enter 3) or division (enter 4)")
    if nam == "1":
        final = q + w
    if nam == "2":
        final = num - nsm
    if nam == "3":
        final = q * w
    if nam == "4":
        final = q / w

    print("Calculating Sum...")
    time.sleep(1)
    print(final)
    goback = input("Calculate Again?")
    if goback == "yes":
        cal2()
    else:
        lobby()

def cal2():
    print("`")
    print("`")
    final: float = 0
    num: float = 0
    nsm: float = 0
    q: float = 0
    w: float = 0
    num = float(input("Enter First Number"))
    q = num
    nsm = float(input("Enter Second Number"))
    w = nsm
    nam = input("add (enter 1), minus (enter 2), multiplication (enter 3) or division (enter 4)")
    if nam == "1":
        final = q + w
    if nam == "2":
        final = num - nsm
    if nam == "3":
        final = q * w
    if nam == "4":
        final = q / w


    print("Calculating Sum...")
    time.sleep(1)
    print(final)
    goback = input("Calculate Again?")
    if goback == "yes":
       cal2()
    else:
        lobby()

def htp():
    print("`")
    print("`")
    print("`")
    print("Welecome to How To Play!")
    print("Note: All Try/Play Again or Are You Sure questions can be answered with *yes* or *no*. Anything else will result in choosing no.")
    print("Replies:")
    print("Timer = t, calculator = c, rock paper scissors = rps, timeNumber = tm, e = exit")
    htpa = input("Which tool/game do you not understand?")
    if htpa == "t":
        print("Timer: Enter the time in seconds, and let the program count away.")
        htp()
    if htpa == "c":
        print("Calculator: Enter the first and second number, then the symbol. For example I want to calculate 1 + 2, so 1 is the first number and 2 is the second. For symbols, 1 is for addition, 2 for subtraction, 3 for multiplication, and 4 for division")
        htp()
    if htpa == "rps":
        print("Rock Paper Scissors: Select rock paper or scissors, then the computer will also select one. Rock beats scissors but loses to paper, paper beats rock but loses to scissors, and scissors beats paper but loses to rock")
        htp()
    if htpa == "tm":
        print("timeNumber: Calculate the sum of the 3 numbers shown on screen within 3 seconds.")
        htp()
    if htpa == "e":
        lobby()

def lobby():
    print("`")
    print("`")
    print("`")
    gowhere = input(
        "What Would You Like To Do? (e for exit, rps for rock paper scissors, c for calculator, tm for TimeNumber, htp for How To Play and t for timer)")
    if gowhere == "c":
        cal()
    if gowhere == "t":
        start()
    if gowhere == "e":
        print("Closing Software...")
        time.sleep(1)
        exit()
    if gowhere == "rps":
        game1()
    if gowhere == "tm":
        game2()
    if gowhere == "htp":
        htp()
    else:
        lobby()


def game1():
    print("`")
    print("`")
    print("`")
    print("Welecome To Rock Paper Scissors!")
    time.sleep(0.5)
    user_action = input("Enter a choice (rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
    time.sleep(2)

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    play_again = input("Play again? (yes or no): ")
    if play_again.lower() == "yes":
        game1()
    if play_again.lower == "no":
        lobby()
    else:
        lobby()


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
        game2f()
    else:
        lobby()



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
                lobby()



        Thread(target=check).start()

        answer = int(input("Input the answer!"))
        if answer == (tn1 + tn2 + tn3):
            print("Your Answer Was CORRECT. Good Job!")
            time.sleep(1)
            print("Moving On To Next Question!")
            time.sleep(1)
            sch = 1
            game2ques1()
        else:
            print("Wrong Answer")
            score = 0
            tryagain123 = input("Try Again?")
            if tryagain123 == "yes":
                game2ques1()
            else:
                lobby()


print("Hello!")
lobby()


def game2f():
    score = 1



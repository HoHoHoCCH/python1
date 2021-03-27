import time

def  cal1():
    print("`")
    print("`")
    print("`")
    print("Welecome To Calculator")
    ## What happens here if I enter a string? 
    num = float(input("Enter First Number"))
    q = num
    nsm = float(input("Enter Second Number"))
    w = nsm
    nam = input("add (enter 1), minus (enter 2), multiplication (enter 3) or division (enter 4)")
    ## What happens here if I enter 5 or a ?
    if nam == "1":
        final = q + w
    if nam == "2":
        final = num - nsm
    if nam == "3":
        final = q * w
    if nam == "4":
        final = q / w


        ## Why are we tabbed in here/
        print("Calculating Sum...")
        ## Why do we need to sleep?
        time.sleep(1)
        print(final)

        ## What if we removed this part of the function? Could you do this looping at a higher level
        ## In the program?
        goback = input("Calculate Again?")
        if goback == "yes":
            cal1()
        else:
            exit()

cal1()


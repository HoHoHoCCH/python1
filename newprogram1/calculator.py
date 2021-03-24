import time

def  cal1():
    print("`")
    print("`")
    print("`")
    print("Welecome To Calculator")
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
            cal1()
        else:
            exit()

cal1()


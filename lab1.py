from time import sleep
from random import randint
fibo = [1, 2, 3, 5, 8, 13, 21]
boolean = "trou"
while "2=2":
    num = input("menu:\n1.print 1-100\n2.check fibo\n3.randint numbers until we get 10 or 15 times\n4.out\n")
    if num == "1":
        for x in range(1, 101):
            print(x)
        print("------\n")
        y = input("\nyou want to get out? y/n ")
        if y == "y" or y == "yes":
            break
    elif num == "2":
        print("\n\nthe fibonachi: " + str(fibo))
        for a in range(2, len(fibo)):
            print(fibo[a])
            print(fibo[a - 1])
            print(fibo[a - 2])
            print("\n-----\n")
            if fibo[a] != (fibo[a - 1] + fibo[a - 2]):
                boolean = "false"
                break
            sleep(2)
        if boolean == "trou":
            print("this is good fiborachi")
        else:
            print("somthing is worng")
        sleep(4)
        y = input("\nyou want to get out? y/n ")
        if y == "y" or y == "yes":
            break
    elif num == "3":
        for w in range(15):
            print(randint(1, 100))
            if w == "10":
                print("you won!!")
                break
        print("you didn't won.")
        y = input("\nyou want to get out? y/n ")
        if y == "y" or y == "yes":
            break
    elif num == "4":
        break
    else:
        print("\npick 1-4 only!!\n")

from time import sleep
from random import randint

money = int(input("this is a game of dice(: every throw cost 3$\nhow much money you have? "))
print("you can to throw:" + str(money//3) + " times\n" + "your change: " + str(money%3))
prise=0
for x in range(money//3):
    num1=randint(1,6)
    num2=randint(1,6)
    print("\nrolling cubes for round number: " + str(x+1))
    sleep(3)
    print("\ndice 1: " + str(num1) + "\ndice 2: " + str(num2) + "\n------\n")
    if(num1==num2):
        if (num2+num1==12):
            prise=prise+1000
        else:
            prise=prise+100
    elif(num2==2):
        prise=prise+40
    elif(num1==1):
        prise=prise+20
print("calculate your prise...")
sleep(2)
print("your prise: " + str(prise))


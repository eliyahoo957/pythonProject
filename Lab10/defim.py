from time import sleep

                                    #menu of IP systems and URL system

def menu():
    while True:
        a = input("\nmenu:\n------\n1.ip system \n2.DNS system\n3.to out\n")
        if a == "1":
            ip()
        elif a == "2":
            dns()
        elif a == "3":
            break
        else:
            print("\n1-3 only!!\n\n")
            sleep(3)

#################################################################################################


def ip():
    list = ["1.1.1.1", "2.2.2.2", "3.3.3.3", "4.4.4.4"]
    while True:
        choise1 = input("\n\nIP system:\n------\n1.search for IP from a list\n2.add IP to a list\n3.delete IP from a list\n4.print all the IP's to the screen\n5.To menu\n")
        if choise1 == "1":
            k = input("input ip:")
            print(k in list)
            sleep(3)
        elif choise1 == "2":
            e = input("input IP: ")
            list.append(e)
            print(list)
            sleep(3)
        elif choise1 == "3":
            q = int(input("number of the cell: "))
            list.pop(q-1)
            print(list)
            sleep(3)
        elif choise1 == "4":
            print(list)
            sleep(3)
        elif choise1 == "5":
            break
        else:
            print("tap 1-5 only!!")
            sleep(3)

#############################################################################################3


def dns():
    dict = {"www.n12.co.il": "1.1.1.1", "www.ynet.co.il": "2.2.2.2", "www.google.co.il": "3.3.3.3", "www.apple.co.il": "4.4.4.4"}
    while True:
        choise2 = input("\nDNS system:\n-------\n1.search for URL+IP from a dictionary\n2.add a URL+IP to a dictionary\n3.delete URL from a dictionary\n4.update the ip of specific URL\n5.print all the URL:IP to the screen\n6.To menu\n")
        if choise2 == "1":
            b = input("input URL: ")
            print(b in dict)
            sleep(3)
        elif choise2 == "2":
            Z = input("input URL+IP: ")
            dict.update(Z)
            print(dict)
        elif choise2 == "3":
            s = input("choose URL: ")
            dict.pop(s)
            print(dict)
            sleep(3)
        elif choise2 == "4":
            dd = input("the key: ")
            ff = input("change the value of the key to: ")
            dict[dd] = ff
            print(dict)
            sleep(3)
        elif choise2 == "5":
            print(dict)
            sleep(3)
        elif choise2 =="6":
            break
        else:
            print("tap 1-6 only!!")
            sleep(3)

menu()
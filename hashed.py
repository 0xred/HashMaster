import os
import sys
import pyfiglet
import time
import requests
import hashlib
#############################################
os.system('cls' if os.name == 'nt' else 'clear')
os.system("color B")
ascii_banner = pyfiglet.figlet_format("chacker md5")
print(ascii_banner)
print(" Enter Your Option")
################### Menu ####################
def menu():
    print("[1] md5 cracked")
    print("[2] Generate hash md5")
    print("[3] brute force md5 ")
    print("[0] Exit the program.")
#############################################


############# Function option1 ##############
def option1():
    print(" ")
    print(" <<==============<< md5 Cracked >>================>>")
    gg = input(" Enter md5 Hash : ")
    int =len(gg)
    if int is 32:
            r = requests.get('http://www.nitrxgen.net/md5db/%s'% gg)
            print(" Cracked Hash =====> "+r.text)
            print(" <<================<< Finish >>===================>>")
            print(" ")
            backmenu = input(" Press Enter To Back Menu >>>")
            if backmenu == "":
                os.system('cls')
            print(ascii_banner)
            time.sleep(1)
#############################################

############# Function option2 ##############

def option2():
    print("")
    print(" <<==============<<  hash md5   >>================>>")
    sss = input(" Enter Your word : ")
    str2hash = str(sss)
    result = hashlib.md5(str2hash.encode())
    print(" md5 hash =====> "+result.hexdigest())
    print(" <<================<< Finish >>===================>>")
    print("")
    backmenu = input(" Press Enter To Back Menu >>>")
    if backmenu == "":
        os.system('cls')
        print(ascii_banner)
        time.sleep(1)
#############################################
def option3():
    print("")
    print(" <<==============<<  hash md5   >>================>>")
    hashxx = input(" Enter md5 Hash : ")
    wordxx = input(" Enter word : ")
    haaash = str(wordxx)
    result = hashlib.md5(haaash.encode())
    finaly = result.hexdigest()
    if finaly == hashxx:
        print(" YEEEESS it is hash : "+finaly+" <----> "+hashxx)
    else:
        print(" NOOOOOOOOOOOOOOOOOOOOOO it is NOOOOOOOOTTT ")
    print(" <<================<< Finish >>===================>>")
    print("")
    backmenu = input(" Press Enter To Back Menu >>>")
    if backmenu == "":
        os.system('cls')
        print(ascii_banner)
        time.sleep(1)
################### Menu ####################
menu()
option = int(input(" Enter Your Option: "))

while option != 0:
    if option == 1:
        option1()
    elif option == 2:
        option2()
    elif option == 3:
        option3()
    else:
        print(" Invalid option.")

    print()
    menu()
    option = int(input(" Enter Your Option: "))

print(" Thank For using this program. Goodbye. ") 

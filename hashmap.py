import os
import sys
import pyfiglet
import time
import requests
import hashlib
from urllib.request import urlopen, hashlib
from colorama import Fore, Back, Style
#############################################
os.system('cls' if os.name == 'nt' else 'clear')
os.system("color B")
ascii_banner = pyfiglet.figlet_format("Hash Map")
print(ascii_banner)
################### Menu ####################
def menu():
    print("[1] MD5 Cracked ")
    print("[2] Generate Hash MD5 & SHA1 & SHA256 ")
    print("[3] Brute Force MD5 ")
    print("[4] Brute Force SHA1 ")
    print("[5] Brute Force SHA256 ")
    print("[6] Help ")
    print("[0] Exit the program.")
#############################################


############# Function option1 ##############
def option1():
    print(" ")
    print(" <<==============<< md5 Cracked >>================>>")
    gg = input('\033[1;96m'" Enter MD5 Hash =====> "'\033[1;92m')
    int =len(gg)
    if int is 32:
            r = requests.get('http://www.nitrxgen.net/md5db/%s'% gg)
            print('\033[1;96m'" Cracked Hash =====> "'\033[1;92m'+r.text)
            print('\033[1;96m'" <<================<< Finish >>===================>>")
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
    print(" <<============<< Generate Hash >>================>>")
    sss = input('\033[1;96m'" Enter Your Word =====> "'\033[1;92m')
    str2hash = str(sss)
    md5hash = hashlib.md5(str2hash.encode())
    for i in range(3):
        setpass = bytes(sss, 'utf-8')
    hash_object = hashlib.sha1(setpass)
    sha1hash = hash_object.hexdigest()
    for i in range(3):
        setpass = bytes(sss, 'utf-8')
    hash_object = hashlib.sha256(setpass)
    sha256hash = hash_object.hexdigest()
    print('\033[1;96m'" md5 hash  ========> "'\033[1;92m'+md5hash.hexdigest())
    print('\033[1;96m'" SHA1 hash  =======> "'\033[1;92m'+sha1hash)
    print('\033[1;96m'" SHA256 hash ======> "'\033[1;92m'+sha256hash)
    print('\033[1;96m'" <<================<< Finish >>===================>>")
    print("")
    backmenu = input(" Press Enter To Back Menu >>>")
    if backmenu == "":
        os.system('cls')
        print(ascii_banner)
        time.sleep(1)
#############################################
def option3():
    print(" <<===============<< Brute Force md5 >>=================>>")
    md55hash = input('\033[1;96m'" Add hash To Start Cracked =====> "'\033[1;92m')
    LIST_OF_COMMON_PASSWORDS = str(urlopen("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt").read(), 'utf-8')
    for guess in LIST_OF_COMMON_PASSWORDS.split('\n'):
        hashedlist = hashlib.md5(bytes(guess, 'utf-8')).hexdigest()
        if hashedlist == md55hash:
            print('\033[1;92m'+md55hash+"\033[1;96m <----> \033[1;92m"+hashedlist+ '\033[1;96m'" Password is : " '\033[1;92m'+str(guess)) # True hash
            print('\033[1;96m'"")
            quit()
        elif hashedlist != md55hash:
            print('\033[1;91m'+md55hash+"\033[1;96m <----> \033[1;91m"+hashedlist+ '\033[1;96m'" Error Password : " '\033[1;91m'+str(guess)) # False Hash
    backmenu = input('\033[1;96m'" Press Enter To Back Menu >>>")
    if backmenu == "":
        os.system('cls')
        print(ascii_banner)
        time.sleep(1)
#############################################
def option4():
    print(" <<===============<< Brute Force SHA1 >>=================>>")
    SHA1hash = input("please input the hash to crack.\n>")
    LIST_OF_COMMON_PASSWORDS = str(urlopen("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt").read(), 'utf-8')
    for guess in LIST_OF_COMMON_PASSWORDS.split('\n'):
        hashedlist = hashlib.md5(bytes(guess, 'utf-8')).hexdigest()
        if hashedlist == SHA1hash:
            print('\033[1;92m'+SHA1hash+"\033[1;96m <----> \033[1;92m"+hashedlist+ '\033[1;96m'" Password is : " '\033[1;92m'+str(guess)) # True hash
            print('\033[1;96m'"")
            quit()
        elif hashedlist != SHA1hash:
            print('\033[1;91m'+SHA1hash+"\033[1;96m <----> \033[1;91m"+hashedlist+ '\033[1;96m'" Error Password : " '\033[1;91m'+str(guess)) # False Hash
    backmenu = input('\033[1;96m'" Press Enter To Back Menu >>>")
    if backmenu == "":
        os.system('cls')
        print(ascii_banner)
        time.sleep(1)
#################################################################
def option5():
    print(" <<===============<< Brute Force SHA256 >>=================>>")
    sha256hash = input("please input the hash to crack.\n>")
    LIST_OF_COMMON_PASSWORDS = str(urlopen("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt").read(), 'utf-8')
    for guess in LIST_OF_COMMON_PASSWORDS.split('\n'):
        hashedlist = hashlib.sha256(bytes(guess, 'utf-8')).hexdigest()
        if hashedlist == sha256hash:
            print('\033[1;92m'+sha256hash+"\033[1;96m <----> \033[1;92m"+hashedlist+ '\033[1;96m'" Password is : " '\033[1;92m'+str(guess)) # True hash
            print('\033[1;96m'"")
            quit()
        elif hashedlist != sha256hash:
            print('\033[1;91m'+sha256hash+"\033[1;96m <----> \033[1;91m"+hashedlist+ '\033[1;96m'" Error Password : " '\033[1;91m'+str(guess)) # False Hash
    backmenu = input('\033[1;96m'" Press Enter To Back Menu >>>")
    if backmenu == "":
        os.system('cls')
        print(ascii_banner)
        time.sleep(1)
#################################################################
def option6():
        print(" ")
        print(" <<===============<< How Using Tools? >>=================>>")
        print(" ")
        print("   option 1 : For Cracked hash MD5 Using API :)")
        print("   option 2 : For Generate hash : MD5 or SHA1")
        print("   option 3 : For Brute Force Hash MD5 Using text in Github 10 Million Password ")
        print("   option 4 : For Brute Force Hash SHA1 Using text in Github 10 Million Password ")
        print(" ")
        print(" <<=====================<< Enjoy >>======================>>")
        print(" ")
        backmenu = input('\033[1;96m'" Press Enter To Back Menu >>>")
        if backmenu == "":
            os.system('cls')
        print(ascii_banner)
        time.sleep(1)

#################################################################

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
    elif option == 4:
        option4()
    elif option == 5:
        option5()
    elif option == 6:
        option6()
    else:
        print(" Invalid option.")

    print()
    menu()
    option = int(input(" Enter Your Option: "))

print(" Thank For using this program. Goodbye. ") 
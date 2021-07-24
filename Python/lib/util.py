import os

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def askIntRange(min, max):
    choice = input()
    while not choice.isdigit():
        choice = input("Please enter a valid number: ")
    while int(choice) < min or int(choice) > max:
        choice = input(f"Please enter a number between {min} and {max}: ")
        while not choice.isdigit():
            choice = input("Please enter a valid number: ")
    return int(choice)

def banner():
    print("__   _       ____         _____")
    print("| \ | |     |  _ \       / ____|")
    print("|  \| |_   _| |_) | __ _| |     ___")
    print("| . ` | | | |  _ < / _` | |    / _ \\")
    print("| |\  | |_| | |_) | (_| | |___| (_) |")
    print("|_| \_|\__,_|____/ \__,_|\_____\___/")
    print("-------------------------------------\n")
                                      
                                      
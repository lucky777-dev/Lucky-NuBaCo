#coding:utf-8

import lib.util as util

alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", \
             "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def start():
    util.clear()
    util.banner()
    print("     CONVERTER\n")
    print("Enter the base of your number (2 to 36): ", end="")
    baseSrc = util.askIntRange(2, 36)
    print(f"Enter your number (>= 0): ", end="")
    nbrSrc = askNumberWithBase(baseSrc)
    print(f"Enter the base you want to convert '{nbrSrc}' to (1 to 36): ", end="")
    base = util.askIntRange(2, 36)
    while base == baseSrc:
        print(f"Really? -_- try again (1 to 36 BUT NOT {baseSrc}...): ", end="")
        base = util.askIntRange(2, 36)
    nbr = convertNumberToBase(nbrSrc, baseSrc, base)
    print("\nBase {:2}: {}".format(baseSrc, nbrSrc))
    print("Base {:2}: {}".format(base, nbr))
    input("\nPress enter to continue...")

def askNumberWithBase(base):
    nbr = input()
    nbr = nbr.upper()
    while not validNumberWithBase(nbr, base):
        nbr = input(f"Invalid number. Try again: ")
        nbr = nbr.upper()
    return nbr

def validNumberWithBase(nbr, base):
    for i in nbr:
        if ((not i.isdigit() and not i.isalpha()) or \
            (not i.isdigit() and i.upper() in alpha and alpha.index(i) > base - 11) or \
            (i.isdigit() and int(i) >= base)):
            #   not digit and not A-Z
            #or not digit and letter not in base range
            #
            #Example:
            #If base == 16
            #Then max letter is F
            #alpha.index('F') == 5
            #So max index is (16 - 11)
            #(base - 11) will work for every base
            #If base == 11 max index is 0 (0-9 and letter 'A')
            #cheers mates
            print(f"<'{i}' not possible in base {base}>")
            return False
    return True

def convertNumberToBase(nbrSrc, baseSrc, base):
    nbrDec = 0
    if baseSrc != 10:
        nbrDec = convertToDecimal(nbrSrc, baseSrc)
    else:
        nbrDec = int(nbrSrc)
    if base != 10:
        nbr = convertFromDecimal(nbrDec, base)
    else:
        nbr = str(nbrDec)
    return nbr

def convertToDecimal(nbrSrc, baseSrc):
    nbrDec = 0
    for i in range(len(nbrSrc)):
        if not nbrSrc[i].isdigit():
            nbrDec += ((alpha.index(nbrSrc[i]) + 10) * baseSrc**(len(nbrSrc) - i - 1))
        else:
            nbrDec += int(nbrSrc[i]) * int(baseSrc)**(len(nbrSrc) - i - 1)
    return nbrDec

def convertFromDecimal(nbrDec:int, base:int):
    nbr = ""
    while (nbrDec >= base):
        if nbrDec % base <= 9:
            nbr = str(int(nbrDec % base)) + nbr
        else:
            nbr = alpha[(nbrDec % base) - 10] + nbr
        nbrDec = int(nbrDec / base)
    if nbrDec > 0:
        if nbrDec <= 9:
            nbr = str(nbrDec) + nbr
        else:
            nbr = alpha[nbrDec - 10] + nbr
    return nbr
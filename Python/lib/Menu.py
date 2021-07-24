#coding:utf-8

import lib.util as util
import lib.util as util

def start(options):
    util.clear()
    util.banner()
    print("     MENU\n")
    for i in range(len(options)):
        print(f"{i+1}| {options[i]}")
    print("\n0| Quit\n")
    print("Enter your choice: ", end="")
    return util.askIntRange(0, len(options))
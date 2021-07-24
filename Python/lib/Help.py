#coding:utf-8

import sys

import lib.util as util

def start():
    util.clear()
    util.banner()
    print("     HELP\n")

    print("This software can convert positive numbers from a base to another base.\n")
    print("1. Enter the base your want to use")
    print("2. Enter the number you want to convert")
    print("3. Enter the base you want to convert to\n")
    print("That's it!\n")
    print("  Base minimum and maximum: 2 to 36")
    print(f"Number minimum and maximum: 0 to {sys.maxsize} (in decimal)")
    input("\nPress enter to continue...")
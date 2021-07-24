#coding:utf-8
import lib.Menu as Menu
import lib.Convert as Convert
import lib.Help as Help
import lib.About as About
import lib.util as util
from lib.infos import version


if __name__ == '__main__':
    util.clear()
    menu = ["Convert", "Help", "About"]
    print(f"NuBaCo {version}")
    print("Number base converter.\n")
    choice = Menu.start(menu)
    while(choice != 0):
        if choice == 1:
            Convert.start()
        elif choice == 2:
            Help.start()
        elif choice == 3:
            About.start()
        choice = Menu.start(menu)
    util.clear()
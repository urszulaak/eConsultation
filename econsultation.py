import subprocess
from shared_core.Core import Core

class Main:
    @staticmethod
    def run():
        choice = input("What type of program u want: console - 0, gui - 1: ")
        if int(choice):
            subprocess.run(['python', './gui/main_gui.py'])
        else:
            subprocess.run(['python', './console/main_console.py'])
if __name__ == '__main__':
    Main.run()
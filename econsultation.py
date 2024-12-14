import subprocess
from shared_core.Core import Core

class Main:
    @staticmethod
    def run():
        choice = input("What type of program u want: \u001b[34mconsole - 0\u001b[0m, \u001b[32mgui - 1: \u001b[0m")
        if int(choice):
            subprocess.run(['python', './gui/main_gui.py'])
        else:
            subprocess.run(['python', './console/main_console.py'])
if __name__ == '__main__':
    Main.run()
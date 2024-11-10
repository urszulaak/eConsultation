import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from shared_core.Core import Core
from shared_core.ViewFactory import ViewFactory

class Main:
    @staticmethod
    def run():
        ViewFactory.set_mode("gui")
        app = Core.openController("home")
        app.main()

if __name__ == '__main__':
    Main.run()
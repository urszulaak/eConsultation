import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from shared_core.Controller import Controller
from shared_core.Core import Core
from shared_core.ViewFactory import ViewFactory

class HomeController(Controller):

    def __init__(self,response=None):
        self.homeView = ViewFactory.load_view("home", self)

    def _menuChoice(self, current_row):
        if current_row == 0:
            Core.openController("login").main()
        elif current_row == 1:
            Core.openController("register").main()
        elif current_row == 2:
            Core.openController("information").main()
        elif current_row == 3:
            ViewFactory.set_mode("gui")
            Core.openController("home").main()
        else:
            quit()

    def main(self):
        self.homeView.main()
from core.Controller import Controller
from core.Core import Core

class HomeController(Controller):

    def __init__(self):
        self.homeView = self.loadView("home")
        
    def _menuChoice(self, current_row):
        if current_row == 0:
            Core.openController("login")
        elif current_row == 1:
            Core.openController("register")
        elif current_row == 2:
            Core.openController("information")
        elif current_row == 3:
            Core.openController("graphic")
        else:
            quit()

    def main(self):
        self.homeView.main()
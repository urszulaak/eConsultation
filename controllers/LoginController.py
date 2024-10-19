from core.Controller import Controller
from core.Core import Core

class LoginController(Controller):

    def __init__(self):
        self.loginView = self.loadView("login")
        
    def main(self):
        self.loginView.main()
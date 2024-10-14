from core.Controller import Controller
from core.Core import Core

class HomeController(Controller):

    def __init__(self):
        self.homeView = self.loadView("home")

    def main(self):
        self.homeView.main()
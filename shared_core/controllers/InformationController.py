from core.Controller import Controller
from core.Core import Core

class InformationController(Controller):

    def __init__(self,response=None):
        self.informationView = self.loadView("information")
        
    def main(self):
        self.informationView.main()
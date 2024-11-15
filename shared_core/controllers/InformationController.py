import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from shared_core.Controller import Controller
from shared_core.Core import Core
from shared_core.ViewFactory import ViewFactory

class InformationController(Controller):

    def __init__(self,response=None):
        self.informationView = self.loadView("information")

    def home(self):
        Core.openController("home").main()
        
    def main(self):
        self.informationView.main()
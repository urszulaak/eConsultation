import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from shared_core.Controller import Controller
from shared_core.Core import Core
from shared_core.ViewFactory import ViewFactory
from models.UsersModel import UsersModel

class RegisterController(Controller):

    def __init__(self,response=None):
        self.registerView = self.loadView("register")
        self.usersModel = UsersModel()

    def add(self, fields):
        response = self.usersModel.add(fields)
        print(response)
        if response != 0:
            print("Successfully added!")
        else:
            print("Error while adding")

    def _added(self):
        Core.openController("login").main()
        
    def main(self):
        self.registerView.main()
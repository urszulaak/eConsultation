from core.Controller import Controller
from core.Core import Core
from models.UsersModel import UsersModel

class RegisterController(Controller):

    def __init__(self,response=None):
        self.registerView = self.loadView("register")
        self.usersModel = UsersModel()

    def _add(self, fields):
        response = self.usersModel._add(fields)
        if response != 0:
            print("Successfully added!")
        else:
            print("Error while adding")

    def _added(self):
        pass
        
    def main(self):
        self.registerView.main()
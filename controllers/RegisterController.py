from core.Controller import Controller
from core.Core import Core
from models.UsersModel import UsersModel

class RegisterController(Controller):

    def __init__(self):
        self.registerView = self.loadView("register")
        self.usersModel = UsersModel()

    def _add(self, fields):
        response = self.usersModel.add(fields)
        if response > 0:
            print("Successfully added!")
        else:
            print("Error while adding")
        
    def main(self):
        self.registerView.main()
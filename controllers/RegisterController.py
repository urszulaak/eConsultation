from core.Controller import Controller
from core.Core import Core
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
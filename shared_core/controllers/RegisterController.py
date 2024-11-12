from shared_core.Controller import Controller
from shared_core.Core import Core
from models.UsersModel import UsersModel

class RegisterController(Controller):

    def __init__(self,response=None):
        self.registerView = self.loadView("register")
        self.usersModel = UsersModel()

    def add(self, fields):
        response = self.usersModel.add(fields)
        if response:
            print("Successfully added!")
            return True
        else:
            print("Error while adding")
            return False

    def _added(self):
        Core.openController("login").main()

    def home(self):
        Core.openController("home").main()
        
    def main(self):
        self.registerView.main()
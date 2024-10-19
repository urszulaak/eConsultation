from core.Controller import Controller
from core.Core import Core
from models.UsersModel import UsersModel

class UserMenuController(Controller):

    def __init__(self, response):
        self.userMenuView = self.loadView("userMenu", response)
        self.usersModel = UsersModel()

        
    def main(self):
        self.userMenuView.main()
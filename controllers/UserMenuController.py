from core.Controller import Controller
from core.Core import Core
from models.UsersModel import UsersModel

class UserMenuController(Controller):

    def __init__(self, response):
        self.userMenuView = self.loadView("userMenu", response)
        self.usersModel = UsersModel()
        self.response = response

    def _menuChoice(self, current_row):
        if current_row == 0:
            Core.openController("chooseConsult",self.response).main()
        elif current_row == 1:
            Core.openController("register").main()
        elif current_row == 2:
            Core.openController("information").main()
        else:
            Core.openController("home").main()

    def main(self):
        self.userMenuView.main()
from core.Controller import Controller
from core.Core import Core
from models.UsersModel import UsersModel

class TeacherMenuController(Controller):

    def __init__(self, response):
        self.teacherMenuView = self.loadView("teacherMenu", response)
        self.usersModel = UsersModel()

    def _menuChoice(self, current_row):
        if current_row == 0:
            Core.openController("login").main()
        elif current_row == 1:
            Core.openController("register").main()
        elif current_row == 2:
            Core.openController("information").main()
        else:
            Core.openController("home").main()
        
    def main(self):
        self.teacherMenuView.main()
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from shared_core.Controller import Controller
from shared_core.Core import Core
from shared_core.ViewFactory import ViewFactory
from models.UsersModel import UsersModel

class TeacherMenuController(Controller):

    def __init__(self, response):
        self.teacherMenuView = self.loadView("teacherMenu", response)
        self.usersModel = UsersModel()
        self.response = response

    def menuChoice(self, current_row):
        if current_row == 0:
            Core.openController("addDays",self.response).main()
        elif current_row == 1:
            Core.openController("checkConsult",self.response).main()
        else:
            Core.openController("home").main()
        
    def main(self):
        self.teacherMenuView.main()
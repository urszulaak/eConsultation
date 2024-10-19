from core.Controller import Controller
from core.Core import Core
from models.UsersModel import UsersModel

class TeacherMenuController(Controller):

    def __init__(self, response):
        self.teacherMenuView = self.loadView("teacherMenu", response)
        self.usersModel = UsersModel()

        
    def main(self):
        self.teacherMenuView.main()
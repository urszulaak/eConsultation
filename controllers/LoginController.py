from core.Controller import Controller
from core.Core import Core
from models.UsersModel import UsersModel

class LoginController(Controller):

    def __init__(self,response=None):
        self.loginView = self.loadView("login")
        self.usersModel = UsersModel()

    def _logged(self, fields):
        response = self.usersModel._logged(fields)
        if response != 0:
            print("Successfully logged!")
            return 1
        else:
            return 0
        
    def _isTeacher(self, fields):
        response = self.usersModel._isTeacher(fields)
        if response != 0:
            Core.openController("teacherMenu",response).main()
        else:
            Core.openController("userMenu",response).main()
        
    def main(self):
        self.loginView.main()
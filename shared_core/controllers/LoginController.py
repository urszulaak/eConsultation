import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from shared_core.Controller import Controller
from shared_core.Core import Core
from shared_core.ViewFactory import ViewFactory
from models.UsersModel import UsersModel

class LoginController(Controller):

    def __init__(self,response=None):
        self.loginView = self.loadView("login")
        self.usersModel = UsersModel()

    def _logged(self, fields):
        response = self.usersModel._logged(fields)
        if response != 0:
            Core.openController("userMenu",response).main()
        else:
            return 0
        
    def _isTeacher(self, fields):
        response = self.usersModel._isTeacher(fields)
        if response != 0:
            Core.openController("teacherMenu",response).main()
        else:
            self._logged(fields)

    def _home(self):
        Core.openController("Home").main()
        
    def main(self):
        self.loginView.main()
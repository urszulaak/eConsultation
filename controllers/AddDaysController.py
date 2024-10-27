from core.Controller import Controller
from core.Core import Core
from models.UsersModel import UsersModel

class AddDaysController(Controller):

    def __init__(self,response=None):
        self.addDaysView = self.loadView("addDays")
        self.usersModel = UsersModel()

    def _getDays(self):
        days = []
        for i in range(1,8):
            response = self.usersModel._days(i)
            days.append(response)
        return days

    def main(self):
        self.addDaysView.main()
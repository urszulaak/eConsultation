from core.Controller import Controller
from core.Core import Core
from models.DaysModel import DaysModel
from models.TimeStampsModel import TimeStampsModel
from models.UsersModel import UsersModel

class ChooseConsultController(Controller):

    def __init__(self,response=None):
        self.chooseConsultView = self.loadView("chooseConsult", response)
        self.timeStampsModel = TimeStampsModel()
        self.usersModel = UsersModel()
        self.response = response

    def _getTeachersID(self):
        teachersID = self.timeStampsModel._teachersID()
        return teachersID

    def _getTeachers(self):
        teachers = []
        teachersID = self._getTeachersID()
        for i in teachersID:
            response = self.timeStampsModel._teachers(i)
            teachers.append(response)
        return teachers

    def _getDaysID(self,current_teacher):
        daysID = self.timeStampsModel._daysID(current_teacher)
        return daysID

    def _getDays(self, current_teacher):
        days = []
        daysID = self._getDaysID(current_teacher)
        for i in daysID:
            response = self.timeStampsModel._days(i)
            days.append(response)
        return days

    def _userHome(self):
        Core.openController("userMenu", self.response).main()

    def main(self):
        self.chooseConsultView.main()
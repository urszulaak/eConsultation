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

    def _getStampsID(self, current_teacher, selected_day):
        stampsID = self.timeStampsModel._stampsID(current_teacher, selected_day)
        return stampsID

    def _getStamps(self, current_teacher, selected_day):
        stamps = []
        stampsID = self._getStampsID(current_teacher, selected_day)
        for i in stampsID:
            response = self.timeStampsModel._stamps(i)
            stamps.append(response)
        return stamps

    def _form(self, current_teacher, selected_date, current_stamp):
        pass

    def _userHome(self):
        Core.openController("userMenu", self.response).main()

    def main(self):
        self.chooseConsultView.main()
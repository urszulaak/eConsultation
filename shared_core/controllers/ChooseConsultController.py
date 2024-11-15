import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from shared_core.Controller import Controller
from shared_core.Core import Core
from shared_core.ViewFactory import ViewFactory
from models.DaysModel import DaysModel
from models.TimeStampsModel import TimeStampsModel
from models.UsersModel import UsersModel
from models.ConsultModel import ConsultModel

class ChooseConsultController(Controller):

    def __init__(self,response=None):
        self.chooseConsultView = self.loadView("chooseConsult", response)
        self.timeStampsModel = TimeStampsModel()
        self.usersModel = UsersModel()
        self.consultModel = ConsultModel()
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
        daysID = self.timeStampsModel.daysID(current_teacher)
        return daysID

    def getStampsID(self, current_teacher, selected_day):
        stampsID = self.timeStampsModel._stampsID(current_teacher, selected_day)
        return stampsID

    def getStamps(self, current_teacher, selected_day):
        stamps = []
        stampsID = self.getStampsID(current_teacher, selected_day)
        for i in stampsID:
            response = self.timeStampsModel._stamps(i)
            stamps.append(response)
        return stamps

    def form(self, current_teacher, selected_date, current_stamp, form, user):
        response = self.consultModel.addConsult(current_teacher, selected_date, current_stamp, form, user)
        return response

    def home(self):
        Core.openController("userMenu", self.response).main()

    def main(self):
        self.chooseConsultView.main()
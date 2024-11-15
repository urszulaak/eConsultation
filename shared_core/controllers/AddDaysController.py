import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from shared_core.Controller import Controller
from shared_core.Core import Core
from shared_core.ViewFactory import ViewFactory
from models.DaysModel import DaysModel
from models.TimeStampsModel import TimeStampsModel

class AddDaysController(Controller):

    def __init__(self,response=None):
        self.addDaysView = self.loadView("addDays", response)
        self.daysModel = DaysModel()
        self.timeStampsModel = TimeStampsModel()
        self.response = response

    def _getDays(self):
        days = []
        for i in range(1,8):
            response = self.daysModel.days(i)
            days.append(response)
        return days

    def _getTimeStamps(self):
        timeStamps = []
        for i in range(1,15):
            response = self.timeStampsModel._timeStamps(i)
            timeStamps.append(response)
        return timeStamps

    def _saveTimeStamps(self, selected, current_day, user):
        self.timeStampsModel.delStamps(current_day, user)
        for select in selected:
            self.timeStampsModel._saveTime(select, current_day, user)

    def ifAdded(self, current_teacher, current_day):
        return self.timeStampsModel._stampsID(current_teacher, current_day)

    def _teacherHome(self):
        Core.openController("teacherMenu", self.response).main()

    def main(self):
        self.addDaysView.main()
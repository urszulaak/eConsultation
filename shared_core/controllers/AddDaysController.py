from core.Controller import Controller
from core.Core import Core
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
            response = self.daysModel._days(i)
            days.append(response)
        return days

    def _getTimeStamps(self):
        timeStamps = []
        for i in range(1,15):
            response = self.timeStampsModel._timeStamps(i)
            timeStamps.append(response)
        return timeStamps

    def _saveTimeStamps(self, selected, current_day, user):
        for select in selected:
            response = self.timeStampsModel._saveTime(select, current_day, user)
            if response != 0:
                print("Successfully added!")
            else:
                print("Error while adding")

    def _teacherHome(self):
        Core.openController("teacherMenu", self.response).main()

    def main(self):
        self.addDaysView.main()
from core.Controller import Controller
from core.Core import Core
from models.DaysModel import DaysModel
from models.TimeStampsModel import TimeStampsModel

class CheckConsultController(Controller):

    def __init__(self,response=None):
        self.checkConsultView = self.loadView("checkConsult", response)
        self.timeStampsModel = TimeStampsModel()
        self.response = response

    def getConsult(self):
        consult = []
        response = self.timeStampsModel.consults(self.response)
        print(response)
        return response

    def main(self):
        self.checkConsultView.main()
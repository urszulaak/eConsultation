from core.Controller import Controller
from core.Core import Core
from models.ConsultModel import ConsultModel

class CheckConsultController(Controller):

    def __init__(self,response=None):
        self.checkConsultView = self.loadView("checkConsult", response)
        self.consultModel = ConsultModel()
        self.response = response

    def getConsult(self):
        response = self.consultModel.consults(self.response)
        return response
    
    def teacherHome(self):
        Core.openController("teacherMenu", self.response).main()

    def main(self):
        self.checkConsultView.main()
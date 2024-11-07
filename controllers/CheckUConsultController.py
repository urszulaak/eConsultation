from core.Controller import Controller
from core.Core import Core
from models.ConsultModel import ConsultModel

class CheckUConsultController(Controller):

    def __init__(self,response=None):
        self.checkUConsultView = self.loadView("checkUConsult", response)
        self.consultModel = ConsultModel()
        self.response = response

    def getConsult(self):
        consult = []
        response = self.consultModel.consultsU(self.response)
        return response
    
    def userHome(self):
        Core.openController("userMenu", self.response).main()

    def main(self):
        self.checkUConsultView.main()
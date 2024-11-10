import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from shared_core.Controller import Controller
from shared_core.Core import Core
from shared_core.ViewFactory import ViewFactory
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
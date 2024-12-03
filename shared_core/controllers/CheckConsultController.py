import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from shared_core.Controller import Controller
from shared_core.Core import Core
from shared_core.ViewFactory import ViewFactory
from models.ConsultModel import ConsultModel

class CheckConsultController(Controller):

    def __init__(self,response=None):
        self.response = response
        self.consultModel = ConsultModel()
        self.checkUConsultView = self.loadView("checkUConsult", response)

    def getConsult(self):
        response = self.consultModel.consults(self.response)
        return response
    
    def delete_consult(self, consult_id):
        self.consultModel.delete_by_id(consult_id)
    
    def home(self):
        Core.openController("teacherMenu", self.response).main()

    def main(self):
        self.checkConsultView.main()
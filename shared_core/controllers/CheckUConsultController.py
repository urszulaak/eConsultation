import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from shared_core.Controller import Controller
from shared_core.Core import Core
from shared_core.ViewFactory import ViewFactory
from models.ConsultModel import ConsultModel

class CheckUConsultController(Controller):

    def __init__(self,response=None):
        self.checkUConsultView = self.loadView("checkUConsult", response)
        self.consultModel = ConsultModel()
        self.response = response

    def getConsult(self):
        response = self.consultModel.consultsU(self.response)
        return response
    
    def delete_consult(self, consult_id):
        self.consultModel.delete_by_id(consult_id)
    
    def home(self):
        Core.openController("userMenu", self.response).main()

    def main(self):
        self.checkUConsultView.main()
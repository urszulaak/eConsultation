import abc
import importlib

class Controller(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def main(self):
        return

    def loadView(self, viewName):
        response = None
        
        viewName = viewName[0].upper()+viewName[1:]+"View"

        module = importlib.import_module("views."+viewName)
        class_ = getattr(module, viewName)
        response = class_(self)
        
        return response
import abc
import importlib

class Controller(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def main(self):
        return

    def loadView(self, view):
        response = None
        
        viewName = view[0].upper()+view[1:]+"View"

        module = importlib.import_module("views."+viewName)
        class_ = getattr(module, viewName)
        response = class_(self)
        
        return response
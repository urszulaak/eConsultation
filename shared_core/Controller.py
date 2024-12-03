import abc
import importlib
from shared_core.ViewFactory import ViewFactory

class Controller(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def main(self):
        return

    def loadView(self, view, optional_param=None):
        return ViewFactory.load_view(view, self, optional_param)
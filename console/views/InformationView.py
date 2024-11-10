from core.View import View
import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle

class InformationView(View):

    def __init__(self, controller,response=None):
        super().__init__()
        self.informationController = controller

    def main(self):
        wrapper(self._content)

    def close(self):
        return
    
from core.View import View
import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle

class LoginView(View):

    def __init__(self, controller):
        super().__init__()
        self.loginController = controller

    def main(self):
        wrapper(self._content)

    def close(self):
        return

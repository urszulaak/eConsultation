import time
from shared_core.View import View
import curses
from curses import wrapper
from curses.textpad import Textbox
from views.Custom import Custom

class RegisterView(View):

    def __init__(self, controller,response=None):
        super().__init__()
        self.registerController = controller
        self.custom = Custom

    def _content(self, stdscr):
        curses.curs_set(1)
        h, w = stdscr.getmaxyx()
        self.custom.clearContent(stdscr)
        self.custom.initialize_colors(stdscr)
        content = ['Teacher account [t/T]: ','FirstName: ', 'LastName: ', 'Login: ', 'Password: ']
        menu_height = 10
        message = "Exit to menu [ctrl + E]"
        stdscr.addstr(menu_height + 2, w//2-(len(message)//2), message,curses.color_pair(5))
        fields = self.custom.input(stdscr, content, 4)
        if fields == -1:
            self.registerController.home()
        if self.registerController.add(fields):
            success = "\u2705 SUCCESSFULLY ADDED! \u2705"
            success2 = "    SUCCESSFULLY ADDED!    "
            self.custom.message(stdscr, success, success2, 1)
            self.registerController.added()
        else:
            exist = "\u274c USER WITH THIS LOGIN EXIST! \u274c"
            exist2 = "    USER WITH THIS LOGIN EXIST!    "
            self.custom.message(stdscr, exist, exist2, 0)
            curses.curs_set(0)
            self._content(stdscr)

    def main(self):
        wrapper(self._content)

    def close(self):
        return

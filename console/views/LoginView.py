import time
from shared_core.View import View
import curses
from curses import wrapper
from views.Custom import Custom
from curses.textpad import Textbox

class LoginView(View):

    def __init__(self, controller,response=None):
        super().__init__()
        self.loginController = controller
        self.custom = Custom

    def _content(self, stdscr):
        h, w = stdscr.getmaxyx()
        self.custom.clearContent(stdscr)
        self.custom.initialize_colors(stdscr)
        curses.curs_set(1)
        content = ['Login: ', 'Password: ']
        menu_height = 11
        message = "Exit to menu [ctrl + E]"
        stdscr.addstr(menu_height+1, w // 2 - (len(message) // 2), message,curses.color_pair(5))
        fields = self.custom.input(stdscr, content, 1)
        if fields == -1:
            self.loginController.home()
        self.loginController.isTeacher(fields)
        no_user_found = "\u274c NO USER FOUND! \u274c"
        no_user_found2 = "    NO USER FOUND!    "
        self.custom.message(stdscr,no_user_found,no_user_found2,0)
        self.main()
        stdscr.getch()

    def _clearContent(self, stdscr, h, w, menu_height):
        start_y = menu_height + 1
        end_y = h

        for i in range(start_y, end_y):
            stdscr.move(i, 0)
            stdscr.clrtoeol()
        stdscr.refresh()

    def main(self):
        wrapper(self._content)

    def close(self):
        return

from core.View import View
import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle

class UserMenuView(View):

    def __init__(self, controller, response):
        super().__init__()
        self.userMenuController = controller
        self.response = response

    def _content(self, stdscr):
        curses.curs_set(0)
        h, w = stdscr.getmaxyx()
        menu_height = 10
        self._clearContent(stdscr, h, w, menu_height)
        stdscr.addstr(h//2, w//2, "User: "+str(self.response))
        stdscr.refresh()
        stdscr.getch()

    def _clearContent(self, stdscr, h, w, menu_height):
        start_y = menu_height + 1
        end_y = h - 1

        for i in range(start_y, end_y):
            stdscr.move(i, 1)
            stdscr.clrtoeol()
        stdscr.border()
        stdscr.refresh()

    def main(self):
        wrapper(self._content)

    def close(self):
        return
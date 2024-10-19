from core.View import View
import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle

class TeacherMenuView(View):

    def __init__(self, controller, response):
        super().__init__()
        self.informationController = controller
        self.response = response

    def _content(self, stdscr):
        curses.curs_set(0)
        h, w = stdscr.getmaxyx()
        stdscr.addstr(h//2, w//2, str(self.response))
        stdscr.refresh()
        stdscr.getch()

    def main(self):
        wrapper(self._content)

    def close(self):
        return
from core.View import View
import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle

class AddDaysView(View):

    def __init__(self, controller,response=None):
        super().__init__()
        self.addDaysController = controller

    def _content(self, stdscr):
        curses.curs_set(1)
        h, w = stdscr.getmaxyx()
        menu_height = 10
        curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLUE)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(4, curses.COLOR_RED, curses.COLOR_RED)
        available_height = h - menu_height - 1
        line = "Choose day"
        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(menu_height + 1, w // 2 - (len(line) // 2), line)
        stdscr.attroff(curses.color_pair(3))
        days = self.addDaysController._getDays()
        stdscr.attron(curses.color_pair(3))
        available_width = w // len(days)
        i=0
        for i, day in enumerate(days):
            x_position = available_width * i
            win_day = curses.newwin(5, available_width, menu_height+2, x_position)
            win_day.attron(curses.color_pair(3))
            win_day.box()
            text = str(day)
            text_x = (available_width - len(text)) // 2
            text_y = 5 // 2
            win_day.addstr(text_y, text_x, str(day))
            win_day.refresh()
            win_day.attroff(curses.color_pair(3))
        stdscr.getch()

    def main(self):
        wrapper(self._content)

    def close(self):
        return
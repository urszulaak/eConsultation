import locale
import os
from core.View import View
import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle

class TeacherMenuView(View):

    def __init__(self, controller, response):
        super().__init__()
        self.teacherMenuController = controller
        self.response = response

    def _content(self, stdscr, current_row):
        curses.curs_set(0)
        h, w = stdscr.getmaxyx()
        menu_height = 10
        self._clearContent(stdscr, h, w, menu_height)
        locale.setlocale(locale.LC_ALL, '')
        stdscr.encoding = 'utf-8'
        os.environ['PYTHONIOENCODING'] = 'utf-8'
        content = ['Update details','Add consultation day','Check consultation']
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
        num_items = len(content)
        
        available_height = h - menu_height
        
        box_height = available_height // num_items
        
        box_width = w - 2

        for id, row in enumerate(content):
            x = 1
            y = menu_height + id * box_height

            win = curses.newwin(box_height, box_width, y, x)
            win.box()

            text_x = (box_width - len(row)) // 2
            text_y = box_height // 2

            if id == current_row:
                win.attron(curses.color_pair(1))
                win.addstr(text_y, text_x, row)
                win.attroff(curses.color_pair(1))
            else:
                win.addstr(text_y, text_x, row)

            win.refresh()
                
        stdscr.getch()

    def _move(self, stdscr):
        h, w = stdscr.getmaxyx()
        menu_height = 10
        current_row = 0
        content = ['Update details','Add consultation day','Check consultation']
        self._content(stdscr, current_row)
        while 1:
            key = stdscr.getch()
            if key == (curses.KEY_UP) and current_row > 0:
                current_row -= 1
            elif key == curses.KEY_DOWN and current_row < len(content)-1:
                current_row += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                self._clearContent(stdscr, h, w, menu_height)
                self.homeController._menuChoice(current_row)
            elif key in [ord('l'), ord('r'), ord('i'), ord('g'), ord('e')]:
                if key == ord('l'):
                    current_row = 0
                elif key == ord('r'):
                    current_row = 1
                elif key == ord('i'):
                    current_row = 2
                elif key == ord('g'):
                    current_row = 3
                elif key == ord('e'):
                    current_row = 4
                self._clearContent(stdscr, h, w, menu_height)
                self.homeController._menuChoice(current_row)
            
            self._content(stdscr, current_row)

    def _clearContent(self, stdscr, h, w, menu_height):
        start_y = menu_height + 1
        end_y = h - 1

        for i in range(start_y, end_y):
            stdscr.move(i, 1)
            stdscr.clrtoeol()
        stdscr.border()
        stdscr.refresh()

    def main(self):
        wrapper(self._move)

    def close(self):
        return
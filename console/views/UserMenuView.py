import locale
import os
from shared_core.View import View
import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle

class UserMenuView(View):

    def __init__(self, controller, response):
        super().__init__()
        self.userMenuController = controller
        self.response = response

    def _content(self, stdscr, current_row, content):
        curses.curs_set(0)
        h, w = stdscr.getmaxyx()
        menu_height = 10
        locale.setlocale(locale.LC_ALL, '')
        stdscr.encoding = 'utf-8'
        os.environ['PYTHONIOENCODING'] = 'utf-8'
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
        curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
        num_items = len(content)

        available_height = h - menu_height - 1

        box_height = available_height // num_items

        box_width = w - 2

        for id, row in enumerate(content):
            x = 1
            y = menu_height + id * box_height

            win = curses.newwin(box_height, box_width, y, x)
            win.attron(curses.color_pair(2))
            win.box()
            win.attroff(curses.color_pair(2))

            text_x = (box_width - len(row)) // 2
            text_y = box_height // 2

            if id == current_row:
                win.attron(curses.color_pair(1))
                win.addstr(text_y, text_x, row)
                win.attroff(curses.color_pair(1))
            else:
                win.addstr(text_y, text_x, row)

            win.refresh()

    def _clearContent(self, stdscr, h, w, menu_height):
        start_y = menu_height + 1
        end_y = h

        for i in range(start_y, end_y):
            stdscr.move(i, 1)
            stdscr.clrtoeol()
        stdscr.refresh()

    def _move(self, stdscr):
        h, w = stdscr.getmaxyx()
        menu_height = 9
        current_row = 0
        content = ['Book consultation [B]', 'Check consultations status [C]', 'Update details [U]', 'Log out [ctrl + E]']
        self._content(stdscr, current_row, content)
        while 1:
            key = stdscr.getch()
            if key == (curses.KEY_UP) and current_row > 0:
                current_row -= 1
            elif key == curses.KEY_DOWN and current_row < len(content) - 1:
                current_row += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                self._clearContent(stdscr, h, w, menu_height)
                self.userMenuController._menuChoice(current_row)
            elif key == 5:
                current_row = 3
                self._clearContent(stdscr, h, w, menu_height)
                stdscr.refresh()
                self.userMenuController._menuChoice(current_row)
            elif key in [ord('b'), ord('c'), ord('u')]:
                if key == ord('b'):
                    current_row = 0
                elif key == ord('c'):
                    current_row = 1
                elif key == ord('u'):
                    current_row = 2
                self._clearContent(stdscr, h, w, menu_height)
                self.userMenuController._menuChoice(current_row, self.response)

            self._content(stdscr, current_row, content)

    def main(self):
        wrapper(self._move)

    def close(self):
        return
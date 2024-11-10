import time
from shared_core.View import View
import curses
from curses import wrapper
from curses.textpad import Textbox
import locale
import os

class RegisterView(View):

    def __init__(self, controller,response=None):
        super().__init__()
        self.registerController = controller

    def _content(self, stdscr):
        curses.curs_set(1)
        locale.setlocale(locale.LC_ALL, '')
        stdscr.encoding = 'utf-8'
        os.environ['PYTHONIOENCODING'] = 'utf-8'
        h, w = stdscr.getmaxyx()
        content = ['Type of account [t/s]: ','FirstName: ', 'LastName: ', 'Login: ', 'Password: ']
        menu_height = 10
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(4, curses.COLOR_RED, curses.COLOR_RED)
        curses.init_pair(5, curses.COLOR_GREEN, curses.COLOR_GREEN)

        available_height = h - menu_height - 1
        num_items = len(content)
        box_height = available_height // num_items
        fields = []
        y = 0

        for id, row in enumerate(content):
            x = 1
            y = menu_height + id * 2

            win = curses.newwin(3, w - 4, y, x)
            text_x = 2
            text_y = 1
            win.attron(curses.color_pair(3))
            win.addstr(text_y, text_x, row)
            win.attroff(curses.color_pair(3))
            win.refresh()

            win_text = curses.newwin(1, w - len(row) - 6, y + 1, x + len(row) + 2)
            box = Textbox(win_text)
            win_text.refresh()

            #stdscr.hline(y + 2, x + len(row) + 1, curses.ACS_HLINE, w - len(row))
            stdscr.refresh()
            while True:
                input_text = box.edit()
                win_text.refresh()
                fields.append(input_text.strip())
                break


        self._clearContent(stdscr, h, w, menu_height)
        if self.registerController.add(fields):
            win_shadow = curses.newwin(h // 3, w // 4, h // 2 - h // 6 + 1, w // 2 - w // 8 + 1)
            win_shadow.attron(curses.color_pair(4))
            win_shadow.box()
            win_shadow.refresh()
            win_shadow.attroff(curses.color_pair(4))

            win_success = curses.newwin(h // 3, w // 4, h // 2 - h // 6, w // 2 - w // 8)
            win_success.attron(curses.color_pair(1))
            win_success.box()
            win_success.refresh()
            win_success.attroff(curses.color_pair(1))

            success = "\u2705 SUCCESSFULLY ADDED! \u2705"
            success2 = "    SUCCESSFULLY ADDED!    "
            text_x = (w // 4 - len(success)) // 2
            text_y = h // 3 // 2
            curses.curs_set(0)
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(h // 2, w // 2 - (len(success) // 2) - 1, success)
            stdscr.refresh()
            time.sleep(0.6)
            stdscr.addstr(h // 2, w // 2 - (len(success2) // 2) - 1, success2)
            stdscr.refresh()
            time.sleep(0.6)
            stdscr.addstr(h // 2, w // 2 - (len(success) // 2) - 1, success)
            stdscr.refresh()
            time.sleep(0.6)
            stdscr.attroff(curses.color_pair(1))
            self._clearContent(stdscr, h, w, menu_height)
            stdscr.refresh()
            self.registerController._added()
        else:
            win_shadow = curses.newwin(h // 3, w // 4, h // 2 - h // 6 + 1, w // 2 - w // 8 + 1)
            win_shadow.attron(curses.color_pair(4))
            win_shadow.box()
            win_shadow.refresh()
            win_shadow.attroff(curses.color_pair(4))

            win_error = curses.newwin(h // 3, w // 4, h // 2 - h // 6, w // 2 - w // 8)
            win_error.attron(curses.color_pair(2))
            win_error.box()
            win_error.refresh()
            win_error.attroff(curses.color_pair(2))

            exist = "\u274c USER WITH THIS LOGIN ALREADY EXIST! \u274c"
            exist2 = "    USER WITH THIS LOGIN ALREADY EXIST!    "
            curses.curs_set(0)
            stdscr.attron(curses.color_pair(2))
            stdscr.addstr(h // 2, w // 2 - (len(exist) // 2) - 1, exist)
            stdscr.refresh()
            time.sleep(0.6)
            stdscr.addstr(h // 2, w // 2 - (len(exist2) // 2) - 1, exist2)
            stdscr.refresh()
            time.sleep(0.6)
            stdscr.addstr(h // 2, w // 2 - (len(exist) // 2) - 1, exist)
            stdscr.refresh()
            time.sleep(0.6)
            stdscr.attroff(curses.color_pair(2))
            self._clearContent(stdscr, h, w, menu_height)
            stdscr.refresh()
            self._content(stdscr)

    def _clearContent(self, stdscr, h, w, menu_height):
        start_y = menu_height + 1
        end_y = h

        for i in range(start_y, end_y):
            stdscr.move(i, 1)
            stdscr.clrtoeol()
        stdscr.refresh()

    def main(self):
        wrapper(self._content)

    def close(self):
        return

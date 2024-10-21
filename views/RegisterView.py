from core.View import View
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
        content = ['Type of acc [t/s]*: ','FirstName*: ', 'LastName*: ', 'Login*: ', 'Password*: ', 'PhoneNumber: ', 'Email: ']
        menu_height = 9
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        available_height = h - menu_height
        num_items = len(content) + 1
        box_height = available_height // num_items
        fields = []
        for id, row in enumerate(content):
            x = 1
            y = menu_height + id * box_height
            win = curses.newwin(3, w - 4, y, x)
            win_text = curses.newwin(1, w - 4, y+3, x+2)
            text_x = 2
            text_y = 1
            win.attron(curses.color_pair(1))
            win.addstr(text_y, text_x, row)
            win.attroff(curses.color_pair(1))
            win.refresh()

            box = Textbox(win_text)
            win_text.refresh()

            stdscr.hline(y + 4, x + 2, curses.ACS_HLINE, w - 8)
            stdscr.refresh()

            input_text = ""
            while True:
                input_text = box.edit()
                win_text.refresh()
                fields.append(input_text.strip())
                break
                

        self._clearContent(stdscr, h, w, menu_height)
        self.registerController._add(fields)
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

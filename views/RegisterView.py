from core.View import View
import curses
from curses import wrapper
from curses.textpad import Textbox
import locale
import os

class RegisterView(View):

    def __init__(self, controller):
        super().__init__()
        self.registerController = controller

    def _content(self, stdscr):
        curses.curs_set(1)  # Ustawienie widoczności kursora
        locale.setlocale(locale.LC_ALL, '')
        stdscr.encoding = 'utf-8'
        os.environ['PYTHONIOENCODING'] = 'utf-8'
        h, w = stdscr.getmaxyx()
        content = ['FirstName*: ', 'LastName*: ', 'Login*: ', 'Password*: ', 'PhoneNumber: ', 'Email: ']
        menu_height = 10  # Dostosuj wysokość menu, jeśli to potrzebne
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_WHITE)

        fields = []

        for id, row in enumerate(content):
            x = 1
            y = menu_height-1 + id*3  # Użyj 3 jako wysokości dla każdego pola
            text_len=len(row)
            win = curses.newwin(3, w - 2, y, x)  # Stworzenie okna dla każdego pola
            win_text = curses.newwin(1, w - 4, y+2, x+1)

            text_x = 2
            text_y = 1

            win.addstr(text_y, text_x, row)

            box = Textbox(win_text)
            win.refresh()

            input_text = ""
            while True:
                input_text = box.edit()
                
                fields.append(input_text.strip())
                break
                
            win.refresh()

        print(fields)
        self.registerController._add(fields)
        stdscr.refresh()
        self._clearContent(stdscr, h, w, menu_height)
        self.registerController._added()
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

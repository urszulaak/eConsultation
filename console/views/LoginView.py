import time
from shared_core.View import View
import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle
import threading

class LoginView(View):

    def __init__(self, controller,response=None):
        super().__init__()
        self.loginController = controller

    def _content(self, stdscr):
        curses.curs_set(1)
        h, w = stdscr.getmaxyx()
        content = ['Login: ', 'Password: ']
        menu_height = 10
        curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLUE)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(4, curses.COLOR_RED, curses.COLOR_RED)
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

            stdscr.refresh()
            while True:
                input_text = box.edit()
                win_text.refresh()
                fields.append(input_text.strip())
                break

        self.loginController._isTeacher(fields)
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

        no_user_found = "\u274c NO USER FOUND! \u274c"
        no_user_found2 = "    NO USER FOUND!    "
        text_x = (w // 4 - len(no_user_found)) // 2
        text_y = h // 3 // 2
        curses.curs_set(0)
        stdscr.attron(curses.color_pair(2))
        stdscr.addstr(h//2, w//2-(len(no_user_found)//2)-1, no_user_found)
        stdscr.refresh()
        time.sleep(0.6)
        stdscr.addstr(h//2, w//2-(len(no_user_found2)//2)-1, no_user_found2)
        stdscr.refresh()
        time.sleep(0.6)
        stdscr.addstr(h//2, w//2-(len(no_user_found)//2)-1, no_user_found)
        stdscr.refresh()
        time.sleep(0.6)
        stdscr.attroff(curses.color_pair(2))
        self._clearContent(stdscr, h, w, menu_height)
        stdscr.refresh()
        self.main()
        stdscr.getch()

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

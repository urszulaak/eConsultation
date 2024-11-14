from shared_core.View import View
import curses
import time
from curses import wrapper
from curses.textpad import Textbox, rectangle

class CheckUConsultView(View):

    def __init__(self, controller,response=None):
        super().__init__()
        self.checkUConsultController = controller
        self.response = response

    def _content(self, stdscr, current_row, content):
        curses.curs_set(0)
        h, w = stdscr.getmaxyx()
        menu_height = 10
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
        curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(4, curses.COLOR_RED, curses.COLOR_RED)
        exit_text = "Exit [ctrl+E]"
        stdscr.attron(curses.color_pair(2))
        stdscr.addstr(menu_height+1, w//2-(len(exit_text)//2), exit_text)
        stdscr.attroff(curses.color_pair(2))
        menu_height = 12
        num_items = len(content)
        if not num_items:
            self._noConsult(stdscr, menu_height)
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

            text_x = 2
            text_y = box_height // 2

            if id == current_row:
                win.attron(curses.color_pair(1))
                win.addstr(text_y, text_x, str(row)[2:-2])
                win.attroff(curses.color_pair(1))
            else:
                win.addstr(text_y, text_x, str(row)[2:-2])

            win.refresh()

    def _clearContent(self, stdscr, h, w, menu_height):
        start_y = menu_height + 1
        end_y = h

        for i in range(start_y, end_y):
            stdscr.move(i, 0)
            stdscr.clrtoeol()
        stdscr.refresh()

    def _move(self, stdscr):
        h, w = stdscr.getmaxyx()
        menu_height = 9
        current_row = 0
        content = self.checkUConsultController.getConsult()
        self._content(stdscr, current_row, content)
        while 1:
            key = stdscr.getch()
            if key == (curses.KEY_UP) and current_row > 0:
                current_row -= 1
            elif key == curses.KEY_DOWN and current_row < len(content) - 1:
                current_row += 1
            elif key == 5:
                self._clearContent(stdscr, h, w, menu_height)
                stdscr.refresh()
                self.checkUConsultController.userHome()

            self._content(stdscr, current_row, content)

    def _noConsult(self, stdscr, menu_height):
        h, w = stdscr.getmaxyx()
        win_shadow = curses.newwin(h // 3, w // 4, h // 2 - h // 6 + 1, w // 2 - w // 8 + 1)
        win_shadow.attron(curses.color_pair(4))
        win_shadow.box()
        win_shadow.refresh()
        win_shadow.attroff(curses.color_pair(4))

        win_error = curses.newwin(h // 3, w // 4, h // 2 - h // 6, w // 2 - w // 8)
        win_error.attron(curses.color_pair(3))
        win_error.box()
        win_error.refresh()
        win_error.attroff(curses.color_pair(3))

        no_user_found = "\u274c NO CONSULT FOUND! \u274c"
        no_user_found2 = "    NO CONSULT FOUND!    "
        text_x = (w // 4 - len(no_user_found)) // 2
        text_y = h // 3 // 2
        curses.curs_set(0)
        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(h//2, w//2-(len(no_user_found)//2)-1, no_user_found)
        stdscr.refresh()
        time.sleep(0.6)
        stdscr.addstr(h//2, w//2-(len(no_user_found2)//2)-1, no_user_found2)
        stdscr.refresh()
        time.sleep(0.6)
        stdscr.addstr(h//2, w//2-(len(no_user_found)//2)-1, no_user_found)
        stdscr.refresh()
        time.sleep(0.6)
        stdscr.attroff(curses.color_pair(3))
        self._clearContent(stdscr, h, w, menu_height)
        stdscr.refresh()
        self.checkUConsultController.userHome()

    def main(self):
        wrapper(self._move)

    def close(self):
        return
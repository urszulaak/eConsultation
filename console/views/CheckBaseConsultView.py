from shared_core.View import View
import curses
import time
from curses import wrapper
from views.Custom import Custom

class CheckBaseConsultView(View):

    def __init__(self, controller,response=None):
        super().__init__()
        self.controller = controller
        self.response = response
        self.custom = Custom

    def _content(self, stdscr, current_row, content, start_index, visible_items):
        h, w = stdscr.getmaxyx()
        self.custom.clearContent(stdscr)
        self.custom.initialize_colors(stdscr)
        curses.curs_set(0)

        menu_height = 11
        exit_text = "Exit [ctrl+E]"
        stdscr.attron(curses.color_pair(2))
        stdscr.addstr(menu_height + 1, w // 2 - (len(exit_text) // 2), exit_text, curses.color_pair(5))
        stdscr.attroff(curses.color_pair(2))
        menu_height = 13
        if not content:
            no_consult_found = "\u274c NO CONSULT FOUND! \u274c"
            no_consult_found2 = "    NO CONSULT FOUND!    "
            self.custom.message(stdscr, no_consult_found, no_consult_found2, 0)
            self.checkUConsultController.home()
        box_height = (h - menu_height - 2) // visible_items
        box_width = w - 2

        visible_content = content[start_index:start_index + visible_items]

        for idx, row in enumerate(visible_content):
            x = 1
            y = menu_height + idx * box_height

            win = curses.newwin(box_height, box_width, y, x)
            win.attron(curses.color_pair(4))
            win.box()
            win.attroff(curses.color_pair(4))

            text_x = 2
            text_y = box_height // 2

            if idx + start_index == current_row:
                win.addstr(text_y, text_x, str(row)[2:-2],curses.color_pair(3))
            else:
                win.addstr(text_y, text_x, str(row)[2:-2])

            win.refresh()

    def _move(self, stdscr):
        current_row = 0
        start_index = 0
        visible_items = 5
        content = self.controller.getConsult()
        self._content(stdscr, current_row, content, start_index, visible_items)

        while 1:
            key = stdscr.getch()
            if key == curses.KEY_UP:
                if current_row > 0:
                    current_row -= 1
                    if current_row < start_index:
                        start_index = max(0, current_row - visible_items + 1)

            elif key == curses.KEY_DOWN:
                if current_row < len(content) - 1:
                    current_row += 1
                    if current_row >= start_index + visible_items:
                        start_index = min(len(content) - visible_items, current_row)

            elif key == 5:
                stdscr.refresh()
                self.controller.home()

            self._content(stdscr, current_row, content, start_index, visible_items)

    def main(self):
        wrapper(self._move)

    def close(self):
        return
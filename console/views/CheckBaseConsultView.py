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
        exit_text = "Exit [ctrl+E], Delete consult [C]"
        stdscr.attron(curses.color_pair(2))
        stdscr.addstr(menu_height + 1, w // 2 - (len(exit_text) // 2), exit_text, curses.color_pair(5))
        stdscr.attroff(curses.color_pair(2))
        menu_height = 13
        if not content:
            no_consult_found = "\u274c NO CONSULTS FOUND! \u274c"
            no_consult_found2 = "    NO CONSULTS FOUND!    "
            self.custom.message(stdscr, no_consult_found, no_consult_found2, 0)
            self.controller.home()
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

            consult_id, c_date, last_name, first_name, title, description, stamp = row
            formatted_row = (
                f"Date: {c_date} | Time: {stamp} | "
                f"Teacher: {last_name} {first_name} | "
                f"Topic: {title} | Description: {description}"
            )

            if idx + start_index == current_row:
                win.addstr(text_y, text_x, formatted_row, curses.color_pair(3))
            else:
                win.addstr(text_y, text_x, formatted_row)

            win.refresh()
    
    def _confirmation_window(self, stdscr, current_row):
        h, w = stdscr.getmaxyx()
        win_height, win_width = h // 3, w // 4
        win_y, win_x = h // 2 - win_height // 2, w // 2 - win_width // 2

        win = curses.newwin(win_height, win_width, win_y, win_x)
        curses.curs_set(0)
        win.keypad(True)
        win.box()

        question = "Do you really want to delete?"
        yes_option = "Delete"
        no_option = "No"

        current_option = 0

        while True:
            win.clear()
            win.box()
            win.addstr(2, win_width // 2 - len(question) // 2, question)

            if current_option == 0:
                win.addstr(4, win_width // 4, yes_option, curses.color_pair(7))
                win.addstr(4, 3 * win_width // 4 - len(no_option), no_option, curses.color_pair(11))
            else:
                win.addstr(4, win_width // 4, yes_option, curses.color_pair(5))
                win.addstr(4, 3 * win_width // 4 - len(no_option), no_option, curses.color_pair(12))

            win.refresh()

            key = win.getch()

            if key == curses.KEY_LEFT:
                current_option = 0
            elif key == curses.KEY_RIGHT:
                current_option = 1
            elif key == 5:
                current_option = 1
                return current_option
            elif key == curses.KEY_ENTER or key in [10, 13]:
                return current_option

    def _move(self, stdscr):
        current_row = 0
        start_index = 0
        visible_items = 5
        content = self.controller.getConsult()
        self._content(stdscr, current_row, content, start_index, visible_items)

        while True:
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

            elif key == ord('c'):
                choice = self._confirmation_window(stdscr, current_row)
                if choice == 0:
                    consult_id = content[current_row][0]
                    self.controller.delete_consult(consult_id)
                    content = self.controller.getConsult()
                    current_row = 0
                    start_index = 0

            elif key == 5:
                stdscr.refresh()
                self.controller.home()

            self._content(stdscr, current_row, content, start_index, visible_items)

    def main(self):
        wrapper(self._move)

    def close(self):
        return
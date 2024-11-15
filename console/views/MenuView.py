import curses
from curses import wrapper
from views.Custom import Custom
from shared_core.View import View


class MenuView(View):
    def __init__(self, controller, response):
        super().__init__()
        self.controller = controller
        self.response = response
        self.custom = Custom

    def _content(self, stdscr, current_row, content):
        curses.curs_set(0)
        self.custom.clearContent(stdscr)
        self.custom.initialize_colors(stdscr)
        self.custom.list(stdscr, current_row, content)

    def _move(self, stdscr):
        current_row = 0
        content = self.get_menu_content()
        self._content(stdscr, current_row, content)

        while True:
            key = stdscr.getch()
            if key == curses.KEY_UP and current_row > 0:
                current_row -= 1
            elif key == curses.KEY_DOWN and current_row < len(content) - 1:
                current_row += 1
            elif key in [curses.KEY_ENTER, 10, 13]:
                self.controller.menuChoice(current_row)
            elif key == 5:
                self.controller.menuChoice(len(content) - 1)
            elif key in self.get_shortcuts():
                current_row = self.get_shortcuts()[key]
                self.controller.menuChoice(current_row)

            self._content(stdscr, current_row, content)

    def main(self):
        wrapper(self._move)

    def close(self):
        return

    def get_menu_content(self):
        pass

    def get_shortcuts(self):
        return {}

from core.View import View
import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle

class HomeView(View):

    def __init__(self, controller):
        super().__init__()
        self.homeController = controller

    def _menuBar(self, stdscr):
        ascii_art = """
     _ _
.-. | | |
|M|_|A|N|__
|A|a|.|.|\\ \\
|T|r| | | \\ \\
|H|t|M|Z|  \\ \\
| |!| | |   \\ \\
"""
        text = """
       _____                      _ _        _   _             
      / ____|                    | | |      | | (_)            
  ___| |     ___  _ __  ___ _   _| | |_ __ _| |_ _  ___  _ __  
 / _ \\ |    / _ \\| '_ \\/ __| | | | | __/ _` | __| |/ _ \\| '_ \\ 
|  __/ |___| (_) | | | \\__ \\ |_| | | || (_| | |_| | (_) | | | |
 \\___|\\_____\\___/|_| |_|___/\\__,_|_|\\__\\__,_|\\__|_|\\___/|_| |_|
"""

        stdscr.clear()
        curses.curs_set(0)
        h, w = stdscr.getmaxyx()
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_RED)

        ascii_lines = ascii_art.splitlines()
        text_lines = text.splitlines()
        max_ascii_width = max(len(line) for line in ascii_lines)
        max_text_width = max(len(line) for line in text_lines)

        for i, line in enumerate(ascii_lines):
            stdscr.addstr(0 + i, 0, line)

        text_x = w // 2 - max_text_width // 2
        for i, line in enumerate(text_lines):
            stdscr.addstr(0 + i, text_x, line)

        right_ascii_x = w - max_ascii_width
        for i, line in enumerate(ascii_lines):
            stdscr.addstr(0 + i, right_ascii_x, line)

        stdscr.attron(curses.color_pair(1))
        stdscr.hline(h // 4, 0, ' ', w)
        stdscr.attroff(curses.color_pair(1))
        stdscr.refresh()
        self._move(stdscr, h, w)


    def _content(self, stdscr, current_row, h, w, content):
        curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLUE)
        for id, row in enumerate(content):
            x = w // 2 - len(row) // 2
            y = h // 2 - len(content) // 2 +id
            if id == current_row:
                stdscr.attron(curses.color_pair(2))
                stdscr.addstr(y, x, row)
                stdscr.attroff(curses.color_pair(2))
            else:
                stdscr.addstr(y, x, row)
        stdscr.refresh()


    def _move(self, stdscr, h, w):
        current_row = 0
        content = ['Login', 'Register', 'Information', 'Graphic version', 'Exit']
        self._content(stdscr, current_row, h, w, content)
        while 1:
            key = stdscr.getch()
            if key == curses.KEY_UP and current_row > 0:
                current_row -= 1
            elif key == curses.KEY_DOWN and current_row < len(content)-1:
                current_row += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                stdscr.getch()
                self.homeController._menuChoice(current_row)
            
            self._content(stdscr, current_row, h, w, content)



    def main(self):
        wrapper(self._menuBar)

    def close(self):
        return
    

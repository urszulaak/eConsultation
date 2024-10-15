from core.View import View
import curses
from curses import wrapper

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
 / _ \ |    / _ \| '_ \/ __| | | | | __/ _` | __| |/ _ \| '_ \ 
|  __/ |___| (_) | | | \__ \ |_| | | || (_| | |_| | (_) | | | |
 \___|\_____\___/|_| |_|___/\__,_|_|\__\__,_|\__|_|\___/|_| |_|
"""

        stdscr.clear()
        curses.curs_set(0)
        h, w = stdscr.getmaxyx()
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)

        ascii_lines = ascii_art.splitlines()
        text_lines = text.splitlines()
        max_ascii_width = max(len(line) for line in ascii_lines)
        max_text_width = max(len(line) for line in text_lines)
        start_y = h // 50

        for i, line in enumerate(ascii_lines):
            stdscr.addstr(start_y + i, 0, line)

        text_x = w - max_text_width - max_ascii_width*2
        for i, line in enumerate(text_lines):
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(start_y + i, text_x, line)
            stdscr.attroff(curses.color_pair(1))

        right_ascii_start_x = w - max_ascii_width
        for i, line in enumerate(ascii_lines):
            stdscr.addstr(start_y + i, right_ascii_start_x, line)

        stdscr.hline(h // 4, 0, '-', w)
        # stdscr.refresh()
        # stdscr.getch()


    def _content(self, stdscr):
        h, w = stdscr.getmaxyx()
        key = stdscr.getch()
        content = ['Login', 'Register', 'Information']
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)

        # for i, line in enumerate(content):
        #     start_y = h // 2 + i
        #     start_x = w // 2
        #     if i == 

    def _move(self, stdscr):
        key = stdscr.getch()
        current_row = 0
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN:
            pass

    def main(self):
        wrapper(self._menuBar)

    def close(self):
        return
    

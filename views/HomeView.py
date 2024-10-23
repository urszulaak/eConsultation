from core.View import View
import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle
import time

class HomeView(View):

    def __init__(self, controller,response=None):
        super().__init__()
        self.homeController = controller

    def draw_rounded_box(win, y, x, height, width):
        # Zdefiniuj znaki dla zaokrąglonych rogów i krawędzi
        win.addch(y, x, curses.ACS_ULCORNER)  # Lewy górny róg
        win.addch(y, x + width - 1, curses.ACS_URCORNER)  # Prawy górny róg
        win.addch(y + height - 1, x, curses.ACS_LLCORNER)  # Lewy dolny róg
        win.addch(y + height - 1, x + width - 1, curses.ACS_LRCORNER)  # Prawy dolny róg

        # Rysuj górną i dolną krawędź
        for i in range(1, width - 1):
            win.addch(y, x + i, curses.ACS_HLINE)  # Górna krawędź
            win.addch(y + height - 1, x + i, curses.ACS_HLINE)  # Dolna krawędź

        # Rysuj lewą i prawą krawędź
        for i in range(1, height - 1):
            win.addch(y + i, x, curses.ACS_VLINE)  # Lewa krawędź
            win.addch(y + i, x + width - 1, curses.ACS_VLINE)  # Prawa krawędź

        # Wypełnij wnętrze (opcjonalnie)
        for i in range(1, height - 1):
            for j in range(1, width - 1):
                win.addch(y + i, x + j, ' ')

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
        menu_height = 0

        for i, line in enumerate(ascii_lines):
            stdscr.addstr(0 + i, 0, line)

        text_x = w // 2 - max_text_width // 2
        for i, line in enumerate(text_lines):
            stdscr.addstr(0 + i, text_x, line)

        right_ascii_x = w - max_ascii_width
        for i, line in enumerate(ascii_lines):
            stdscr.addstr(0 + i, right_ascii_x, line)
            menu_height +=1

        stdscr.attron(curses.color_pair(1))
        stdscr.hline(menu_height , 0, ' ', w)
        stdscr.attroff(curses.color_pair(1))
        stdscr.border()
        stdscr.refresh()
        self._move(stdscr, h, w, menu_height)


    def _content(self, stdscr, current_row, h, w, content, menu_height):
        
        menu_height += 1

        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_WHITE)
        num_items = len(content)
        
        available_height = h - menu_height
        
        box_height = available_height // num_items
        
        box_width = w - 2

        for id, row in enumerate(content):
            x = 1
            y = menu_height + id * box_height

            win = curses.newwin(box_height, box_width, y, x)
            win.box()


            text_x = (box_width - len(row)) // 2
            text_y = box_height // 2

            if id == current_row:
                win.attron(curses.color_pair(2))
                win.addstr(text_y, text_x, row)
                win.attroff(curses.color_pair(2))
            else:
                win.addstr(text_y, text_x, row)

            win.refresh()

        stdscr.refresh()



    def _clearContent(self, stdscr, h, w, menu_height):
        start_y = menu_height + 1
        end_y = h - 1

        for i in range(start_y, end_y):
            stdscr.move(i, 1)
            stdscr.clrtoeol()
        stdscr.border()
        stdscr.refresh()

    def _move(self, stdscr, h, w, menu_height):
        current_row = 0
        content = ['Login [L]', 'Register [R]', 'Information [I]', 'Graphic version [G]', 'Exit [E]']
        self._content(stdscr, current_row, h, w, content, menu_height)
        while 1:
            key = stdscr.getch()
            if key == (curses.KEY_UP) and current_row > 0:
                current_row -= 1
            elif key == curses.KEY_DOWN and current_row < len(content)-1:
                current_row += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                self._clearContent(stdscr, h, w, menu_height)
                self.homeController._menuChoice(current_row)
            elif key in [ord('l'), ord('r'), ord('i'), ord('g'), ord('e')]:
                if key == ord('l'):
                    current_row = 0
                elif key == ord('r'):
                    current_row = 1
                elif key == ord('i'):
                    current_row = 2
                elif key == ord('g'):
                    current_row = 3
                elif key == ord('e'):
                    current_row = 4
                self._clearContent(stdscr, h, w, menu_height)
                self.homeController._menuChoice(current_row)
            
            self._content(stdscr, current_row, h, w, content, menu_height)



    def main(self):
        wrapper(self._menuBar)

    def close(self):
        return
    

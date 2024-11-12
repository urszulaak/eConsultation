from shared_core.View import View
from shared_core.ViewFactory import ViewFactory
import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle
import time

class HomeView(View):

    def __init__(self, controller,response=None):
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

███████╗ ██████╗ ██████╗ ███╗   ██╗███████╗██╗   ██╗██╗  ████████╗ █████╗ ████████╗██╗ ██████╗ ███╗   ██╗
██╔════╝██╔════╝██╔═══██╗████╗  ██║██╔════╝██║   ██║██║  ╚══██╔══╝██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║
█████╗  ██║     ██║   ██║██╔██╗ ██║███████╗██║   ██║██║     ██║   ███████║   ██║   ██║██║   ██║██╔██╗ ██║
██╔══╝  ██║     ██║   ██║██║╚██╗██║╚════██║██║   ██║██║     ██║   ██╔══██║   ██║   ██║██║   ██║██║╚██╗██║
███████╗╚██████╗╚██████╔╝██║ ╚████║███████║╚██████╔╝███████╗██║   ██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║
╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
                                                                                                         

"""

        stdscr.clear()
        curses.curs_set(0)
        h, w = stdscr.getmaxyx()
        curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLUE)
        curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLUE)
        curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)

        ascii_lines = ascii_art.splitlines()
        text_lines = text.splitlines()
        max_ascii_width = max(len(line) for line in ascii_lines)
        max_text_width = max(len(line) for line in text_lines)
        menu_height = -1

        # for i, line in enumerate(ascii_lines):
        #     stdscr.addstr(0 + i, 0, line)

        text_x = w // 2 - max_text_width // 2
        for i, line in enumerate(text_lines):
            stdscr.attron(curses.color_pair(3))
            stdscr.addstr(0 + i, text_x, line)
            stdscr.attroff(curses.color_pair(3))
            menu_height += 1

        # right_ascii_x = max_text_width
        # for i, line in enumerate(ascii_lines):
        #     stdscr.addstr(0 + i, right_ascii_x, line)
        #     menu_height +=1

        stdscr.attron(curses.color_pair(1))
        stdscr.hline(menu_height , 0, ' ', w)
        stdscr.attroff(curses.color_pair(1))
        stdscr.refresh()
        self._move(stdscr, h, w, menu_height)


    def _content(self, stdscr, current_row, h, w, content, menu_height):
        
        menu_height += 1

        num_items = len(content)
        
        available_height = h - menu_height
        
        box_height = available_height // num_items
        
        box_width = w - 2

        for id, row in enumerate(content):
            x = 1
            y = menu_height + id * box_height

            win = curses.newwin(box_height, box_width, y, x)

            win.attron(curses.color_pair(3))
            win.box()
            win.attroff(curses.color_pair(3))


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
        end_y = h

        for i in range(start_y, end_y):
            stdscr.move(i, 0)
            stdscr.clrtoeol()
        stdscr.refresh()

    def _move(self, stdscr, h, w, menu_height):
        current_row = 0
        content = ['Login [L]', 'Register [R]', 'Information [I]', 'Graphic version [G]', 'Exit [ctrl + E]']
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
            elif key in [ord('l'), ord('r'), ord('i'), ord('g')]:
                if key == ord('l'):
                    current_row = 0
                elif key == ord('r'):
                    current_row = 1
                elif key == ord('i'):
                    current_row = 2
                elif key == ord('g'):
                    current_row = 3
                self._clearContent(stdscr, h, w, menu_height)
                self.homeController._menuChoice(current_row)
            elif key == 5:
                current_row = 4
                self._clearContent(stdscr, h, w, menu_height)
                self.homeController._menuChoice(current_row)
            
            self._content(stdscr, current_row, h, w, content, menu_height)



    def main(self):
        wrapper(self._menuBar)

    def close(self):
        return
    
